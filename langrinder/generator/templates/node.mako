import logging
import time

from langrinder.generator import TextResult
${custom_node if custom_node else "from langrinder.nodes import ConstLanguageCode"}
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
        time_wrapper = (
            ctx
            .get("time_wrapper")
            .unwrap_or(
                GlobalCtxVar(PendulumWrapper, name="time_wrapper"),
            )
            .value(locale=self.locale)
        )
        return TextResult(
            tmp,
            {
                "F": HTML(user=self.user),
                "this": this,
                "plural": plural.plural,
                "time": time_wrapper,
                **ctx.get("args").unwrap_or({}).value,
            },
        )

    @classmethod
    def compose(cls, locale: ${custom_node_name if custom_node_name else "ConstLanguageCode"}, user: UserSource):
        return cls(locale=locale, user=user)
