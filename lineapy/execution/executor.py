import builtins
import importlib.util
from os import chdir, getcwd
import io
import subprocess
import sys
from typing import Any, Optional, Dict, cast
import time

from lineapy.utils import InternalLogicError, debug_log
import lineapy.lineabuiltins as lineabuiltins
from lineapy.data.graph import Graph
from lineapy.data.types import (
    LookupNode,
    SessionContext,
    NodeType,
    Node,
    CallNode,
    ImportNode,
    LiteralNode,
    SideEffectsNode,
    StateChangeNode,
    FunctionDefinitionNode,
    LineaID,
    VariableNode,
)
from lineapy.graph_reader.graph_util import get_segment_from_source_location


class Executor:
    def __init__(self):
        """
        TODO: documentation
        """
        self._variable_values: dict[str, object] = {}

        # Note: no output will be shown in Terminal because it is
        #       being redirected here
        self._old_stdout = sys.stdout
        self._stdout = io.StringIO()

    def teardown(self) -> None:
        chdir(self.prev_working_dir)

    def get_stdout(self) -> str:
        """
        This returns the text that corresponds to the stdout results.
        For instance, `print("hi")` should yield a result of "hi\n" from this function.

        Note:
        - If we assume that everything is sliced, the user printing may not
        happen, but third party libs may still have outputs.
        - Also the user may manually annotate for the print line to be
        included and in general stdouts are useful
        """

        val = self._stdout.getvalue()
        return val

    def get_value_by_variable_name(self, name: str) -> Any:
        if name in self._variable_values:
            return self._variable_values[name]
        else:
            # throwing internal logic error because this is only called
            #   for testing right now
            raise InternalLogicError(f"Cannot find variable {name}")

    def execute_program_with_inputs(
        self, program: Graph, inputs: Dict[LineaID, Any]
    ) -> Any:
        """
        Execute the `program` with specific `inputs`.
        Note: the inputs do not have to be root nodes in `program`. For
          a non-root node input, we should cut its dependencies.
          For example `a = foo(), b = a + 1`, if `a` is passed
          in as an input with value `2`, we should skip `foo()`.

        TODO:
        :param program: program to be run.
        :param inputs: mapping for node id to values for a set of input nodes.
        :return: result of the program run with specified inputs.
        """
        ...

    def execute_program(self, program: Graph) -> float:
        """
        Returns how long the program took
        TODO:
        - we should probably also return the stdout and any error messages
          as well in the near future
        """
        self.setup(program.session_context)
        start = time.time()
        self.walk(program)
        end = time.time()
        self.teardown()
        return end - start

    def setup_context_for_node(
        self,
        node: SideEffectsNode,
        program: Graph,
        scoped_locals: Dict[str, Any],
    ) -> None:
        if node.input_state_change_nodes is not None:
            for state_var_id in node.input_state_change_nodes:
                state_var = cast(
                    StateChangeNode, program.get_node(state_var_id)
                )
                initial_state = program.get_node(
                    state_var.initial_value_node_id
                )
                if initial_state is not None and initial_state.node_type in [
                    NodeType.CallNode,
                    NodeType.LiteralNode,
                    NodeType.StateChangeNode,
                ]:
                    scoped_locals[state_var.variable_name] = initial_state.value  # type: ignore

        if node.import_nodes is not None:
            for import_node_id in node.import_nodes:
                import_node = cast(
                    ImportNode, program.get_node(import_node_id)
                )
                import_node.module = importlib.import_module(import_node.library.name)  # type: ignore
                scoped_locals[import_node.library.name] = import_node.module

    def update_node_side_effects(
        self,
        node: Optional[Node],
        program: Graph,
        scoped_locals: Dict[str, Any],
    ) -> None:
        if node is None:
            return

        local_vars = scoped_locals
        node = cast(SideEffectsNode, node)
        if node.output_state_change_nodes is not None:
            for state_var_id in node.output_state_change_nodes:
                state_var = cast(
                    StateChangeNode, program.get_node(state_var_id)
                )

                state_var.value = local_vars[state_var.variable_name]

                if state_var.variable_name is not None:
                    self._variable_values[
                        state_var.variable_name
                    ] = state_var.value

    def walk(self, program: Graph) -> None:
        """
        FIXME: side effect evaluation is currently not supported
        """
        for node in program.visit_order():
            # If we have already executed this node, dont do it again
            # This shows up during jupyter cell exection
            if getattr(node, "value", None) is not None:
                continue

            scoped_locals = locals()

            # all of these have to be in the same scope in order to read
            # and write to scoped_locals properly using Python exec
            if node.node_type == NodeType.LookupNode:
                node = cast(LookupNode, node)
                node.value = lookup_value(node.name)
            elif node.node_type == NodeType.CallNode:
                node = cast(CallNode, node)
                fn = program.get_node(node.function_id).value  # type: ignore

                args, kwargs = program.get_arguments_from_call_node(node)

                sys.stdout = self._stdout
                val = fn(*args, **kwargs)
                sys.stdout = self._old_stdout

                node.value = val

            elif node.node_type == NodeType.ImportNode:
                node = cast(ImportNode, node)
                node.module = importlib.import_module(node.library.name)

            elif node.node_type in [NodeType.LoopNode, NodeType.ConditionNode]:
                node = cast(SideEffectsNode, node)
                # set up vars and imports
                self.setup_context_for_node(node, program, scoped_locals)
                source_location = node.source_location
                assert source_location
                exec(get_segment_from_source_location(source_location))
                self.update_node_side_effects(node, program, scoped_locals)

            elif node.node_type == NodeType.FunctionDefinitionNode:
                node = cast(FunctionDefinitionNode, node)
                source_location = node.source_location
                assert source_location
                self.setup_context_for_node(node, program, scoped_locals)
                exec(
                    get_segment_from_source_location(source_location),
                    scoped_locals,
                )
                node.value = scoped_locals[node.function_name]

            elif node.node_type == NodeType.LiteralNode:
                node = cast(LiteralNode, node)

            elif node.node_type == NodeType.VariableNode:
                node = cast(VariableNode, node)
                node.value = program.get_node_value(
                    program.ids[node.source_node_id]
                )

                self._variable_values[node.assigned_variable_name] = node.value

            # not all node cases are handled, including
            # - DataSourceNode
            # - ArgumentNode

    def validate(self, program: Graph) -> None:
        raise NotImplementedError("validate is not implemented!")


def lookup_value(name: str) -> object:
    """
    Lookup a value from a string identifier.
    """
    if hasattr(builtins, name):
        return getattr(builtins, name)
    if hasattr(lineabuiltins, name):
        return getattr(lineabuiltins, name)
    return globals()[name]
