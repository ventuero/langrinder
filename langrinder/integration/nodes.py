from telegrinder.node import ComposeError, scalar_node
from telegrinder.tools.global_context import GlobalContext

ctx = GlobalContext("langrinder")
__all__ = ("ConstLanguageCode",)


@scalar_node()
class ConstLanguageCode:
    @classmethod
    def compose(cls):
        return ctx.get("locale").unwrap_or_other(
            ComposeError("No locale specified"),
        ).value
