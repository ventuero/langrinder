import importlib.resources
import logging

from telegrinder.node import Node

from langrinder.generator import (
    LangrinderBaseGenerator,
    LangrinderTranslationsGenerator,
)
from langrinder.nodes import ConstLanguageCode
from langrinder.parser import LangrinderBaseParser, LangrinderSyntaxParser


class Langrinder:
    """
    Main Langrinder class.
    """
    LANGRINDER_PATH = importlib.resources.files("langrinder")

    def __init__(
            self,
            generator: type[LangrinderBaseGenerator]
                = LangrinderTranslationsGenerator,
            parser: type[LangrinderBaseParser] = LangrinderSyntaxParser,
            node_template: str = (
                f"{LANGRINDER_PATH}/generator/templates/node.mako"
            ),
            translation_template: str = (
                f"{LANGRINDER_PATH}/generator/templates/translation.mako"
            ),
            translation_name: str = "Translation",
            node: type[Node] = ConstLanguageCode,
            logger: logging.Logger | None = None,
    ):
        self.logger = logger
        self.gen = generator(
            node_path=node_template,
            translation_path=translation_template,
            translation_name=translation_name,
            node=node,
            logger=self.logger,
        )
        self.gen.parser = parser()

    def compile(self, input_dir: str, output_file: str):
        self.gen.generate(
            output_file=output_file,
            input_dir=input_dir,
        )
        if not self.logger:
            print("Locales generated")
            return
        self.logger.info("Locales generated")
