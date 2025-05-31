import logging

from telegrinder import API, Message, Telegrinder, Token
from telegrinder.rules import Argument, Command, StartCommand
from telegrinder.tools.formatting import HTMLFormatter
from telegrinder.tools.global_context import GlobalContext

from examples.locales.i18n import Translation

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s: %(message)s",
)
logging.getLogger("telegrinder").setLevel(logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.WARNING)
logging.getLogger("langrinder").setLevel(logging.DEBUG)

api = API(Token.from_env())
bot = Telegrinder(api)

ctx = GlobalContext("langrinder")
ctx["locale"] = "en"
api.default_params["parse_mode"] = HTMLFormatter.PARSE_MODE


@bot.on.message(StartCommand())
async def start_cmd(m: Message, tr: Translation):
    await m.answer(tr.start())


@bot.on.message(Command("help"))
async def help_cmd(m: Message, tr: Translation):
    await m.answer(tr.help())


@bot.on.message(Command("nested"))
async def nested_start_cmd(m: Message, tr: Translation):
    await m.answer(tr.nested_start())


@bot.on.message(
    Command(
        "friends",
        Argument("fr_arg", [int]),
    ),
)
async def friends_cmd(m: Message, fr_arg: int, tr: Translation):
    await m.answer(tr.friends(fr_arg=fr_arg))


bot.run_forever(skip_updates=True)
