"""Shared utilities for component tests."""

from __future__ import annotations

from datetime import timezone

from hightime import datetime as ht_datetime
from nitypes.time.typing import AnyDateTime


def _is_timestamp_close_to_now(timestamp: AnyDateTime, tolerance_seconds: float = 1.0) -> bool:
    current_time = ht_datetime.now(timezone.utc)
    time_diff = abs((timestamp - current_time).total_seconds())
    return time_diff <= tolerance_seconds
