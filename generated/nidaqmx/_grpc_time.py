from datetime import timezone, timedelta
from datetime import datetime as std_datetime
from hightime import datetime as ht_datetime
from typing import Optional, Union

from google.protobuf.timestamp_pb2 import Timestamp as GrpcTimestamp


_NS_PER_S = 10**9
_NS_PER_US = 10**3

_YS_PER_US = 10**18
_YS_PER_NS = 10**15
_YS_PER_FS = 10**9


def convert_time_to_timestamp(dt: Union[std_datetime, ht_datetime], ts: Optional[GrpcTimestamp] = None) -> GrpcTimestamp:
    utc_dt = dt.astimezone(tz=timezone.utc)
    seconds = int(utc_dt.timestamp())
    if ts is None:
        ts = GrpcTimestamp()

    if isinstance(dt, ht_datetime):
        total_yoctoseconds = dt.yoctosecond
        total_yoctoseconds += dt.femtosecond * _YS_PER_FS
        total_yoctoseconds += dt.microsecond * _YS_PER_US
        nanos, remainder_yoctoseconds = divmod(total_yoctoseconds, _YS_PER_NS)
        # round up, if necessary
        if remainder_yoctoseconds >= _YS_PER_NS / 2:
            nanos += 1
    else:
        nanos = utc_dt.microsecond * _NS_PER_US

    ts.FromNanoseconds(seconds * _NS_PER_S + nanos)
    return ts


def convert_to_local_timezone(expected_time_utc):
    current_time_utc = ht_datetime.now(timezone.utc)
    local_timezone_offset = current_time_utc.astimezone().utcoffset()
    local_expected_time = expected_time_utc + local_timezone_offset
    return local_expected_time


def negative_timestamp_to_1904_epoch(negative_timestamp):
    epoch_1904 = ht_datetime(1904, 1, 1)
    delta = timedelta(seconds=abs(negative_timestamp))
    datetime_1904 = epoch_1904 - delta
    return datetime_1904


def convert_timestamp_to_time(ts: GrpcTimestamp, tzinfo: Optional[timezone] = None) -> ht_datetime:
    total_nanos = ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanos, _NS_PER_S)

    # Convert the nanoseconds to micro, femto, and yoctorseconds.
    total_yoctoseconds = int(round(_YS_PER_NS * nanos))
    microsecond, remainder_yoctoseconds = divmod(total_yoctoseconds, _YS_PER_US)
    femtosecond, remainder_yoctoseconds = divmod(remainder_yoctoseconds, _YS_PER_FS)
    yoctosecond = remainder_yoctoseconds

    if seconds < 0:
        dt = negative_timestamp_to_1904_epoch(negative_timestamp)
    else:
        dt = ht_datetime.fromtimestamp(seconds, timezone.utc)

    # Add in precision
    dt = dt.replace(microsecond=microsecond, femtosecond=femtosecond, yoctosecond=yoctosecond)

    # Then convert to requested timezone
    if seconds < 0:
        return convert_to_local_timezone(dt)
    else:
        return dt.astimezone(tz=tzinfo)
