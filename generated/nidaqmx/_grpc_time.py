from __future__ import annotations

from datetime import timezone
from datetime import datetime as std_datetime
from datetime import tzinfo as dt_tzinfo
from hightime import datetime as ht_datetime
from hightime import timedelta as ht_timedelta
from typing import Optional, Union
from nidaqmx._time import _convert_to_desired_timezone

from google.protobuf.timestamp_pb2 import Timestamp as GrpcTimestamp

# 66 years, 17 leap days = 24107 days = 2082844800 seconds
_BIAS_FROM_1970_EPOCH = 2082844800

_NS_PER_S = 10**9
_NS_PER_US = 10**3

_YS_PER_US = 10**18
_YS_PER_NS = 10**15
_YS_PER_FS = 10**9

_EPOCH_1970 = ht_datetime(1970, 1, 1, tzinfo=timezone.utc)

def convert_time_to_timestamp(dt: std_datetime | ht_datetime, ts: GrpcTimestamp | None = None) -> GrpcTimestamp:
    seconds_since_1970 = 0

    if ts is None:
        ts = GrpcTimestamp()

    if isinstance(dt, ht_datetime):
        seconds_since_1970 = int((dt - _EPOCH_1970).precision_total_seconds())
        total_yoctoseconds = dt.yoctosecond
        total_yoctoseconds += dt.femtosecond * _YS_PER_FS
        total_yoctoseconds += dt.microsecond * _YS_PER_US
        nanos, remainder_yoctoseconds = divmod(total_yoctoseconds, _YS_PER_NS)
        # round up, if necessary
        if remainder_yoctoseconds >= _YS_PER_NS / 2:
            nanos += 1
    else:
        seconds_since_1970 = int((dt - _EPOCH_1970).total_seconds())
        nanos = dt.microsecond * _NS_PER_US

    ts.FromNanoseconds(seconds_since_1970 * _NS_PER_S + nanos)
    return ts

def convert_timestamp_to_time(ts: GrpcTimestamp, tzinfo: dt_tzinfo | None = None) -> ht_datetime:
    total_nanos = ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanos, _NS_PER_S)
    # Convert the nanoseconds to yoctoseconds.
    total_yoctoseconds = int(round(_YS_PER_NS * nanos))
    dt = _EPOCH_1970 + ht_timedelta(seconds = seconds) + ht_timedelta(yoctoseconds=total_yoctoseconds)
    return _convert_to_desired_timezone(dt, tzinfo)
