from __future__ import annotations

import ctypes
import functools
from datetime import timezone
from datetime import datetime as std_datetime
from hightime import datetime as ht_datetime
from typing import Optional, Union


@functools.total_ordering
class AbsoluteTime(ctypes.Structure):
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

    @classmethod
    def from_datetime(cls, dt: Union[std_datetime, ht_datetime]) -> AbsoluteTime:
        utc_dt = dt.astimezone(tz=timezone.utc)

        # First, calculate whole seconds by converting from the 1970 to 1904 epoch.
        timestamp_1970_epoch = utc_dt.timestamp()
        was_negative = timestamp_1970_epoch < 0
        timestamp_1904_epoch = int(timestamp_1970_epoch + AbsoluteTime._BIAS_FROM_1970_EPOCH)

        # Our bias is positive, so our sign should only change if we were previously negative.
        is_negative = timestamp_1904_epoch < 0
        if is_negative != was_negative and not was_negative:
            raise OverflowError(f"Can't represent {dt.isoformat()} in AbsoluteTime (1904 epoch)")

        # Finally, convert the subseconds.
        if isinstance(dt, ht_datetime):
            total_yoctoseconds = dt.yoctosecond
            total_yoctoseconds += dt.femtosecond * AbsoluteTime._YS_PER_FS
            total_yoctoseconds += dt.microsecond * AbsoluteTime._YS_PER_US
            lsb = int(
                round(AbsoluteTime._NUM_SUBSECONDS * total_yoctoseconds / AbsoluteTime._YS_PER_S)
            )
        else:
            lsb = int(
                round(AbsoluteTime._NUM_SUBSECONDS * utc_dt.microsecond / AbsoluteTime._US_PER_S)
            )

        return AbsoluteTime(lsb=lsb, msb=timestamp_1904_epoch)

    def to_datetime(self, tzinfo: Optional[timezone] = None) -> ht_datetime:
        # First, calculate whole seconds by converting from the 1904 to 1970 epoch.
        timestamp_1904_epoch = self.msb
        was_positive = timestamp_1904_epoch > 0
        timestamp_1970_epoch = int(timestamp_1904_epoch - AbsoluteTime._BIAS_FROM_1970_EPOCH)

        # Our bias is negative, so our sign should only change if we were previously positive.
        is_positive = timestamp_1970_epoch > 0
        if is_positive != was_positive and not was_positive:
            raise OverflowError(f"Can't represent {str(self)} in datetime (1970 epoch)")

        # Finally, convert the subseconds to micro, femto, and yoctoseconds.
        total_yoctoseconds = int(
            round(AbsoluteTime._YS_PER_S * self.lsb / AbsoluteTime._NUM_SUBSECONDS)
        )
        microsecond, remainder_yoctoseconds = divmod(total_yoctoseconds, AbsoluteTime._YS_PER_US)
        femtosecond, remainder_yoctoseconds = divmod(
            remainder_yoctoseconds, AbsoluteTime._YS_PER_FS
        )
        yoctosecond = remainder_yoctoseconds

        # Start with UTC
        dt = ht_datetime.fromtimestamp(timestamp_1970_epoch, timezone.utc)
        # Add in precision
        dt = dt.replace(microsecond=microsecond, femtosecond=femtosecond, yoctosecond=yoctosecond)
        # Then convert to requested timezone
        return dt.astimezone(tz=tzinfo)

    def __str__(self) -> str:
        return f"AbsoluteTime(lsb=0x{self.lsb:x}, msb=0x{self.msb:x})"

    def __eq__(self, other) -> bool:
        return self.msb == other.msb and self.lsb == other.lsb

    def __lt__(self, other) -> bool:
        if self.msb == other.msb:
            return self.lsb < other.lsb
        else:
            return self.msb < other.msb
