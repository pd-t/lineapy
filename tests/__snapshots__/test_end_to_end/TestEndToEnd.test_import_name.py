import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""import pandas as pd
assert pd.__name__ == \'pandas\'""",
    location=PosixPath("[source file path]"),
)
call_1 = CallNode(
    source_location=SourceLocation(
        lineno=2,
        col_offset=7,
        end_lineno=2,
        end_col_offset=18,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="getattr",
    ).id,
    positional_args=[
        ImportNode(
            source_location=SourceLocation(
                lineno=1,
                col_offset=0,
                end_lineno=1,
                end_col_offset=19,
                source_code=source_1.id,
            ),
            library=Library(
                name="pandas",
            ),
        ).id,
        LiteralNode(
            value="__name__",
        ).id,
    ],
)
global_1 = GlobalNode(
    name="foo",
    call_id=call_1.id,
)
global_2 = GlobalNode(
    name="math",
    call_id=call_1.id,
)
global_3 = GlobalNode(
    name="a",
    call_id=call_1.id,
)
global_4 = GlobalNode(
    name="df",
    call_id=call_1.id,
)
global_5 = GlobalNode(
    name="v",
    call_id=call_1.id,
)
global_6 = GlobalNode(
    name="pandas",
    call_id=call_1.id,
)
global_7 = GlobalNode(
    name="DataFrame",
    call_id=call_1.id,
)
global_8 = GlobalNode(
    name="bs",
    call_id=call_1.id,
)
global_9 = GlobalNode(
    name="c",
    call_id=call_1.id,
)
global_10 = GlobalNode(
    name="x",
    call_id=call_1.id,
)
global_11 = GlobalNode(
    name="b",
    call_id=call_1.id,
)
global_12 = GlobalNode(
    name="new_df",
    call_id=call_1.id,
)
global_13 = GlobalNode(
    name="my_function",
    call_id=call_1.id,
)
call_3 = CallNode(
    source_location=SourceLocation(
        lineno=2,
        col_offset=0,
        end_lineno=2,
        end_col_offset=30,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="l_assert",
    ).id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=7,
                end_lineno=2,
                end_col_offset=30,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="eq",
            ).id,
            positional_args=[
                call_1.id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=2,
                        col_offset=22,
                        end_lineno=2,
                        end_col_offset=30,
                        source_code=source_1.id,
                    ),
                    value="pandas",
                ).id,
            ],
        ).id
    ],
)
