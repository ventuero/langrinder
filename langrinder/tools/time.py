import os
from collections import defaultdict
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

        total_seconds = int(delta_abs.total_seconds())
        unit_values = defaultdict(int)

        if granularity in ("day", "hour", "minute", "second"):
            unit_values["day"], rem = divmod(total_seconds, 86400)
        else:
            rem = total_seconds

        if granularity in ("hour", "minute", "second"):
            unit_values["hour"], rem = divmod(rem, 3600)
        if granularity in ("minute", "second"):
            unit_values["minute"], rem = divmod(rem, 60)
        if granularity == "second":
            unit_values["second"] = rem

        parts = [
            (unit, value)
            for unit, value in unit_values.items()
            if value > 0
        ]

        if not parts:
            return format_timedelta(
                delta_abs,
                granularity=granularity,
                add_direction=add_direction,
                format=fmt,
                locale=self.locale,
            )

        formatted = ", ".join(
            format_timedelta(
                timedelta(**{unit + "s": value}),
                granularity=unit,
                format=fmt,
                locale=self.locale,
            )
            for unit, value in parts
        )

        if add_direction:
            base_delta_str = format_timedelta(
                delta,
                granularity=granularity,
                format=fmt,
                locale=self.locale,
            )
            base_with_direction = format_timedelta(
                delta,
                granularity=granularity,
                add_direction=True,
                format=fmt,
                locale=self.locale,
            )
            return base_with_direction.replace(base_delta_str, formatted)

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
