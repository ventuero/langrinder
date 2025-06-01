import inspect
from abc import ABCMeta
from pathlib import Path
from pprint import pformat

from loguru import _logger
from mako.template import Template

from langrinder.parser import LangrinderSyntaxParser


class LangrinderTranslationsGenerator:
    def __init__(
            self,
            node_path: str,
            translation_path: str,
            translation_name: str,
            node: ABCMeta,
            logger: _logger.Logger | None = None,
    ):
        self.parser = LangrinderSyntaxParser()
        self.node_path = node_path
        self.tr_path = translation_path
        self.tr_name = translation_name
        self.node = node
        self.logger = logger

    def generate_import(self, obj):
        module_name = inspect.getmodule(obj).__name__
        class_name = obj.__name__

        if module_name == "builtins":
            return None, None

        result = (f"from {module_name} import {class_name}", class_name)
        if self.logger:
            self.logger.debug("Node import: '{}'", result[0])
        return result

    def generate_node(self):
        with Path(
            self.node_path,
        ).open("r", encoding="utf-8") as file:
            tmp = Template(file.read())

        node_import, node_class = self.generate_import(self.node)
        if self.logger:
            self.logger.debug("Rendering node")
        return tmp.render(
            custom_node=node_import,
            custom_node_name=node_class,
        )

    def generate_translation(self, tr_pack: dict):
        with Path(
            self.tr_path,
        ).open("r", encoding="utf-8") as file:
            tmp = Template(file.read())

        if self.logger:
            self.logger.debug("Rendering translation")
        return tmp.render(
            translation_name=self.tr_name,
            pack=tr_pack,
        )

    def generate(self, output_file: str, input_dir: str):
        node_result = self.generate_node()
        pack = {}
        for file_path in Path(input_dir).iterdir():
            if file_path.is_file() and file_path.suffix == ".mako":
                locale_name = file_path.stem
                with file_path.open("r", encoding="utf-8") as f:
                    file_content = f.read()
                    if self.logger:
                        self.logger.debug("Rendering '{}'", locale_name)
                    parsed_data_for_locale = self.parser.parse_to_dict(
                        file_content,
                    )
                    pack[locale_name] = parsed_data_for_locale

        translation_result = self.generate_translation(
            pformat(pack, indent=4),
        )

        with Path(output_file).open(mode="w", encoding="utf-8") as out:
            if self.logger:
                self.logger.debug("Writing '{}'", output_file)
            out.write(node_result + translation_result)
