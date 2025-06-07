import os
from datetime import datetime

from babel.dates import (
    format_date,
    format_datetime,
    format_time,
    format_timedelta,
    get_timezone,
)


class TimeFormatter:
    def __init__(self, locale_code="ru", tz_name=None):
        self.locale = locale_code
        self.tzinfo = get_timezone(tz_name) if tz_name else os.getenv("TZ")

    def now(self):
        return datetime.now(tz=self.tzinfo)

    def date(self, dt, fmt="medium"):
        return format_date(dt, format=fmt, locale=self.locale)

    def time(self, dt, fmt="medium"):
        return format_time(
            dt,
            format=fmt,
            tzinfo=self.tzinfo,
            locale=self.locale,
        )

    def datetime(self, dt, fmt="medium"):
        return format_datetime(
            dt,
            format=fmt,
            tzinfo=self.tzinfo,
            locale=self.locale,
        )

    def ago(self, delta, granularity="second", fmt="long"):
        if delta.total_seconds() > 0:
            delta = -delta
        return format_timedelta(
            delta,
            granularity=granularity,
            add_direction=True,
            format=fmt,
            locale=self.locale,
        )


    def in_(
        self,
        delta,
        granularity="second",
        fmt="long",
    ):
        if delta.total_seconds() < 0:
            delta = -delta
        return format_timedelta(
            delta,
            granularity=granularity,
            add_direction=True,
            format=fmt,
            locale=self.locale,
        )
