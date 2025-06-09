from mako.template import Template

from langrinder.impl import Langrinder
from langrinder.tools import HTMLFormatter, Pluralizer
from langrinder.types import TextResult


class LocaleManager:
    def __init__(self, lgr: Langrinder, locale: str):
        self.pack: dict = lgr.content[locale]
        self.lgr = lgr

        self.DEFAULT_ARGS = {
            "html": HTMLFormatter,
            "plural": Pluralizer(locale).plural,
            "this": self,
        }

    def __getattr__(self, item: str):
        if self.lgr.raise_val_error and not self.pack.get(item):
            raise ValueError(item)
        tmp = Template(self.pack.get(item, item))
        merged_args = {**self.lgr.args, **self.DEFAULT_ARGS}
        return TextResult(tmp, merged_args)
