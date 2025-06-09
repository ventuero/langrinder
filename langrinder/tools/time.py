import os
from datetime import datetime, timedelta

from babel.dates import (
    format_date,
    format_datetime,
    format_time,
    format_timedelta,
    get_timezone,
)


class TimeFormatter:
    def __init__(self, locale_code: str = "ru", tz_name: str | None = None):
        self.locale = locale_code
        self.tzinfo = get_timezone(tz_name) if tz_name else os.getenv("TZ")

    def fmt(self, dt: datetime, _format: str = "medium") -> str:
        return format_datetime(dt, format=_format, locale=self.locale)

    def now(self) -> datetime:
        return datetime.now(tz=self.tzinfo)

    def date(self, dt: datetime, fmt: str = "medium") -> str:
        return format_date(dt, format=fmt, locale=self.locale)

    def time(self, dt: datetime, fmt: str = "medium") -> str:
        return format_time(
            dt,
            format=fmt,
            tzinfo=self.tzinfo,
            locale=self.locale,
        )

    def datetime(self, dt: datetime, fmt: str = "medium") -> str:
        return format_datetime(
            dt,
            format=fmt,
            tzinfo=self.tzinfo,
            locale=self.locale,
        )

    def _format_detailed_delta(
        self,
        delta: timedelta,
        *,
        add_direction: bool = False,
        granularity: str = "second",
        fmt: str = "long",
    ) -> str:
        total_seconds = int(abs(delta).total_seconds())

        days, rem = divmod(total_seconds, 86400)
        hours, rem = divmod(rem, 3600)
        minutes, seconds = divmod(rem, 60)

        result = []
        if granularity in ("day", "hour", "minute", "second") and days:
            result.append(("day", days))
        if granularity in ("hour", "minute", "second") and hours:
            result.append(("hour", hours))
        if granularity in ("minute", "second") and minutes:
            result.append(("minute", minutes))
        if granularity == "second" and seconds:
            result.append(("second", seconds))

        if not result:
            return format_timedelta(
                abs(delta),
                granularity=granularity,
                add_direction=add_direction,
                format=fmt,
                locale=self.locale,
            )

        parts = [
            format_timedelta(
                timedelta(**{unit + "s": value}),
                granularity=unit,
                format=fmt,
                locale=self.locale,
            )
            for unit, value in result
        ]

        formatted = ", ".join(parts)

        if add_direction:
            base_text = format_timedelta(
                delta,
                granularity=granularity,
                format=fmt,
                locale=self.locale,
            )
            directed_text = format_timedelta(
                delta,
                granularity=granularity,
                format=fmt,
                add_direction=True,
                locale=self.locale,
            )
            return directed_text.replace(base_text, formatted)

        return formatted

    def ago(
        self,
        delta: timedelta,
        granularity: str = "second",
        fmt: str = "long",
    ) -> str:
        if delta.total_seconds() > 0:
            delta = -delta
        return self._format_detailed_delta(
            delta,
            add_direction=True,
            granularity=granularity,
            fmt=fmt,
        )

    def in_(
        self,
        delta: timedelta,
        granularity: str = "second",
        fmt: str = "long",
    ) -> str:
        if delta.total_seconds() < 0:
            delta = -delta
        return self._format_detailed_delta(
            delta,
            add_direction=True,
            granularity=granularity,
            fmt=fmt,
        )

    def delta(
        self,
        delta: timedelta,
        granularity: str = "second",
        fmt: str = "long",
    ) -> str:
        return self._format_detailed_delta(
            delta,
            add_direction=False,
            granularity=granularity,
            fmt=fmt,
        )
