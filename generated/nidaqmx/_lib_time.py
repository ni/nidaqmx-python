from __future__ import annotations

import ctypes
import functools
from datetime import datetime as std_datetime, timezone, tzinfo as dt_tzinfo

from hightime import datetime as ht_datetime, timedelta as ht_timedelta

from nidaqmx._time import _convert_to_desired_timezone


@functools.total_ordering
class AbsoluteTime(  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    ctypes.Structure
):
    # Please visit ni.com/info and enter the Info Code NI_BTF for detailed information.
    # The summary is:
    #    * lsb - positive fractions (2^-64) of a second
    #    * msb - number of whole seconds since 12am, Friday, January 1, 1904, UTC

    _pack_ = 4
    _fields_ = [("lsb", ctypes.c_uint64), ("msb", ctypes.c_int64)]

    # 66 years, 17 leap days = 24107 days = 2082844800 seconds
    _BIAS_FROM_1970_EPOCH = 2082844800
    _NUM_SUBSECONDS = 2**64
    _US_PER_S = 10**6
    _YS_PER_S = 10**24
    _YS_PER_US = 10**18
    _YS_PER_FS = 10**9

    MAX_FS = 10**9
    MAX_YS = 10**9

    _EPOCH_1904 = ht_datetime(1904, 1, 1, tzinfo=timezone.utc)

    @classmethod
    def from_datetime(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        cls, dt: std_datetime | ht_datetime
    ) -> AbsoluteTime:
        seconds_since_1904 = 0

        # Convert the subseconds.
        if isinstance(dt, ht_datetime):
            seconds_since_1904 = int((dt - AbsoluteTime._EPOCH_1904).precision_total_seconds())
            total_yoctoseconds = dt.yoctosecond
            total_yoctoseconds += dt.femtosecond * AbsoluteTime._YS_PER_FS
            total_yoctoseconds += dt.microsecond * AbsoluteTime._YS_PER_US
            lsb = int(
                round(AbsoluteTime._NUM_SUBSECONDS * total_yoctoseconds / AbsoluteTime._YS_PER_S)
            )
        else:
            seconds_since_1904 = int((dt - AbsoluteTime._EPOCH_1904).total_seconds())
            lsb = int(round(AbsoluteTime._NUM_SUBSECONDS * dt.microsecond / AbsoluteTime._US_PER_S))

        return AbsoluteTime(lsb=lsb, msb=seconds_since_1904)

    def to_datetime(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self, tzinfo: dt_tzinfo | None = None
    ) -> ht_datetime:
        total_yoctoseconds = int(
            round(AbsoluteTime._YS_PER_S * self.lsb / AbsoluteTime._NUM_SUBSECONDS)
        )
        dt = (
            AbsoluteTime._EPOCH_1904
            + ht_timedelta(seconds=self.msb)
            + ht_timedelta(yoctoseconds=total_yoctoseconds)
        )
        return _convert_to_desired_timezone(dt, tzinfo)

    def __str__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self,
    ) -> str:
        return f"AbsoluteTime(lsb=0x{self.lsb:x}, msb=0x{self.msb:x})"

    def __eq__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, other
    ) -> bool:
        return self.msb == other.msb and self.lsb == other.lsb

    def __lt__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, other
    ) -> bool:
        if self.msb == other.msb:
            return self.lsb < other.lsb
        else:
            return self.msb < other.msb
