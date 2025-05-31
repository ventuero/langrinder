from pathlib import Path
from pprint import pformat

from mako.template import Template

from langrinder.config import config
from langrinder.parser import LangrinderSyntaxParser


class LangrinderTranslationsGenerator:
    parser = LangrinderSyntaxParser()

    @staticmethod
    def generate_import(path: str | None):
        if not path:
            return None, None
        splited = path.split(".")
        node_class = splited.pop()
        return f"from {'.'.join(splited)} import {node_class}", node_class

    @classmethod
    def generate_node(cls):
        with Path(
            config.base_node_template,
        ).open("r", encoding="utf-8") as file:
            tmp = Template(file.read())

        node_import, node_class = cls.generate_import(config.node)
        return tmp.render(
            custom_node=node_import,
            custom_node_name=node_class,
        )

    @staticmethod
    def generate_translation(tr_pack: dict):
        with Path(
            config.base_translation_template,
        ).open("r", encoding="utf-8") as file:
            tmp = Template(file.read())

        return tmp.render(
            translation_name=config.translation_name,
            pack=tr_pack,
        )

    @classmethod
    def generate(cls):
        node_result = cls.generate_node()
        pack = {}
        for file_path in Path(config.locales_path).iterdir():
            if file_path.is_file() and file_path.suffix == ".mako":
                locale_name = file_path.stem
                with file_path.open("r", encoding="utf-8") as f:
                    file_content = f.read()
                    parsed_data_for_locale = cls.parser.parse_to_dict(
                        file_content,
                    )
                    pack[locale_name] = parsed_data_for_locale

        translation_result = cls.generate_translation(
            pformat(pack, indent=4),
        )

        with Path(config.output).open(mode="w", encoding="utf-8") as out:
            out.write(node_result + translation_result)
