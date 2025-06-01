import logging

from telegrinder.tools.global_context import GlobalContext, GlobalCtxVar

ctx = GlobalContext("langrinder")
logger = logging.getLogger(__name__)


class PluralGenerator:
    def __init__(
            self,
            locale: str = (
                ctx.get("locale")
                .unwrap_or(GlobalCtxVar("en", name="locale"))
                .value
            ),
    ):
        self.locale = locale
        self._PLURAL_RULES = {
            "en": lambda n: "one" if n == 1 else "other",
            "ru": lambda n: (
                "one" if n % 10 == 1 and n % 100 != 11 else
                "few" if n % 10 >= 2 and n % 10 <= 4 and (
                    n % 100 < 10 or n % 100 >= 20
                ) else
                "many" if n % 10 == 0 or n % 10 >= 5 or (
                    n % 100 >= 11 and n % 100 <= 14
                ) else
                "other"
            ),
        }

    def plural(  # noqa: PLR0911
        self,
        count: int,
        *forms: str,
    ) -> str:
        if not forms:
            logger.warning("No forms provided to plural function.")
            return ""

        rule_func = self._PLURAL_RULES.get(
            self.locale, self._PLURAL_RULES["en"],
        )
        plural_category = rule_func(count)

        num_forms = len(forms)

        if num_forms == 2:
            if plural_category == "one":
                return forms[0]
            else: # "other"
                return forms[1]
        elif num_forms >= 3:
            if plural_category == "one":
                return forms[0]
            elif plural_category == "few" and num_forms >= 3:
                return forms[1]
            elif plural_category == "many" and num_forms >= 4:
                return forms[2]
            else:
                return forms[num_forms - 1]

        logger.error(
            "Could not find plural form for count %d, locale %s, forms %r.",
            count, self.locale, forms,
        )
        return f"PLURAL_ERROR:{count}:{self.locale}"
