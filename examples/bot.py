import logging

from langrinder import Langrinder, LocaleManager
from langrinder.middlewares import ConstI18nMiddleware
from telegrinder import API, Message, Telegrinder, Token
from telegrinder.node import UserSource
from telegrinder.rules import StartCommand

logging.basicConfig()

api = API(Token.from_env())
bot = Telegrinder(api)
lgr = Langrinder("examples/locales/compiled.json")
bot.on.message.middlewares.extend(
    [ConstI18nMiddleware(lgr, locale="ru", alias="_")],
)


@bot.on.message(StartCommand())
async def on_start(message: Message, user: UserSource, _: LocaleManager):
    await message.answer(_.start(name=user.first_name))


bot.run_forever(skip_updates=True)
