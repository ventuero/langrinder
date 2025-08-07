from pathlib import Path
from typing import Any

from .compiler.abc import ABCCompiler
from .tools import import_class

DEFAULT_COMPILER = "langrinder.JSONCompiler"


class Langrinder:
    """Main class of Langrinder"""

    NO_CONTENT = "No content for i18n!"

    def __init__(
            self,
            compiled_file: Path | str,
            compiler: str = DEFAULT_COMPILER,
            args: dict[str, Any] | None = None,
            raise_value_error: bool = True,
            key_separator: str = "-",
    ):
        """
        Main class of Langrinder

        :param compiled_file: File to load translation
        :param compiler: Compiler to load translation
        :param args: Global args for locales
        :param raise_value_error: Raise value error if locale not found
        :param key_separator: Separator for building keys
        """
        file = (
            compiled_file
            if isinstance(compiled_file, Path)
            else Path(compiled_file)
        )
        _compiler: type[ABCCompiler] = import_class(compiler)
        self.args = args if args else {}
        file_content = self.read(file)
        self.content: dict = _compiler.load(file_content)
        if not self.content:
            raise ValueError(self.NO_CONTENT)
        self.raise_val_error = raise_value_error
        self.sep = key_separator

    @staticmethod
    def read(file: Path) -> str:
        with file.open("r", encoding="utf-8") as f:
            return f.read()

    def locale(self, loc: str):
        from .manager.manager import LocaleManager
        return LocaleManager(i18n=self, locale=loc)
