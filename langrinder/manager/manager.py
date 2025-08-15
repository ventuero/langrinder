from mako.template import Template

from langrinder.exceptions import LocaleNotFoundError
from langrinder.main import Langrinder
from langrinder.tools import HTMLFormatter, Pluralizer


class LocaleManager:
    """Langrinder locale manager"""

    MESSAGE_NOT_FOUND = "Message '{}' not found!"

    def __init__(self, i18n: Langrinder, locale: str):
        self.pack: dict | None = i18n.content.get(locale)
        if not self.pack:
            raise LocaleNotFoundError(locale)
        self.i18n = i18n
        self.sequence = []

        self.DEFAULT_ARGS = {
            "html": HTMLFormatter,
            "plural": Pluralizer(locale).plural,
            "this": self,
        }

    def _get(self, key: str, **kwargs) -> str:
        text = self.pack.get(key, None if self.i18n.raise_val_error else key) # type: ignore
        if not text:
            raise ValueError(self.MESSAGE_NOT_FOUND.format(key))
        template = Template(text)
        return str(
            template.render(
                **self.i18n.args,
                **self.DEFAULT_ARGS,
                **kwargs,
            ),
        )

    def __getitem__(self, item: str):
        return self._get(item)

    def __getattr__(self, item: str) -> "LocaleManager":
        self.sequence.append(item)
        return self

    def __call__(self, **kwargs) -> str:
        key = self.i18n.sep.join(self.sequence)
        self.sequence = []
        return self._get(key, **kwargs)

    def get_manager(self, loc: str) -> "LocaleManager":
        return LocaleManager(i18n=self.i18n, locale=loc)
