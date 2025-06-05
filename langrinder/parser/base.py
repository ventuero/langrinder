import re

from telegrinder.modules import logger


class LangrinderBaseParser:
    TAB: str
    JOINER: str
    MESSAGE_PATTERN: re.Pattern
    BLOCK_PATTERN: re.Pattern

    @classmethod
    def parse_to_dict(cls, string: str) -> dict[str, str]:
        parsed_locale_data = {}

        messages = list(cls.MESSAGE_PATTERN.finditer(string))

        for message in messages:
            string = string.replace(message.group("message"), "")
            name = message.group("name")
            logger.debug(
                "Found message with name={} content={}",
                name,
                message.group("data"),
            )
            parsed_locale_data[name] = message.group("data")

        blocks = list(cls.BLOCK_PATTERN.finditer(string))

        for block in blocks:
            name = block.group("name")
            data = cls._clean_block_indentation(block.group("data")).strip()
            logger.debug("Found block with name={} content=\n{}", name, data)
            parsed_locale_data[name] = data

        return parsed_locale_data

    @classmethod
    def _clean_block_indentation(cls, block_data: str) -> str:
        lines = block_data.splitlines()
        cleaned_lines = []

        for line in lines:
            if line.startswith(cls.TAB):
                cleaned_lines.append(line[len(cls.TAB):])
            elif not line.strip():
                cleaned_lines.append(line)
            else:
                cleaned_lines.append(line)

        logger.debug("Cleaned lines:\n{}", cleaned_lines)
        return cls.JOINER.join(cleaned_lines)
