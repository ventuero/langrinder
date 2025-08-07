from telegrinder import ABCMiddleware, Context
from telegrinder.node import UserSource

from langrinder.exceptions import LocaleNotFoundError
from langrinder.main import Langrinder
from langrinder.manager import LocaleManager


class ConstI18nMiddleware(ABCMiddleware):
    def __init__(self, i18n: Langrinder, locale: str, alias: str = "i18n"):
        self.mng = LocaleManager(i18n=i18n, locale=locale)
        self.alias = alias
    async def pre(self, ctx: Context):
        ctx.set(self.alias, self.mng)
        return True


class UserLanguageI18nMiddleware(ABCMiddleware):
    def __init__(
        self,
        i18n: Langrinder,
        alias: str = "i18n",
        default_locale: str = "en",
    ):
        self.alias = alias
        self.i18n = i18n
        self.default_locale = default_locale

    async def pre(self, ctx: Context, user: UserSource):
        language: str = user.language_code.unwrap_or(self.default_locale)
        if language not in self.i18n.content:
            raise LocaleNotFoundError(language)
        mng = LocaleManager(i18n=self.i18n, locale=language)
        ctx.set(self.alias, mng)
        return True
