from telegrinder.node import UserSource


class HTML:
    def __init__(self, user: UserSource):
        self.user = user

    def bold(self, text: str):
        return f"<b>{text}</b>"

    def italic(self, text: str):
        return f"<i>{text}</i>"

    def mono(self, text: str):
        return f"<code>{text}</code>"

    def quote(self, text: str):
        return f"<blockquote>{text}</blockquote>"

    def exquote(self, text: str):
        return f"<blockquote expandeable>{text}</blockquote>"

    def link(self, text: str, url: str):
        return f"<a href='{url}'>{text}</a>"

    def mention(self, **kwargs):
        link = (
            "https://t.me/"
            f"{kwargs.get("username") or self.user.username.unwrap()}"
            if self.user.username or kwargs.get("username")
            else f"tg://user?id={kwargs.get("id") or self.user.id}"
        )
        return self.link(kwargs.get("name") or self.user.full_name, link)
