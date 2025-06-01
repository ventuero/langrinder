import re

from . import LangrinderBaseParser


class LangrinderSyntaxParser(LangrinderBaseParser):
    TAB = " " * 4
    JOINER = "\n"
    MESSAGE_PATTERN = re.compile(
        r"^@(?P<name>[\w_\d]+)"
        r"(?:"
        r"\s*=?\s*(?P<inline_data>[^\n]+)"
        r"|"
        r"\n(?P<block_data>(?: {4}[^\n]*\n?)*)"
        r")?"
        r"(?=\n@|\Z)",
        re.IGNORECASE | re.MULTILINE | re.DOTALL | re.UNICODE,
    )
