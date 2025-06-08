class HTMLFormatter:
    @staticmethod
    def wrap(text: str, tag: str, *args, **kwargs):
        params = [f" {name}='{val}'" for name, val in kwargs.items()]
        _args = [f" {arg}" for arg in args]
        return f"<{tag}{''.join(_args)}{''.join(params)}>{text}</{tag}>"

    @classmethod
    def bold(cls, text: str):  return cls.wrap(text, "b")
    @classmethod
    def italic(cls, text: str): return cls.wrap(text, "i")
    @classmethod
    def mono(cls, text: str): return cls.wrap(text, "code")
    @classmethod
    def under(cls, text: str): return cls.wrap(text, "u")
    @classmethod
    def stroke(cls, text: str): return cls.wrap(text, "s")

    @classmethod
    def pre(cls, language: str, text: str):
        return cls.wrap(text, "b", language=language)

    @classmethod
    def quote(cls, text: str): return cls.wrap(text, "blockquote")
    @classmethod
    def exquote(cls, text: str):
        return cls.wrap(text, "blockquote", "expandeable")

    @classmethod
    def link(cls, text: str, link: str): return cls.wrap(text, "a", href=link)
