import logging

from langrinder.parser.abc import ABCParser
from langrinder.types import ParserParameters

logger = logging.getLogger("langrinder.parser")


class SyntaxParser(ABCParser):
    def __init__(
            self,
            content: list[str],
            params: ParserParameters | None = None,
    ):
        self.results = {}
        if not params:
            params = ParserParameters()
        self.params = params
        self.content = [line.rstrip("\n") for line in content]

    def parse_blocks(self) -> None | dict[str, str]:  # noqa: C901
        current_var: str | None = None
        current_lines: list[str] | list[None] = []
        results: dict[str, str] | dict[None, None] = {}
        for line in self.content:
            if (line.startswith(self.params.vars_prefix)
                    and line.endswith(self.params.blocks_end)):
                logger.debug("Trying to parse block...")
                if current_var:
                    if current_lines[-1] == "":
                        current_lines.pop()
                    results[current_var] = self.params.joiner.join(current_lines)  # noqa: E501
                    logger.debug("Saved previous block name='%s'", current_var)
                current_var = (
                    line
                    .replace(self.params.vars_prefix, "")
                    .replace(self.params.blocks_end, "")
                )
                current_lines = []
                logger.debug("Current block: '%s'", current_var)

            if line.startswith(self.params.indent) and not current_var:
                logger.warning("Found text, but no current var. Skipping")
                continue

            if line.startswith(self.params.indent):
                logger.debug(
                    "Found %d text line for '%s' block. Appending",
                    len(current_lines), current_var,
                )
                current_lines.append(line[len(self.params.indent):])

            if line == "":
                logger.debug(
                    "Found %d text void line for '%s' block. Appending",
                    len(current_lines), current_var,
                )
                current_lines.append("")
        if current_var and current_lines:
            if current_lines[-1] == "":
                current_lines.pop()
            results[current_var] = self.params.joiner.join(current_lines)
        if not results:
            logger.debug("No blocks found")
            return None
        return results

    def is_separated(self, line: str):
        stripped = line.strip()
        for sep in self.params.message_separators:
            if (
                stripped.startswith(self.params.vars_prefix)
                and sep in stripped
            ):
                sep_index = stripped.find(sep)
                var_name = stripped[
                    len(self.params.vars_prefix) : sep_index
                ].strip()
                message = stripped[sep_index + len(sep) :].strip()
                if var_name:
                    return var_name, message
        return None

    def parse_messages(
        self,
    ) -> tuple[dict[str, str], set[int]] | tuple[None, None]:
        messages = {}
        message_lines = set()
        for i, line in enumerate(self.content):
            if result := self.is_separated(line):
                var, msg = result
                if msg == "":
                    logger.debug("Skipped void message name='%s'", var)
                    continue
                messages[var] = msg
                message_lines.add(i)
                logger.debug("Parsed message name='%s'", var)
        return (messages, message_lines) if messages else (None, None)

    def parse_all(self) -> dict[str, str] | None:
        results = {}

        messages, message_lines = self.parse_messages() or ({}, [])

        if messages and message_lines:
            logger.debug("Found %d messages", len(messages))
            results.update(messages)

        lines_for_blocks = [
            line
            for i, line in enumerate(self.content)
            if i not in message_lines
        ] if message_lines else self.content

        temp_parser = SyntaxParser(lines_for_blocks, self.params)
        blocks = temp_parser.parse_blocks()

        if blocks:
            logger.debug("Found %d blocks", len(blocks))
            results.update(blocks)

        return results or None
