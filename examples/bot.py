import logging
import random

from langrinder import Langrinder
from langrinder.node import DefaultLocaleSource, I18nConfig, Translator
from telegrinder import API, Message, Telegrinder, Token
from telegrinder.modules import setup_logger
from telegrinder.node import UserSource, as_node
from telegrinder.rules import Argument, Command, StartCommand

logging.basicConfig()
setup_logger()

api = API(Token.from_env())
bot = Telegrinder(api)

locales = ["en", "ru"]
i18n = Langrinder("examples/locales/compiled.json")
config = I18nConfig(
    i18n=i18n,
    source=as_node(DefaultLocaleSource),
    default_locale=random.choice(locales), # noqa: S311
)
I18nConfig.set(config)


@bot.on.message(StartCommand())
async def on_start(message: Message, user: UserSource, _: Translator):
    await message.answer(_.start(name=user.first_name))


@bot.on.message(Command("locale"))
async def get_current_locale(message: Message, _: Translator):
    await message.answer(_.locale())


def available_locale(value: str) -> str | bool:
    if value not in locales:
        return False
    return value

@bot.on.message(
    Command("set_locale", Argument("loc", [available_locale])),
)
async def set_locale(message: Message, _: Translator, loc: str):
    config.default_locale = loc
    I18nConfig.set(config)
    tr = _.get_manager(loc)
    await message.answer(tr.locale.changed())


bot.run_forever(skip_updates=True)
