from babel.core import Locale
from babel.plural import PluralRule


class Pluralizer:
    def __init__(self, locale_code: str):
        locale = Locale.parse(locale_code)
        self.rule = PluralRule(locale.plural_form.rules)

    def plural(self, n: int, *forms: str):
        tag = self.rule(n)
        tag2idx = {"one": 0, "few": 1, "many": 2, "other": 2}
        idx = tag2idx.get(tag, 2)
        if idx >= len(forms):
            idx = len(forms) - 1
        return forms[idx]
