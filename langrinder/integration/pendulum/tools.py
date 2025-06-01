import pendulum
from telegrinder.tools.global_context import GlobalContext

ctx = GlobalContext("langrinder")


def now() -> pendulum.DateTime:
    tz = ctx.get("tz").unwrap_or_none()
    if tz:
        tz = tz.value
    return pendulum.now(tz=tz)
