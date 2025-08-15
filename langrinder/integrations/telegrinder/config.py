from dataclasses import dataclass

from telegrinder.node import DataNode, GlobalNode, IsNode

from langrinder import Langrinder


@dataclass
class I18nConfig(GlobalNode, DataNode):
    i18n: Langrinder
    source: IsNode
    default_locale: str = "en"
