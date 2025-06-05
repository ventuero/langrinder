import logging
import time

from langrinder.generator import TextResult
from langrinder.integration.telegrinder.nodes import ConstLanguageCode
from langrinder.tools import PluralGenerator
from langrinder.tools.formatting import HTML
from mako.template import Template
from telegrinder.node import UserSource, scalar_node
from telegrinder.tools.global_context import GlobalContext, GlobalCtxVar
from langrinder.tools import PluralGenerator
from langrinder.integration.pendulum import PendulumWrapper

logger = logging.getLogger("langrinder.compilation")
cache = {}
ctx = GlobalContext("langrinder")


@scalar_node()
class BaseTranslation:
    pack: dict[str, dict[str, str]]

    def __init__(
            self,
            locale: str | None = None,
            user: UserSource | None = None,
    ):
        self.locale = (
            locale
            if locale
            else ctx.get("locale").unwrap().value
        )
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
        plural = (
            ctx
            .get("plural_generator")
            .unwrap_or(
                GlobalCtxVar(PluralGenerator, name="plural_generator"),
            )
            .value(locale=self.locale)
        )
        # skipped pendulum integration
        return TextResult(
            tmp,
            {
                "F": HTML(user=self.user),
                "this": this,
                "plural": plural.plural,
                # skipped pendulum integration
                **ctx.get("args").unwrap_or(GlobalCtxVar({}, name="args")).value,
            },
        )

    @classmethod
    def compose(cls, locale: ConstLanguageCode, user: UserSource):
        return cls(locale=locale, user=user)


class Translation(BaseTranslation):
    pack = {
        "en": {
            "nested_start": "Here is start message: ${this.start()}",
            "friends": "I have ${fr_arg} ${plural(fr_arg, \"friend\", \"friends\")}",
            "iam": "You are ${gender(\"male\", \"female\", \"oak?\")}",
            "meow": "${meow}",
            "nowtime": "Now ${time.in_words(now, seconds=False)}",
            "start": "Hi, i am bot from ${F.link(F.bold(\"Langrinder\"), \"github.com/tirch/langrinder\")} example!",
            "help": "${F.bold(f\"Meow, {F.mention()}!\")}\nHere we are testing Langrinder"
        },
        "ru": {
            "nested_start": "Вот стартовое сообщение: ${this.start()}",
            "friends": "У меня есть ${fr_arg} ${plural(fr_arg, \"друг\", \"друга\", \"друзей\")}",
            "iam": "Ты ${gender(\"мальчик\", \"девочка\", \"дуб?\")}",
            "meow": "${meow}",
            "nowtime": "Сейчас ${time.in_words(now, seconds=False)}",
            "start": "Привет, я бот из примера ${F.link(F.bold(\"Langrinder\"), \"github.com/tirch/langrinder\")}!",
            "help": "${F.bold(f\"Мяу, {F.mention()}!\")}\nЗдесь мы тестируем Langrinder"
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, name: str):
        return self.var(name, this=self)
