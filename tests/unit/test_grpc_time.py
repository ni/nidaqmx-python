from datetime import datetime as std_datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pytest
from hightime import datetime as ht_datetime

from tests.unit._time_utils import (
    JAN_01_1850_DATETIME,
    JAN_01_1850_HIGHTIME,
    JAN_01_1850_TIMESTAMP_1970_EPOCH,
    JAN_01_2002_DATETIME,
    JAN_01_2002_HIGHTIME,
    JAN_01_2002_TIMESTAMP_1970_EPOCH,
)

try:
    import nidaqmx._grpc_time as grpc_time
    import nidaqmx._stubs.nidaqmx_pb2 as nidaqmx_pb2
except ImportError:
    pass


@pytest.mark.parametrize("from_dt", [(JAN_01_2002_DATETIME), (JAN_01_2002_HIGHTIME)])
def test___utc_datetime_after_1970___convert_to_timestamp___is_reversible(from_dt):
    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    total_nanoseconds = to_ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH
    assert nanos == 0
    assert roundtrip_dt == JAN_01_2002_HIGHTIME


@pytest.mark.parametrize("from_dt", [(JAN_01_1850_DATETIME), (JAN_01_1850_HIGHTIME)])
def test___utc_datetime_before_1970___convert_to_timestamp___is_reversible(from_dt):
    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    total_nanoseconds = to_ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH
    assert nanos == 0
    assert roundtrip_dt == JAN_01_1850_HIGHTIME


@pytest.mark.parametrize("request_dt", [(JAN_01_2002_DATETIME), (JAN_01_2002_HIGHTIME)])
def test___utc_datetime_after_1970___convert_to_grpc_request___succeeds(request_dt):
    request = nidaqmx_pb2.CfgTimeStartTrigRequest()

    grpc_time.convert_time_to_timestamp(request_dt, request.when)

    total_nanoseconds = request.when.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH
    assert nanos == 0


@pytest.mark.parametrize("request_dt", [(JAN_01_1850_DATETIME), (JAN_01_1850_HIGHTIME)])
def test___utc_datetime_before_1970___convert_to_grpc_request___succeeds(request_dt):
    request = nidaqmx_pb2.CfgTimeStartTrigRequest()

    grpc_time.convert_time_to_timestamp(request_dt, request.when)

    total_nanoseconds = request.when.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH
    assert nanos == 0


@pytest.mark.parametrize("response_dt", [(JAN_01_2002_DATETIME), (JAN_01_2002_HIGHTIME)])
def test___grpc_response_after_1970___convert_to_timestamp___succeeds(response_dt):
    response = nidaqmx_pb2.GetStartTrigTrigWhenResponse()
    grpc_time.convert_time_to_timestamp(response_dt, response.data)

    to_dt = grpc_time.convert_timestamp_to_time(response.data, tzinfo=timezone.utc)

    assert to_dt == JAN_01_2002_HIGHTIME


@pytest.mark.parametrize("response_dt", [(JAN_01_1850_DATETIME), (JAN_01_1850_HIGHTIME)])
def test___grpc_response_before_1970___convert_to_timestamp___succeeds(response_dt):
    response = nidaqmx_pb2.GetStartTrigTrigWhenResponse()
    grpc_time.convert_time_to_timestamp(response_dt, response.data)

    to_dt = grpc_time.convert_timestamp_to_time(response.data, tzinfo=timezone.utc)

    assert to_dt == JAN_01_1850_HIGHTIME


@pytest.mark.parametrize(
    "date",
    [
        (std_datetime(1904, 1, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 1, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 2, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 3, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 4, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 5, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 6, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 7, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 8, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 9, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 10, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 11, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 12, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 1, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 2, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 3, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 4, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 5, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 6, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 7, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 8, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 9, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 10, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 11, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 12, 1, tzinfo=timezone.utc)),
    ],
)
def test___utc_datetime___convert_to_timestamp_with_dst___is_reversible(date):
    # we use a location that has daylight savings date change on the dates above
    target_timezone = ZoneInfo("America/Los_Angeles")
    astimezone_date = date.astimezone(target_timezone)

    to_ts = grpc_time.convert_time_to_timestamp(date)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=target_timezone)

    assert astimezone_date == roundtrip_dt


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
def test___tz_datetime_after_1970___convert_to_timestamp___is_reversible(
    datetime_cls, tzinfo, expected_offset
):
    from_dt = datetime_cls(2002, 1, 1, tzinfo=tzinfo)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=tzinfo)

    assert to_ts.seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH + expected_offset
    assert to_ts.nanos == 0
    assert from_dt == roundtrip_dt


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
def test___tz_datetime_before_1970___convert_to_timestamp___is_reversible(
    datetime_cls, tzinfo, expected_offset
):
    from_dt = datetime_cls(1850, 1, 1, tzinfo=tzinfo)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=tzinfo)

    assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH + expected_offset
    assert to_ts.nanos == 0
    assert from_dt == roundtrip_dt


@pytest.mark.parametrize(
    "base_dt, microsecond, nanoseconds",
    [
        (JAN_01_2002_DATETIME, 0, 0),
        (JAN_01_2002_DATETIME, 1, 1000),
        (JAN_01_2002_DATETIME, 250000, 250000000),
        (JAN_01_2002_DATETIME, 500000, 500000000),
        (JAN_01_2002_DATETIME, 750000, 750000000),
        (JAN_01_2002_DATETIME, 999999, 999999000),
        (JAN_01_2002_HIGHTIME, 0, 0),
        (JAN_01_2002_HIGHTIME, 1, 1000),
        (JAN_01_2002_HIGHTIME, 250000, 250000000),
        (JAN_01_2002_HIGHTIME, 500000, 500000000),
        (JAN_01_2002_HIGHTIME, 750000, 750000000),
        (JAN_01_2002_HIGHTIME, 999999, 999999000),
    ],
)
def test___datetime_after_1970_with_microseconds___convert_to_timestamp___is_reversible(
    base_dt, microsecond, nanoseconds
):
    from_dt = base_dt.replace(microsecond=microsecond)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    assert to_ts.seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    assert roundtrip_dt.microsecond == microsecond


@pytest.mark.parametrize(
    "base_dt, microsecond, nanoseconds",
    [
        (JAN_01_1850_DATETIME, 0, 0),
        (JAN_01_1850_DATETIME, 1, 1000),
        (JAN_01_1850_DATETIME, 250000, 250000000),
        (JAN_01_1850_DATETIME, 500000, 500000000),
        (JAN_01_1850_DATETIME, 750000, 750000000),
        (JAN_01_1850_DATETIME, 999999, 999999000),
        (JAN_01_1850_HIGHTIME, 0, 0),
        (JAN_01_1850_HIGHTIME, 1, 1000),
        (JAN_01_1850_HIGHTIME, 250000, 250000000),
        (JAN_01_1850_HIGHTIME, 500000, 500000000),
        (JAN_01_1850_HIGHTIME, 750000, 750000000),
        (JAN_01_1850_HIGHTIME, 999999, 999999000),
    ],
)
def test___datetime_before_1970_with_microseconds___convert_to_timestamp___is_reversible(
    base_dt, microsecond, nanoseconds
):
    from_dt = base_dt.replace(microsecond=microsecond)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    if microsecond:
        # with a change of non-zero subsecond value, the seconds value is off by 1
        # because of negative seconds value
        assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH + 1
    else:
        assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    assert roundtrip_dt.microsecond == microsecond


@pytest.mark.parametrize(
    "base_dt, femtosecond, nanoseconds",
    [
        (JAN_01_2002_HIGHTIME, 0, 0),
        (JAN_01_2002_HIGHTIME, 1, 0),
        # If femtoseconds get high enough, then it should round up
        (JAN_01_2002_HIGHTIME, 500000, 1),
        (JAN_01_2002_HIGHTIME, 999999, 1),
        # And of course, whole nanos
        (JAN_01_2002_HIGHTIME, 1000000, 1),
        (JAN_01_2002_HIGHTIME, 1000001, 1),
        (JAN_01_2002_HIGHTIME, 1500000, 2),
        (JAN_01_2002_HIGHTIME, 1999999, 2),
        (JAN_01_2002_HIGHTIME, 2000000, 2),
        (JAN_01_2002_HIGHTIME, 2000001, 2),
    ],
)
def test___datetime_after_1970_with_femtoseconds___convert_to_timestamp___is_reversible(
    base_dt, femtosecond, nanoseconds
):
    from_dt = base_dt.replace(femtosecond=femtosecond)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    assert to_ts.seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    # we lost femtosecond precision coercing to nanoseconds.
    assert roundtrip_dt.femtosecond == nanoseconds * (10**6)


@pytest.mark.parametrize(
    "base_dt, femtosecond, nanoseconds",
    [
        (JAN_01_1850_HIGHTIME, 0, 0),
        (JAN_01_1850_HIGHTIME, 1, 0),
        # If femtoseconds get high enough, then it should round up
        (JAN_01_1850_HIGHTIME, 500000, 1),
        (JAN_01_1850_HIGHTIME, 999999, 1),
        # And of course, whole nanos
        (JAN_01_1850_HIGHTIME, 1000000, 1),
        (JAN_01_1850_HIGHTIME, 1000001, 1),
        (JAN_01_1850_HIGHTIME, 1500000, 2),
        (JAN_01_1850_HIGHTIME, 1999999, 2),
        (JAN_01_1850_HIGHTIME, 2000000, 2),
        (JAN_01_1850_HIGHTIME, 2000001, 2),
    ],
)
def test___datetime_before_1970_with_femtoseconds___convert_to_timestamp___is_reversible(
    base_dt, femtosecond, nanoseconds
):
    from_dt = base_dt.replace(femtosecond=femtosecond)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    if femtosecond:
        # with a change of non-zero subsecond value, the seconds value is off by 1
        # because of negative seconds value
        assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH + 1
    else:
        assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    # we lost femtosecond precision coercing to nanoseconds.
    assert roundtrip_dt.femtosecond == nanoseconds * (10**6)
