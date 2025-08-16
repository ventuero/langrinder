from telegrinder import ABCRule
from telegrinder.node import Text

from langrinder.node import Translator


class EqualsTo(ABCRule):
    """
    Checks if the text matches the value for a key from i18n
    """
    def __init__(self, key: str, ignore_case: bool = False) -> None:
        self.key = key
        self.i = ignore_case

    def check(self, text: Text, _: Translator) -> bool:
        _text = text.lower() if self.i else text
        message = _[self.key].lower() if self.i else _[self.key]
        return _text == message
