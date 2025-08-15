from telegrinder import Context
from telegrinder.node import as_node, compose_nodes, per_call, scalar_node

from .config import I18nConfig


@per_call
@scalar_node
class Translator:
    @classmethod
    async def compose(cls, ctx: Context, config: I18nConfig):
        node = await compose_nodes(
            {"src": as_node(config.source)},
            ctx,
            data={I18nConfig: config},
        )
        locale = node.unwrap().values["src"]
        return config.i18n.get_manager(locale)
