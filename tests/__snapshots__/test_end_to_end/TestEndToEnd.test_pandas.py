import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""from pandas import DataFrame
v = 4
df = DataFrame([[1,2], [3,v]])
df[0].astype(str)
assert df.size == 4
new_df = df.iloc[:, 1]
assert new_df.size == 2
""",
    location=PosixPath("[source file path]"),
)
call_1 = CallNode(
    function_id=LookupNode(
        name="getattr",
    ).id,
    positional_args=[
        ImportNode(
            source_location=SourceLocation(
                lineno=1,
                col_offset=0,
                end_lineno=1,
                end_col_offset=28,
                source_code=source_1.id,
            ),
            library=Library(
                name="pandas",
            ),
        ).id,
        LiteralNode(
            value="DataFrame",
        ).id,
    ],
)
global_1 = GlobalNode(
    name="foo",
    call_id=call_1.id,
)
global_2 = GlobalNode(
    name="c",
    call_id=call_1.id,
)
global_3 = GlobalNode(
    name="a",
    call_id=call_1.id,
)
global_4 = GlobalNode(
    name="b",
    call_id=call_1.id,
)
global_5 = GlobalNode(
    name="x",
    call_id=call_1.id,
)
global_6 = GlobalNode(
    name="my_function",
    call_id=call_1.id,
)
global_7 = GlobalNode(
    name="math",
    call_id=call_1.id,
)
global_8 = GlobalNode(
    name="bs",
    call_id=call_1.id,
)
call_5 = CallNode(
    source_location=SourceLocation(
        lineno=3,
        col_offset=5,
        end_lineno=3,
        end_col_offset=30,
        source_code=source_1.id,
    ),
    function_id=call_1.id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=3,
                col_offset=15,
                end_lineno=3,
                end_col_offset=29,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="l_list",
            ).id,
            positional_args=[
                CallNode(
                    source_location=SourceLocation(
                        lineno=3,
                        col_offset=16,
                        end_lineno=3,
                        end_col_offset=21,
                        source_code=source_1.id,
                    ),
                    function_id=LookupNode(
                        name="l_list",
                    ).id,
                    positional_args=[
                        LiteralNode(
                            source_location=SourceLocation(
                                lineno=3,
                                col_offset=17,
                                end_lineno=3,
                                end_col_offset=18,
                                source_code=source_1.id,
                            ),
                            value=1,
                        ).id,
                        LiteralNode(
                            source_location=SourceLocation(
                                lineno=3,
                                col_offset=19,
                                end_lineno=3,
                                end_col_offset=20,
                                source_code=source_1.id,
                            ),
                            value=2,
                        ).id,
                    ],
                ).id,
                CallNode(
                    source_location=SourceLocation(
                        lineno=3,
                        col_offset=23,
                        end_lineno=3,
                        end_col_offset=28,
                        source_code=source_1.id,
                    ),
                    function_id=LookupNode(
                        name="l_list",
                    ).id,
                    positional_args=[
                        LiteralNode(
                            source_location=SourceLocation(
                                lineno=3,
                                col_offset=24,
                                end_lineno=3,
                                end_col_offset=25,
                                source_code=source_1.id,
                            ),
                            value=3,
                        ).id,
                        LiteralNode(
                            source_location=SourceLocation(
                                lineno=2,
                                col_offset=4,
                                end_lineno=2,
                                end_col_offset=5,
                                source_code=source_1.id,
                            ),
                            value=4,
                        ).id,
                    ],
                ).id,
            ],
        ).id
    ],
)
call_8 = CallNode(
    source_location=SourceLocation(
        lineno=4,
        col_offset=0,
        end_lineno=4,
        end_col_offset=17,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        source_location=SourceLocation(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=12,
            source_code=source_1.id,
        ),
        function_id=LookupNode(
            name="getattr",
        ).id,
        positional_args=[
            CallNode(
                source_location=SourceLocation(
                    lineno=4,
                    col_offset=0,
                    end_lineno=4,
                    end_col_offset=5,
                    source_code=source_1.id,
                ),
                function_id=LookupNode(
                    name="getitem",
                ).id,
                positional_args=[
                    call_5.id,
                    LiteralNode(
                        source_location=SourceLocation(
                            lineno=4,
                            col_offset=3,
                            end_lineno=4,
                            end_col_offset=4,
                            source_code=source_1.id,
                        ),
                        value=0,
                    ).id,
                ],
            ).id,
            LiteralNode(
                value="astype",
            ).id,
        ],
    ).id,
    positional_args=[
        LookupNode(
            name="str",
        ).id
    ],
)
call_11 = CallNode(
    source_location=SourceLocation(
        lineno=5,
        col_offset=0,
        end_lineno=5,
        end_col_offset=19,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="l_assert",
    ).id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=5,
                col_offset=7,
                end_lineno=5,
                end_col_offset=19,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="eq",
            ).id,
            positional_args=[
                CallNode(
                    source_location=SourceLocation(
                        lineno=5,
                        col_offset=7,
                        end_lineno=5,
                        end_col_offset=14,
                        source_code=source_1.id,
                    ),
                    function_id=LookupNode(
                        name="getattr",
                    ).id,
                    positional_args=[
                        call_5.id,
                        LiteralNode(
                            value="size",
                        ).id,
                    ],
                ).id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=5,
                        col_offset=18,
                        end_lineno=5,
                        end_col_offset=19,
                        source_code=source_1.id,
                    ),
                    value=4,
                ).id,
            ],
        ).id
    ],
)
call_18 = CallNode(
    source_location=SourceLocation(
        lineno=7,
        col_offset=0,
        end_lineno=7,
        end_col_offset=23,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="l_assert",
    ).id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=7,
                end_lineno=7,
                end_col_offset=23,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="eq",
            ).id,
            positional_args=[
                CallNode(
                    source_location=SourceLocation(
                        lineno=7,
                        col_offset=7,
                        end_lineno=7,
                        end_col_offset=18,
                        source_code=source_1.id,
                    ),
                    function_id=LookupNode(
                        name="getattr",
                    ).id,
                    positional_args=[
                        CallNode(
                            source_location=SourceLocation(
                                lineno=6,
                                col_offset=9,
                                end_lineno=6,
                                end_col_offset=22,
                                source_code=source_1.id,
                            ),
                            function_id=LookupNode(
                                name="getitem",
                            ).id,
                            positional_args=[
                                CallNode(
                                    source_location=SourceLocation(
                                        lineno=6,
                                        col_offset=9,
                                        end_lineno=6,
                                        end_col_offset=16,
                                        source_code=source_1.id,
                                    ),
                                    function_id=LookupNode(
                                        name="getattr",
                                    ).id,
                                    positional_args=[
                                        call_5.id,
                                        LiteralNode(
                                            value="iloc",
                                        ).id,
                                    ],
                                ).id,
                                CallNode(
                                    source_location=SourceLocation(
                                        lineno=6,
                                        col_offset=17,
                                        end_lineno=6,
                                        end_col_offset=21,
                                        source_code=source_1.id,
                                    ),
                                    function_id=LookupNode(
                                        name="l_tuple",
                                    ).id,
                                    positional_args=[
                                        CallNode(
                                            source_location=SourceLocation(
                                                lineno=6,
                                                col_offset=17,
                                                end_lineno=6,
                                                end_col_offset=18,
                                                source_code=source_1.id,
                                            ),
                                            function_id=LookupNode(
                                                name="slice",
                                            ).id,
                                            positional_args=[LiteralNode().id],
                                        ).id,
                                        LiteralNode(
                                            source_location=SourceLocation(
                                                lineno=6,
                                                col_offset=20,
                                                end_lineno=6,
                                                end_col_offset=21,
                                                source_code=source_1.id,
                                            ),
                                            value=1,
                                        ).id,
                                    ],
                                ).id,
                            ],
                        ).id,
                        LiteralNode(
                            value="size",
                        ).id,
                    ],
                ).id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=7,
                        col_offset=22,
                        end_lineno=7,
                        end_col_offset=23,
                        source_code=source_1.id,
                    ),
                    value=2,
                ).id,
            ],
        ).id
    ],
)
