import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils.utils import get_new_id

source_1 = SourceCode(
    code="""import lineapy
from PIL.Image import open, new
new_img = new("RGB", (4,4))
new_img.save("test.png", "PNG")
e = open("test.png")

lineapy.save(e, \'e\')
""",
    location=PosixPath("[source file path]"),
)
import_2 = ImportNode(
    source_location=SourceLocation(
        lineno=2,
        col_offset=0,
        end_lineno=2,
        end_col_offset=31,
        source_code=source_1.id,
    ),
    name="PIL.Image",
    version="9.1.0",
    package_name="PIL.Image",
)
call_9 = CallNode(
    source_location=SourceLocation(
        lineno=7,
        col_offset=0,
        end_lineno=7,
        end_col_offset=20,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        source_location=SourceLocation(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=12,
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
                    end_col_offset=14,
                    source_code=source_1.id,
                ),
                name="lineapy",
                version="0.0.1",
                package_name="lineapy",
            ).id,
            LiteralNode(
                value="save",
            ).id,
        ],
    ).id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=5,
                col_offset=4,
                end_lineno=5,
                end_col_offset=20,
                source_code=source_1.id,
            ),
            function_id=CallNode(
                function_id=LookupNode(
                    name="getattr",
                ).id,
                positional_args=[
                    import_2.id,
                    LiteralNode(
                        value="open",
                    ).id,
                ],
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=5,
                        col_offset=9,
                        end_lineno=5,
                        end_col_offset=19,
                        source_code=source_1.id,
                    ),
                    value="test.png",
                ).id
            ],
            implicit_dependencies=[
                MutateNode(
                    source_id=LookupNode(
                        name="file_system",
                    ).id,
                    call_id=CallNode(
                        source_location=SourceLocation(
                            lineno=4,
                            col_offset=0,
                            end_lineno=4,
                            end_col_offset=31,
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
                                        lineno=3,
                                        col_offset=10,
                                        end_lineno=3,
                                        end_col_offset=27,
                                        source_code=source_1.id,
                                    ),
                                    function_id=CallNode(
                                        function_id=LookupNode(
                                            name="getattr",
                                        ).id,
                                        positional_args=[
                                            import_2.id,
                                            LiteralNode(
                                                value="new",
                                            ).id,
                                        ],
                                    ).id,
                                    positional_args=[
                                        LiteralNode(
                                            source_location=SourceLocation(
                                                lineno=3,
                                                col_offset=14,
                                                end_lineno=3,
                                                end_col_offset=19,
                                                source_code=source_1.id,
                                            ),
                                            value="RGB",
                                        ).id,
                                        CallNode(
                                            source_location=SourceLocation(
                                                lineno=3,
                                                col_offset=21,
                                                end_lineno=3,
                                                end_col_offset=26,
                                                source_code=source_1.id,
                                            ),
                                            function_id=LookupNode(
                                                name="l_tuple",
                                            ).id,
                                            positional_args=[
                                                LiteralNode(
                                                    source_location=SourceLocation(
                                                        lineno=3,
                                                        col_offset=22,
                                                        end_lineno=3,
                                                        end_col_offset=23,
                                                        source_code=source_1.id,
                                                    ),
                                                    value=4,
                                                ).id,
                                                LiteralNode(
                                                    source_location=SourceLocation(
                                                        lineno=3,
                                                        col_offset=24,
                                                        end_lineno=3,
                                                        end_col_offset=25,
                                                        source_code=source_1.id,
                                                    ),
                                                    value=4,
                                                ).id,
                                            ],
                                        ).id,
                                    ],
                                ).id,
                                LiteralNode(
                                    value="save",
                                ).id,
                            ],
                        ).id,
                        positional_args=[
                            LiteralNode(
                                source_location=SourceLocation(
                                    lineno=4,
                                    col_offset=13,
                                    end_lineno=4,
                                    end_col_offset=23,
                                    source_code=source_1.id,
                                ),
                                value="test.png",
                            ).id,
                            LiteralNode(
                                source_location=SourceLocation(
                                    lineno=4,
                                    col_offset=25,
                                    end_lineno=4,
                                    end_col_offset=30,
                                    source_code=source_1.id,
                                ),
                                value="PNG",
                            ).id,
                        ],
                    ).id,
                ).id
            ],
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=16,
                end_lineno=7,
                end_col_offset=19,
                source_code=source_1.id,
            ),
            value="e",
        ).id,
    ],
)
