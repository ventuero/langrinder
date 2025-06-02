import re

from . import LangrinderBaseParser


class LangrinderSyntaxParser(LangrinderBaseParser):
    TAB = " " * 4
    JOINER = "\n"
    MESSAGE_PATTERN = re.compile(
        r"@(?P<name>\w+)(?: ?= ?| )(?P<data>.+)",
        re.UNICODE,
    )
    BLOCK_PATTERN = re.compile(
        r"^@(?P<name>\w+)\n(?P<data>[^@]+)$",
        re.MULTILINE + re.UNICODE,
    )
