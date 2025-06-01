import re


class LangrinderBaseParser:
    TAB: str
    JOINER: str
    MESSAGE_PATTERN: re.Pattern

    @classmethod
    def parse_to_dict(cls, string: str) -> dict[str, str]:
        parsed_locale_data = {}

        matches = list(cls.MESSAGE_PATTERN.finditer(string))

        for match in matches:
            name = match.group("name")

            if match.group("inline_data") is not None:
                data = match.group("inline_data").strip()
            elif match.group("block_data") is not None:
                data = cls._clean_block_indentation(match.group("block_data"))
            else:
                data = ""

            parsed_locale_data[name] = data

        return parsed_locale_data

    @classmethod
    def _clean_block_indentation(cls, block_data: str) -> str:
        cleaned_lines = []
        for line in block_data.splitlines():
            if line.startswith(cls.TAB):
                cleaned_lines.append(line[len(cls.TAB):])
            else:
                cleaned_lines.append(line)

        return cls.JOINER.join(cleaned_lines).strip()
