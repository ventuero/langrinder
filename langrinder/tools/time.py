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
        delta_abs = abs(delta)
        parts = []
        days = delta_abs.days
        hours, remainder = divmod(delta_abs.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        if days > 0:
            parts.append(("day", days))
        if hours > 0:
            parts.append(("hour", hours))
        if minutes > 0 and granularity in ("minute", "second"):
            parts.append(("minute", minutes))
        if seconds > 0 and granularity == "second":
            parts.append(("second", seconds))

        if not parts:
            return format_timedelta(
                delta_abs,
                granularity=granularity,
                add_direction=add_direction,
                format=fmt,
                locale=self.locale,
            )

        formatted_parts = [
            format_timedelta(
                timedelta(**{unit + "s": value}),
                granularity=unit,
                format=fmt,
                locale=self.locale,
            )
            for unit, value in parts
        ]

        formatted_delta = ", ".join(formatted_parts)

        if add_direction:
            base_delta_str = format_timedelta(
                delta,
                granularity=granularity,
                format=fmt,
                locale=self.locale,
            )
            base_direction_str = format_timedelta(
                delta,
                granularity=granularity,
                add_direction=True,
                format=fmt,
                locale=self.locale,
            )
            return base_direction_str.replace(base_delta_str, formatted_delta)

        return formatted_delta

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
