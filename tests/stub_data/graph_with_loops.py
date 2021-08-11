from tests.util import get_new_id
from tests.stub_data.simple_graph import session
from lineapy.data.graph import Graph
from lineapy.data.types import (
    LiteralAssignNode,
    CallNode,
    LoopEnterNode,
    StateChangeNode,
    ArgumentNode,
)

"""
Original code:

```python
a = []
b = 0
for x in range(9):
    a.append(x)
    b+=x
x = sum(a)
y = x + b
```

Graph method notes:
- Re-execution
  - Given that the nodes are NOT unrolled, the re-execution will simply do `exec` on the code provided at the loop enter.
  - The loops will have side-effects, these variables deemed to be affected by the side effect will have a new ID from "StateChangeNode". The re-exec need to look up the value of the variable_name in StateChangeNode and give it a value at run time, for later nodes to reference.

"""


a_id = get_new_id()

line_1 = CallNode(
    id=a_id,
    session_id=session.uuid,
    code="a = []",
    function_name="list",
    assigned_variable_name="a",
)

b_id = get_new_id()

line_2 = LiteralAssignNode(
    id=b_id, session_id=session.uuid, code="b = 0", assigned_variable_name="b", value=0
)

x_id = get_new_id()


line_6 = CallNode(
    id=x_id,
    session_id=session.uuid,
    code="x = sum(a)",
    function_name="sum",
    assigned_variable_name="x",
    arguments=[a_argument_node],
)

x_argument_node = ArgumentNode(positional_order=0, value_node_id=x_id)

a_state_change_id = get_new_id()
a_argument_node = ArgumentNode(positional_order=0, value_call_id=a_state_change_id)
a_state_change = StateChangeNode(id=a_state_change_id, variable_name="a")

le_id = get_new_id()

b_state_change_id = get_new_id()
b_argument_node = ArgumentNode(positional_order=1, value_call_id=b_state_change_id)
b_state_change = StateChangeNode(id=b_state_change_id, variable_name="b", associated_node_id=le_id)

le = LoopEnterNode(
    id=le_id,
    session_id=session.uuid,
    # @Dhruv, please watch out for indentation oddities when you run into errors
    code="for x in range(9):\na.append(x)",
    state_change
)

line_7 = CallNode(
    id=a_id,
    session_id=session.uuid,
    code="y = x + b",
    function_name="add",
    function_module="operator",  # built in
    assigned_variable_name="y",
    arguments=[x_argument_node, b_argument_node],
)



graph_with_loops = Graph(
    [
        line_1,
        line_2,
        a_argument_node,
        x_argument_node,
        b_argument_node,
        le,
        a_state_change,
        b_state_change,
        line_6,
        line_7,
    ]
)
