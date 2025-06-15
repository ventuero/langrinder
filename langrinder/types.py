from dataclasses import dataclass, field
from functools import partial

langrinder_type = partial(dataclass, slots=True, frozen=True)


@langrinder_type()
class ParserParameters:
    vars_prefix: str = "@"
    indent: str = " " * 4
    blocks_end: str = ""
    joiner: str = "\n"
    message_separators: list[str] = field(
        default_factory=lambda: [":", "="],
    )
