import re

from . import LangrinderBaseParser


class LangrinderSyntaxParser(LangrinderBaseParser):
    TAB = " " * 4
    JOINER = "\n"
    MESSAGE_PATTERN = re.compile(
        r"(?P<message>@(?P<name>\w+)(?: ?= ?| )(?P<data>.+))",
        re.UNICODE,
    )
    BLOCK_PATTERN = re.compile(
        r"^@(?P<name>\w+)\n"
        r"(?P<data>(?:(?!@\w+\n).)*)",
        re.MULTILINE | re.UNICODE | re.DOTALL,
    )
