from datetime import datetime, timedelta

import pendulum
from telegrinder.tools.global_context import GlobalContext, GlobalCtxVar

ctx = GlobalContext("langrinder")


class PendulumWrapper:
    def __init__(
            self,
            locale: str = (
                ctx.get("locale")
                .unwrap_or(GlobalCtxVar("en", name="locale"))
            ),
    ):
        tz = ctx.get("tz").unwrap_or_none()
        if tz:
            tz = tz.value
        self._locale = locale
        self._tz = tz
        self.TYPERROR_DATETIME = (
            "Expected 'datetime' or 'pendulum.DateTime', got '{}'"
        )
        self.TYPERROR_DURATION = (
            "Expected 'timedelta' or 'pendulum.Duration', got '{}'"
        )

    def _ensure_datetime(
            self,
            dt: datetime | pendulum.DateTime,
    ) -> pendulum.DateTime:
        if isinstance(dt, datetime):
            return pendulum.instance(dt, tz=self._tz)
        if isinstance(dt, pendulum.DateTime):
            if (
                self._tz
                and dt.tzinfo.tzname(dt) != (
                    pendulum.timezone(self._tz).tzname(pendulum.now(self._tz))
                )
            ):
                return dt.in_timezone(self._tz)
            return dt
        raise TypeError(self.TYPERROR_DATETIME.format(type(dt)))

    def _ensure_duration(
            self,
            delta: timedelta | pendulum.Duration,
    ) -> pendulum.Duration:
        if isinstance(delta, timedelta):
            return pendulum.duration(seconds=delta.total_seconds())
        if isinstance(delta, pendulum.Duration):
            return delta
        raise TypeError(self.TYPERROR_DURATION.format(type(delta)))

        def diff(
            self,
            dt_or_delta: datetime | timedelta | pendulum.DateTime
                | pendulum.Duration,
            other: datetime | pendulum.DateTime | None = None,
            absolute: bool = False,
            seconds: bool = True,
        ) -> str:
            if isinstance(
                dt_or_delta,
                (timedelta, pendulum.Duration),
            ):
                p_delta = self._ensure_duration(dt_or_delta)
                if not seconds:
                    total_minutes = int(p_delta.total_seconds() / 60)
                    rounded_delta = pendulum.duration(minutes=total_minutes)
                    return rounded_delta.in_words(locale=self._locale)
                return p_delta.in_words(locale=self._locale)

            p_dt = self._ensure_datetime(dt_or_delta)
            p_other = (
                self._ensure_datetime(other)
                if other else pendulum.now(self._tz)
            )

            if not seconds:
                return p_dt.diff_for_humans(
                    other=p_other,
                    absolute=absolute,
                    locale=self._locale,
                    granularity="minute",
                )

            return p_dt.diff_for_humans(
                other=p_other, absolute=absolute, locale=self._locale,
            )
        return None

    def in_words(
            self,
            delta: timedelta | pendulum.Duration,
            seconds: bool = True,
    ) -> str:
        p_delta = self._ensure_duration(delta)
        if not seconds:
            total_minutes = int(p_delta.total_seconds() / 60)
            rounded_delta = pendulum.duration(minutes=total_minutes)
            return rounded_delta.in_words(locale=self._locale)
        return p_delta.in_words(locale=self._locale)

    def fmt(
        self, dt: datetime | pendulum.DateTime, fmt_string: str = "YYYY-MM-DD",
    ) -> str:
        p_dt = self._ensure_datetime(dt)
        return p_dt.format(fmt_string, locale=self._locale)

    def to_datetime_string(self, dt: datetime | pendulum.DateTime) -> str:
        p_dt = self._ensure_datetime(dt)
        return p_dt.to_datetime_string()

    def to_date_string(self, dt: datetime | pendulum.DateTime) -> str:
        p_dt = self._ensure_datetime(dt)
        return p_dt.to_date_string()

    def to_time_string(self, dt: datetime | pendulum.DateTime) -> str:
        p_dt = self._ensure_datetime(dt)
        return p_dt.to_time_string()
