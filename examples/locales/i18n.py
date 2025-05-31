import logging
import time

from langrinder.config import config
from langrinder.generator import TextResult
from langrinder.nodes import UserLanguageCode
from langrinder.tools.formatting import HTML
from mako.template import Template
from telegrinder.node import UserSource, scalar_node

logger = logging.getLogger("langrinder.compilation")
cache = {}


@scalar_node()
class BaseTranslation:
    pack: dict[str, dict[str, str]]

    def __init__(
            self,
            locale: str | None = None,
            user: UserSource | None = None,
    ):
        self.locale = locale if locale else config.default_locale
        self.user = user

    def var(self, key: str, this) -> str:
        start = time.perf_counter()
        if cached_tmp := cache.get(key):
            logger.debug(
                "'%s' of '%s' already cached. Loading",
                key, self.locale,
            )
            tmp = cached_tmp
        else:
            tmp = Template(self.pack[self.locale][key])  # noqa: S702
            cache[key] = tmp
        end = time.perf_counter()
        logger.debug("Compiled in %f s", end - start)
        return TextResult(
            tmp,
            {
                "F": HTML(user=self.user),
                "this": this,
            },
        )

    @classmethod
    def compose(cls, locale: UserLanguageCode, user: UserSource):
        return cls(locale=locale, user=user)


class Translation(BaseTranslation):
    pack = {   'en': {   'help': '${F.bold(f"Meow, {F.mention()}!")}\n'
                      'Here we are testing Langrinder',
              'nested_start': 'Here is start message: ${this.start()}',
              'start': 'Hi, i am bot from ${F.link(F.bold("Langrinder"), '
                       '"github.com/tirch/langrinder")} example!'},
    'ru': {   'help': '${F.bold(f"Мяу, {F.mention()}!")}\n'
                      'Здесь мы тестируем Langrinder',
              'nested_start': 'Вот стартовое сообщение: ${this.start()}',
              'start': 'Привет, я бот из примера '
                       '${F.link(F.bold("Langrinder"), '
                       '"github.com/tirch/langrinder")}!'}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, name: str):
        return self.var(name, this=self)
