import inspect
from abc import ABCMeta
from pathlib import Path

from loguru import _logger
from mako.template import Template

from langrinder.parser import LangrinderSyntaxParser
from langrinder.tools.json import dump_to_pack


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
        self.ignore = ["__pycache__"]

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
        try:
            import pendulum
            use_pendulum = True
        except ImportError:
            use_pendulum = False
        return tmp.render(
            custom_node=node_import,
            custom_node_name=node_class,
            use_pendulum=use_pendulum,
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

    def _parse_locale_directory(self, locale_dir: Path) -> dict:
        merged_data = {}

        for file_path in locale_dir.rglob("*.mako"):
            if self.logger:
                self.logger.debug("Processing file: '{}'", file_path)

            with file_path.open("r", encoding="utf-8") as f:
                file_content = f.read()
                parsed_data = self.parser.parse_to_dict(file_content)
                merged_data.update(parsed_data)

        return merged_data

    def generate(self, output_file: str, input_dir: str):
        node_result = self.generate_node()
        pack = {}

        input_path = Path(input_dir)

        for locale_dir in input_path.iterdir():
            if locale_dir.is_dir():
                locale_name = locale_dir.name
                if locale_name in self.ignore:
                    continue
                if self.logger:
                    self.logger.info("Processing locale: '{}'", locale_name)

                locale_data = self._parse_locale_directory(locale_dir)

                if locale_data:
                    pack[locale_name] = locale_data

        translation_result = self.generate_translation(
            dump_to_pack(pack),
        )

        with Path(output_file).open(mode="w", encoding="utf-8") as out:
            if self.logger:
                self.logger.debug("Writing '{}'", output_file)
            out.write(node_result + translation_result)
