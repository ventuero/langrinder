import logging

from langrinder.integration.pendulum import now
from langrinder.tools import Gender
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
ctx["locale"] = "ru"
ctx["args"] = {
    "meow": "purr",
}
ctx["tz"] = "Asia/Tokyo"
api.default_params["parse_mode"] = HTMLFormatter.PARSE_MODE


@bot.on.message(StartCommand())
async def start_cmd(m: Message, tr: Translation):
    await m.answer(tr.start())


@bot.on.message(Command("help"))
async def help_cmd(m: Message, tr: Translation):
    await m.answer(tr.help())


@bot.on.message(Command("nested"))
async def nested_start_cmd(m: Message, tr: Translation):
    """Nested values (this.N()) example
    """
    await m.answer(tr.nested_start())


@bot.on.message(
    Command(
        "friends",
        Argument("fr_arg", [int]),
    ),
)
async def friends_cmd(m: Message, fr_arg: int, tr: Translation):
    """Plural forms example
    `/friends 5`
    """
    await m.answer(tr.friends(fr_arg=fr_arg))


def gender_validator(value: str):
    if value == Gender.MALE:
        return Gender.MALE
    if value == Gender.FEMALE:
        return Gender.FEMALE
    if value in [Gender.OTHER, "neutral"]:
        return Gender.OTHER
    return None


@bot.on.message(
    Command(
        "iam",
        Argument("gender_arg", [gender_validator]),
    ),
)
async def iam_cmd(m: Message, gender_arg: Gender, tr: Translation):
    """_Example with gender
    `/iam male | female | other | neutral`
    """
    await m.answer(tr.iam(gender=gender_arg))


@bot.on.message(Command("meow"))
async def meow_cmd(m: Message, tr: Translation):
    """Additional args from context example
    """
    await m.answer(tr.meow())


@bot.on.message(Command("now"))
async def now_cmd(m: Message, tr: Translation):
    """Pendulum integration example
    """
    current = now()
    start = now().start_of("day")
    await m.answer(tr.nowtime(now=current - start))


bot.run_forever(skip_updates=True)
