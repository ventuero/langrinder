from telegrinder import ABCMiddleware, Context
from telegrinder.node import UserSource

from langrinder.exc import LocaleNotFoundError
from langrinder.impl import Langrinder
from langrinder.manager import LocaleManager


class ConstI18nMiddleware(ABCMiddleware):
    def __init__(self, lgr: Langrinder, locale: str, alias: str = "i18n"):
        self.mng = LocaleManager(lgr=lgr, locale=locale)
        self.alias = alias
    async def pre(self, ctx: Context):
        ctx.set(self.alias, self.mng)
        return True


class UserLanguageI18nMiddleware(ABCMiddleware):
    def __init__(self, lgr: Langrinder, alias: str = "i18n"):
        self.alias = alias
        self.lgr = lgr
    async def pre(self, ctx: Context, user: UserSource):
        language = user.language_code.unwrap_err()
        if language not in self.lgr.content:
            raise LocaleNotFoundError(language)
        mng = LocaleManager(lgr=self.lgr, locale=language)
        ctx.set(self.alias, mng)
        return True
