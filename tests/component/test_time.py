import random
from copy import copy
from datetime import datetime as std_datetime
from datetime import timedelta, timezone

import pytest
from hightime import datetime as ht_datetime

try:
    from nidaqmx._grpc_time import Timestamp as GrpcTimestamp
except ImportError:
    GrpcTimestamp = None

from nidaqmx._lib_time import AbsoluteTime as LibTimestamp

# Jan 1, 2002 = 98 years + 25 leapdays = 35795 days = 3092688000 seconds
JAN_01_2022_TIMESTAMP_1904_EPOCH = 0xB856AC80
# Jan 1, 2002 = 32 years + 8 leapdays = 11688 days = 1009843200 seconds
JAN_01_2022_TIMESTAMP_1970_EPOCH = 0x3C30FC00
JAN_01_2022_LIB = LibTimestamp(lsb=0, msb=JAN_01_2022_TIMESTAMP_1904_EPOCH)
# Unfortunately, gRPC's Timestamp class doesn't have a simple constructor that takes raw values.
JAN_01_2022_DATETIME = std_datetime(2002, 1, 1, tzinfo=timezone.utc)
JAN_01_2022_HIGHTIME = ht_datetime(2002, 1, 1, tzinfo=timezone.utc)


def test___libtimestamp___ordering___succeeds():
    ordered = [
        LibTimestamp(msb=1, lsb=0),
        LibTimestamp(msb=2, lsb=0),
        LibTimestamp(msb=2, lsb=1),
        LibTimestamp(msb=2, lsb=2),
        LibTimestamp(msb=3, lsb=0),
    ]

    shuffled = copy(ordered)
    random.shuffle(shuffled)
    assert sorted(shuffled) == ordered


@pytest.mark.parametrize("from_dt", [(JAN_01_2022_DATETIME), (JAN_01_2022_HIGHTIME)])
def test___libtimestamp___convert_from_utc___succeeds(from_dt):
    ts = LibTimestamp.from_datetime(from_dt)
    assert ts == JAN_01_2022_LIB


def test___libtimestamp___convert_to_utc___succeeds():
    dt = JAN_01_2022_LIB.to_datetime(tzinfo=timezone.utc)
    assert dt == JAN_01_2022_HIGHTIME


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
def test___libtimestamp___convert_to_and_from_tz___succeeds(datetime_cls, tzinfo, expected_offset):
    from_dt = datetime_cls(2002, 1, 1, tzinfo=tzinfo)
    ts = LibTimestamp.from_datetime(from_dt)

    assert ts.msb == JAN_01_2022_LIB.msb + expected_offset
    assert ts.lsb == JAN_01_2022_LIB.lsb

    # now convert back
    to_dt = ts.to_datetime(tzinfo=tzinfo)
    assert from_dt == to_dt


@pytest.mark.parametrize(
    "from_dt, microsecond, subseconds",
    [
        (JAN_01_2022_DATETIME, 0, 0),
        (JAN_01_2022_DATETIME, 1, 0x10C6F7A0B5EE),
        (JAN_01_2022_DATETIME, 250000, 0x4000000000000000),
        (JAN_01_2022_DATETIME, 500000, 0x8000000000000000),
        (JAN_01_2022_DATETIME, 750000, 0xC000000000000000),
        (JAN_01_2022_DATETIME, 999999, 0xFFFFEF39085F4800),
        (JAN_01_2022_HIGHTIME, 0, 0),
        (JAN_01_2022_HIGHTIME, 1, 0x10C6F7A0B5EE),
        (JAN_01_2022_HIGHTIME, 250000, 0x4000000000000000),
        (JAN_01_2022_HIGHTIME, 500000, 0x8000000000000000),
        (JAN_01_2022_HIGHTIME, 750000, 0xC000000000000000),
        (JAN_01_2022_HIGHTIME, 999999, 0xFFFFEF39085F4800),
    ],
)
def test___libtimestamp___convert_microseconds_to_and_from_subseconds___succeeds(
    from_dt, microsecond, subseconds
):
    precise_dt = from_dt.replace(microsecond=microsecond)
    ts = LibTimestamp.from_datetime(precise_dt)

    # whole seconds shouldn't change
    assert ts.msb == JAN_01_2022_LIB.msb
    assert ts.lsb == subseconds

    # now convert back
    to_dt = ts.to_datetime(tzinfo=timezone.utc)

    to_dt_microsecond = to_dt.microsecond
    # comparison is tricky since imprecision in the conversion to NI-BTF are
    # caught by the higher precision values in hightime, so we round here.
    if to_dt.femtosecond > LibTimestamp.MAX_FS / 2:
        to_dt_microsecond += 1

    assert to_dt_microsecond == microsecond


@pytest.mark.parametrize(
    "from_dt, femtosecond, subseconds",
    [
        (JAN_01_2022_HIGHTIME, 0, 0),
        (JAN_01_2022_HIGHTIME, 1, 0x480F),
    ],
)
def test___libtimestamp___convert_femtoseconds_to_and_from_subseconds___succeeds(
    from_dt, femtosecond, subseconds
):
    precise_dt = from_dt.replace(femtosecond=femtosecond)
    ts = LibTimestamp.from_datetime(precise_dt)

    # whole seconds shouldn't change
    assert ts.msb == JAN_01_2022_LIB.msb
    assert ts.lsb == subseconds

    # now convert back
    to_dt = ts.to_datetime(tzinfo=timezone.utc)
    to_dt_femtosecond = to_dt.femtosecond
    # comparison is tricky since imprecision in the conversion to NI-BTF are
    # caught by the higher precision values in hightime, so we round here.
    if to_dt.yoctosecond > LibTimestamp.MAX_YS / 2:
        to_dt_femtosecond += 1
    assert to_dt_femtosecond == femtosecond


@pytest.mark.parametrize(
    "from_dt, yoctosecond, subseconds, yoctosecond_round_trip",
    [
        (JAN_01_2022_HIGHTIME, 0, 0, 0),
        # Yoctoseconds is quite a bit more precise than NI-BTF
        (JAN_01_2022_HIGHTIME, 54210, 1, 54210),
        (JAN_01_2022_HIGHTIME, 54211, 1, 54210),
    ],
)
def test___libtimestamp___convert_yoctoseconds_to_and_from_subseconds___succeeds(
    from_dt, yoctosecond, subseconds, yoctosecond_round_trip
):
    precise_dt = from_dt.replace(yoctosecond=yoctosecond)
    ts = LibTimestamp.from_datetime(precise_dt)

    # whole seconds shouldn't change
    assert ts.msb == JAN_01_2022_LIB.msb
    assert ts.lsb == subseconds

    # now convert back
    to_dt = ts.to_datetime(tzinfo=timezone.utc)
    assert to_dt.yoctosecond == yoctosecond_round_trip


# Note: I can't actually test overflow because Python's datetime object is
# limited to years 1-9999, but the NI-BTF format can represent time before the
# Big Bang and until about year 292 billion. Oh well.


@pytest.mark.parametrize("from_dt", [(JAN_01_2022_DATETIME), (JAN_01_2022_HIGHTIME)])
def test___grpctimestamp___convert_from_utc___succeeds(from_dt):
    ts = GrpcTimestamp()
    ts.FromDatetime(from_dt)
    assert ts.seconds == JAN_01_2022_TIMESTAMP_1970_EPOCH
    assert ts.nanos == 0


def test___grpctimestamp___convert_to_utc___succeeds():
    ts = GrpcTimestamp()
    ts.FromSeconds(JAN_01_2022_TIMESTAMP_1970_EPOCH)
    dt = ts.ToDatetime(tzinfo=timezone.utc)
    assert dt == JAN_01_2022_HIGHTIME


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
def test___grpctimestamp___convert_to_and_from_tz___succeeds(datetime_cls, tzinfo, expected_offset):
    from_dt = datetime_cls(2002, 1, 1, tzinfo=tzinfo)
    ts = GrpcTimestamp()
    ts.FromDatetime(from_dt)

    assert ts.seconds == JAN_01_2022_TIMESTAMP_1970_EPOCH + expected_offset
    assert ts.nanos == 0

    # now convert back
    to_dt = ts.ToDatetime(tzinfo=tzinfo)
    assert from_dt == to_dt


@pytest.mark.parametrize(
    "from_dt, microsecond, nanoseconds",
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
def test___grpctimestamp___convert_microseconds_to_and_from_nanoseconds___succeeds(
    from_dt, microsecond, nanoseconds
):
    precise_dt = from_dt.replace(microsecond=microsecond)
    ts = GrpcTimestamp()
    ts.FromDatetime(precise_dt)

    # whole seconds shouldn't change
    assert ts.seconds == JAN_01_2022_TIMESTAMP_1970_EPOCH
    assert ts.nanos == nanoseconds

    # now convert back
    to_dt = ts.ToDatetime(tzinfo=timezone.utc)
    assert to_dt.microsecond == microsecond


@pytest.mark.parametrize(
    "from_dt, femtosecond, nanoseconds",
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
def test___grpctimestamp___convert_femtoseconds_to_and_from_nanoseconds___succeeds(
    from_dt, femtosecond, nanoseconds
):
    precise_dt = from_dt.replace(femtosecond=femtosecond)
    ts = LibTimestamp.from_datetime(precise_dt)
    ts = GrpcTimestamp()
    ts.FromDatetime(precise_dt)

    # whole seconds shouldn't change
    assert ts.seconds == JAN_01_2022_TIMESTAMP_1970_EPOCH
    assert ts.nanos == nanoseconds

    # now convert back
    to_dt = ts.ToDatetime(tzinfo=timezone.utc)
    # we lost femtosecond precision coercing to nanoseconds.
    assert to_dt.femtosecond == nanoseconds * (10**6)
