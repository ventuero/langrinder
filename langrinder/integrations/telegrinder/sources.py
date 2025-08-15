from telegrinder.node import UserSource, scalar_node

from .config import I18nConfig


@scalar_node
class DefaultLocaleSource:
    @classmethod
    def compose(cls, config: I18nConfig) -> str:
        return config.default_locale


@scalar_node
class UserLocaleSource:
    @classmethod
    def compose(cls, config: I18nConfig, user: UserSource) -> str:
        return user.language_code.unwrap_or(config.default_locale)
