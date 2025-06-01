from telegrinder.node import ComposeError, Source, scalar_node
from telegrinder.tools.global_context import GlobalContext

ctx = GlobalContext("langrinder")
__all__ = ("ConstLanguageCode", "UserLanguageCode")


@scalar_node()
class ConstLanguageCode:
    @classmethod
    def compose(cls):
        return ctx.get("locale").expect(
            ComposeError("No locale specified"),
        ).value


@scalar_node()
class UserLanguageCode:
    @classmethod
    def compose(cls, src: Source):
        return src.from_user.language_code.unwrap_or("en")
