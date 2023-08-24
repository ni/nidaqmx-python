import random
from copy import copy
from datetime import datetime as std_datetime
from datetime import timedelta, timezone

import pytest
from hightime import datetime as ht_datetime

try:
    import nidaqmx._grpc_time as grpc_time
    from google.protobuf.timestamp_pb2 import Timestamp as GrpcTimestamp
except ImportError:
    grpc_time = none
    GrpcTimestamp = None

# TODO: single-source
# Jan 1, 2002 = 32 years + 8 leapdays = 11688 days = 1009843200 seconds
JAN_01_2022_TIMESTAMP_1970_EPOCH = 0x3C30FC00
JAN_01_2022_DATETIME = std_datetime(2002, 1, 1, tzinfo=timezone.utc)
JAN_01_2022_HIGHTIME = ht_datetime(2002, 1, 1, tzinfo=timezone.utc)


@pytest.mark.parametrize("from_dt", [(JAN_01_2022_DATETIME), (JAN_01_2022_HIGHTIME)])
def test___utc_datetime___convert_to_timestamp___is_reversible(from_dt):
    to_ts = GrpcTimestamp()
    grpc_time.convert_time_to_timestamp(from_dt, to_ts)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    total_nanoseconds = to_ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_2022_TIMESTAMP_1970_EPOCH
    assert nanos == 0
    assert roundtrip_dt == JAN_01_2022_HIGHTIME


@pytest.mark.parametrize(
    "datetime_cls, tzinfo, expected_offset",
    [
        (std_datetime, timezone(timedelta(minutes=30)), -1800),
        (std_datetime, timezone(timedelta(minutes=-30)), 1800),
        (std_datetime, timezone(timedelta(hours=1)), -3600),
        (std_datetime, timezone(timedelta(hours=-1)), 3600),
        (ht_datetime, timezone(timedelta(minutes=30)), -1800),
        (ht_datetime, timezone(timedelta(minutes=-30)), 1800),
        (ht_datetime, timezone(timedelta(hours=1)), -3600),
        (ht_datetime, timezone(timedelta(hours=-1)), 3600),
    ],
)
def test___tz_datetime___convert_to_timestamp___is_reversible(datetime_cls, tzinfo, expected_offset):
    from_dt = datetime_cls(2002, 1, 1, tzinfo=tzinfo)
    
    to_ts = GrpcTimestamp()
    grpc_time.convert_time_to_timestamp(from_dt, to_ts)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=tzinfo)

    assert to_ts.seconds == JAN_01_2022_TIMESTAMP_1970_EPOCH + expected_offset
    assert to_ts.nanos == 0
    assert from_dt == roundtrip_dt


@pytest.mark.parametrize(
    "base_dt, microsecond, nanoseconds",
    [
        (JAN_01_2022_DATETIME, 0, 0),
        (JAN_01_2022_DATETIME, 1, 1000),
        (JAN_01_2022_DATETIME, 250000, 250000000),
        (JAN_01_2022_DATETIME, 500000, 500000000),
        (JAN_01_2022_DATETIME, 750000, 750000000),
        (JAN_01_2022_DATETIME, 999999, 999999000),
        (JAN_01_2022_HIGHTIME, 0, 0),
        (JAN_01_2022_HIGHTIME, 1, 1000),
        (JAN_01_2022_HIGHTIME, 250000, 250000000),
        (JAN_01_2022_HIGHTIME, 500000, 500000000),
        (JAN_01_2022_HIGHTIME, 750000, 750000000),
        (JAN_01_2022_HIGHTIME, 999999, 999999000),
    ],
)
def test___datetime_with_microseconds___convert_to_timestamp___is_reversible(
    base_dt, microsecond, nanoseconds
):
    from_dt = base_dt.replace(microsecond=microsecond)
    
    to_ts = GrpcTimestamp()
    grpc_time.convert_time_to_timestamp(from_dt, to_ts)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    assert to_ts.seconds == JAN_01_2022_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    assert roundtrip_dt.microsecond == microsecond


@pytest.mark.parametrize(
    "base_dt, femtosecond, nanoseconds",
    [
        (JAN_01_2022_HIGHTIME, 0, 0),
        (JAN_01_2022_HIGHTIME, 1, 0),
        # If femtoseconds get high enough, then it should round up
        (JAN_01_2022_HIGHTIME, 500000, 1),
        (JAN_01_2022_HIGHTIME, 999999, 1),
        # And of course, whole nanos
        (JAN_01_2022_HIGHTIME, 1000000, 1),
        (JAN_01_2022_HIGHTIME, 1000001, 1),
        (JAN_01_2022_HIGHTIME, 1500000, 2),
        (JAN_01_2022_HIGHTIME, 1999999, 2),
        (JAN_01_2022_HIGHTIME, 2000000, 2),
        (JAN_01_2022_HIGHTIME, 2000001, 2),
    ],
)
def test___datetime_with_femtoseconds___convert_to_timestamp___is_reversible(
    base_dt, femtosecond, nanoseconds
):
    from_dt = base_dt.replace(femtosecond=femtosecond)
    
    to_ts = GrpcTimestamp()
    grpc_time.convert_time_to_timestamp(from_dt, to_ts)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    assert to_ts.seconds == JAN_01_2022_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    # we lost femtosecond precision coercing to nanoseconds.
    assert roundtrip_dt.femtosecond == nanoseconds * (10**6)