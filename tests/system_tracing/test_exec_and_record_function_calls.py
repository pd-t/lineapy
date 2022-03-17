import operator
from collections import Counter
from typing import List

import pytest

from lineapy.system_tracing.exec_and_record_function_calls import (
    exec_and_record_function_calls,
)
from lineapy.system_tracing.function_call import FunctionCall
from tests.util import IsInstance

is_list_iter = IsInstance(type(iter([])))


@pytest.mark.parametrize(
    "source_code,globals_,function_calls",
    [
        pytest.param(
            # Example where unary positive returns different result than arg https://stackoverflow.com/a/18818979
            "+c",
            {"c": Counter({"a": -1})},
            [FunctionCall(operator.pos, [Counter({"a": -1})], {}, Counter())],
            id="UNARY_POSITIVE",
        ),
        pytest.param(
            "-x",
            {"x": -1},
            [FunctionCall(operator.neg, [-1], {}, 1)],
            id="UNARY_NEGATIVE",
        ),
        pytest.param(
            "not x",
            {"x": True},
            [FunctionCall(operator.not_, [True], {}, False)],
            id="UNARY_NOT",
        ),
        pytest.param(
            "~x",
            {"x": 1},
            [FunctionCall(operator.inv, [1], {}, -2)],
            id="UNARY_INVERT",
        ),
        pytest.param(
            "for _ in x: pass",
            {"x": [1, 2]},
            [
                FunctionCall(iter, [[1, 2]], {}, is_list_iter),
                FunctionCall(next, [is_list_iter], {}, 1),
                FunctionCall(next, [is_list_iter], {}, 2),
            ],
            id="GET_ITER and FOR_ITER",
        ),
    ],
)
def test_exec_and_record_function_calls(
    source_code: str, globals_, function_calls: List[FunctionCall]
):
    code = compile(source_code, "", "exec")
    trace_fn = exec_and_record_function_calls(code, globals_)
    assert not trace_fn.not_implemented_ops
    assert trace_fn.function_calls == function_calls
