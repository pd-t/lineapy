import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="x = [1, 2, 3][::2]",
    location=PosixPath("[source file path]"),
)
call_1 = CallNode(
    source_location=SourceLocation(
        lineno=1,
        col_offset=4,
        end_lineno=1,
        end_col_offset=13,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="l_list",
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=1,
                col_offset=5,
                end_lineno=1,
                end_col_offset=6,
                source_code=source_1.id,
            ),
            value=1,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=1,
                col_offset=8,
                end_lineno=1,
                end_col_offset=9,
                source_code=source_1.id,
            ),
            value=2,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=1,
                col_offset=11,
                end_lineno=1,
                end_col_offset=12,
                source_code=source_1.id,
            ),
            value=3,
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
    name="r10",
    call_id=call_1.id,
)
global_6 = GlobalNode(
    name="r9",
    call_id=call_1.id,
)
global_7 = GlobalNode(
    name="obj",
    call_id=call_1.id,
)
global_8 = GlobalNode(
    name="Decimal",
    call_id=call_1.id,
)
global_9 = GlobalNode(
    name="decimal",
    call_id=call_1.id,
)
global_10 = GlobalNode(
    name="y",
    call_id=call_1.id,
)
global_11 = GlobalNode(
    name="clf",
    call_id=call_1.id,
)
global_12 = GlobalNode(
    name="is_new",
    call_id=call_1.id,
)
global_13 = GlobalNode(
    name="assets",
    call_id=call_1.id,
)
global_14 = GlobalNode(
    name="sklearn.ensemble",
    call_id=call_1.id,
)
global_15 = GlobalNode(
    name="sns",
    call_id=call_1.id,
)
global_16 = GlobalNode(
    name="alt",
    call_id=call_1.id,
)
global_17 = GlobalNode(
    name="e",
    call_id=call_1.id,
)
global_18 = GlobalNode(
    name="d",
    call_id=call_1.id,
)
global_19 = GlobalNode(
    name="altair",
    call_id=call_1.id,
)
global_20 = GlobalNode(
    name="ls",
    call_id=call_1.id,
)
global_21 = GlobalNode(
    name="v",
    call_id=call_1.id,
)
global_22 = GlobalNode(
    name="r8",
    call_id=call_1.id,
)
global_23 = GlobalNode(
    name="r7",
    call_id=call_1.id,
)
global_24 = GlobalNode(
    name="pandas",
    call_id=call_1.id,
)
global_25 = GlobalNode(
    name="DataFrame",
    call_id=call_1.id,
)
global_26 = GlobalNode(
    name="r5",
    call_id=call_1.id,
)
global_27 = GlobalNode(
    name="r6",
    call_id=call_1.id,
)
global_28 = GlobalNode(
    name="r4",
    call_id=call_1.id,
)
global_29 = GlobalNode(
    name="types",
    call_id=call_1.id,
)
global_30 = GlobalNode(
    name="r2",
    call_id=call_1.id,
)
global_31 = GlobalNode(
    name="r1",
    call_id=call_1.id,
)
global_32 = GlobalNode(
    name="img",
    call_id=call_1.id,
)
global_33 = GlobalNode(
    name="RandomForestClassifier",
    call_id=call_1.id,
)
global_34 = GlobalNode(
    name="PIL.Image",
    call_id=call_1.id,
)
global_35 = GlobalNode(
    name="plt",
    call_id=call_1.id,
)
global_36 = GlobalNode(
    name="pd",
    call_id=call_1.id,
)
global_37 = GlobalNode(
    name="r11",
    call_id=call_1.id,
)
global_38 = GlobalNode(
    name="r3",
    call_id=call_1.id,
)
global_39 = GlobalNode(
    name="c",
    call_id=call_1.id,
)
global_40 = GlobalNode(
    name="x",
    call_id=call_1.id,
)
global_41 = GlobalNode(
    name="open",
    call_id=call_1.id,
)
global_42 = GlobalNode(
    name="bs",
    call_id=call_1.id,
)
global_43 = GlobalNode(
    name="b",
    call_id=call_1.id,
)
global_44 = GlobalNode(
    name="new_df",
    call_id=call_1.id,
)
global_45 = GlobalNode(
    name="my_function",
    call_id=call_1.id,
)
call_3 = CallNode(
    source_location=SourceLocation(
        lineno=1,
        col_offset=4,
        end_lineno=1,
        end_col_offset=18,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="getitem",
    ).id,
    positional_args=[
        call_1.id,
        CallNode(
            source_location=SourceLocation(
                lineno=1,
                col_offset=14,
                end_lineno=1,
                end_col_offset=17,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="slice",
            ).id,
            positional_args=[
                LiteralNode().id,
                LiteralNode().id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=1,
                        col_offset=16,
                        end_lineno=1,
                        end_col_offset=17,
                        source_code=source_1.id,
                    ),
                    value=2,
                ).id,
            ],
        ).id,
    ],
)
