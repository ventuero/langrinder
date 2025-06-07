from pathlib import Path
from typing import Any

from .tools import HTMLFormatter, Pluralizer, TimeFormatter, import_class

DEFAULT_COMPILER = "langrinder.JSONCompiler"


class Langrinder:
    def __init__(
            self,
            compiled_file: Path | str,
            compiler: str = DEFAULT_COMPILER,
            args: dict[str, Any] | None = None,
            tz: str | None = None,
            raise_value_error: bool = True,
    ):
        """
        Main class of Langrinder.

        :param compiled_file: File to load translation
        :param compiler: Compiler to load translation
        :param args: Global args for locales
        :param tz: Timezone for `TimeFormatter`
        :param raise_value_error: Raise value error if locale not found
        """
        file = (
            compiled_file
            if isinstance(compiled_file, Path)
            else Path(compiled_file)
        )
        compiler = import_class(compiler)
        self.args = args if args else {}
        file_content = self.read(file)
        self.content: dict = compiler.load(file_content)
        self.tz = tz
        self.raise_val_error = raise_value_error

    @staticmethod
    def read(file: Path) -> str:
        with file.open("r", encoding="utf-8") as f:
            return f.read()

    def locale(self, loc: str):
        from .manager.mng import LocaleManager
        return LocaleManager(lgr=self, locale=loc)
