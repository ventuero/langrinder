class LocaleNotFoundError(BaseException):
    def __init__(self, locale: str):
        super().__init__(f"Locale {locale!r} not found!")
