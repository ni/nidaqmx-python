from datetime import timezone
from datetime import datetime as std_datetime
from hightime import datetime as ht_datetime
from hightime import timedelta as ht_timedelta
from typing import Optional, Union

from google.protobuf.timestamp_pb2 import Timestamp as GrpcTimestamp

# 66 years, 17 leap days = 24107 days = 2082844800 seconds
_BIAS_FROM_1970_EPOCH = 2082844800

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


def convert_to_desired_timezone(expected_time_utc, tzinfo):
    current_time_utc = ht_datetime.now(timezone.utc)
    desired_timezone_offset = current_time_utc.astimezone(tz=tzinfo).utcoffset()
    desired_expected_time = expected_time_utc + desired_timezone_offset
    new_datetime = ht_datetime(
            desired_expected_time.year,
            desired_expected_time.month,
            desired_expected_time.day,
            desired_expected_time.hour,
            desired_expected_time.minute,
            desired_expected_time.second,
            desired_expected_time.microsecond,
            desired_expected_time.femtosecond,
            desired_expected_time.yoctosecond,
            tzinfo = tzinfo)
    return new_datetime


def timestamp_to_1904_epoch(timestamp, yoctoseconds):
    epoch_1904 = ht_datetime(1904, 1, 1)
    if timestamp < 0:
        seconds_from_1904 = ht_timedelta(seconds = _BIAS_FROM_1970_EPOCH - abs(timestamp))
    else:
        seconds_from_1904 = ht_timedelta(seconds = _BIAS_FROM_1970_EPOCH + abs(timestamp))
    datetime_1904 = epoch_1904 + seconds_from_1904 + ht_timedelta(yoctoseconds=yoctoseconds)
    return datetime_1904


def convert_timestamp_to_time(ts: GrpcTimestamp, tzinfo: Optional[timezone] = None) -> ht_datetime:
    total_nanos = ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanos, _NS_PER_S)
    # Convert the nanoseconds to yoctoseconds.
    total_yoctoseconds = int(round(_YS_PER_NS * nanos))
    dt = timestamp_to_1904_epoch(seconds, total_yoctoseconds)
    return convert_to_desired_timezone(dt, tzinfo)
