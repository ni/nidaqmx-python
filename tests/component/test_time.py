from copy import copy
import pytest
import random

from datetime import datetime as std_datetime
from datetime import timedelta, timezone

from hightime import datetime as ht_datetime

from nidaqmx.time import AbsoluteTime

# Jan 1, 2002 = 98 years + 25 leapdays = 35,795 days = 3,092,688,000 seconds
JAN_01_2022_BTF = AbsoluteTime(lsb=0, msb=0xb856ac80)
JAN_01_2022_DATETIME = std_datetime(2002, 1, 1, tzinfo=timezone.utc)
JAN_01_2022_HIGHTIME = ht_datetime(2002, 1, 1, tzinfo=timezone.utc)


def test___datetime___ordering___succeeds():
    ordered = [
        AbsoluteTime(msb=1, lsb=0),
        AbsoluteTime(msb=2, lsb=0),
        AbsoluteTime(msb=2, lsb=1),
        AbsoluteTime(msb=2, lsb=2),
        AbsoluteTime(msb=3, lsb=0)
    ]

    shuffled = copy(ordered)
    random.shuffle(shuffled)
    assert sorted(shuffled) == ordered


@pytest.mark.parametrize(
    "from_dt", [
        (JAN_01_2022_DATETIME),
        (JAN_01_2022_HIGHTIME)
    ]
)
def test___time___convert_from_utc___succeeds(from_dt):
    btf = AbsoluteTime.from_datetime(from_dt)
    assert btf == JAN_01_2022_BTF


@pytest.mark.parametrize(
    # Note that these are equivalent since there are 0 values in the sub-microsecond precision
    "expected_dt", [
        (JAN_01_2022_DATETIME),
        (JAN_01_2022_HIGHTIME)
    ]
)
def test___time___convert_to_utc___succeeds(expected_dt):
    dt = JAN_01_2022_BTF.to_datetime()
    assert dt == JAN_01_2022_HIGHTIME


@pytest.mark.parametrize(
    "datetime_cls, tzinfo, expected_offset", [
        (std_datetime, timezone(timedelta(minutes=30)), -1800),
        (std_datetime, timezone(timedelta(minutes=-30)), 1800),
        (std_datetime, timezone(timedelta(hours=1)), -3600),
        (std_datetime, timezone(timedelta(hours=-1)), 3600),
        (ht_datetime, timezone(timedelta(minutes=30)), -1800),
        (ht_datetime, timezone(timedelta(minutes=-30)), 1800),
        (ht_datetime, timezone(timedelta(hours=1)), -3600),
        (ht_datetime, timezone(timedelta(hours=-1)), 3600),
    ]
)
def test___time___convert_to_and_from_tz___succeeds(datetime_cls, tzinfo, expected_offset):
    from_dt = datetime_cls(2002, 1, 1, tzinfo=tzinfo)
    btf = AbsoluteTime.from_datetime(from_dt)

    assert btf.msb == JAN_01_2022_BTF.msb + expected_offset
    assert btf.lsb == JAN_01_2022_BTF.lsb

    # now convert back
    to_dt = btf.to_datetime(tzinfo=tzinfo)
    assert from_dt == to_dt


@pytest.mark.parametrize(
    "from_dt, microsecond, subseconds", [
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
    ]
)
def test___datetime___convert_microseconds_to_and_from_subseconds___succeeds(from_dt, microsecond, subseconds):
    precise_dt = from_dt.replace(microsecond=microsecond)
    btf = AbsoluteTime.from_datetime(precise_dt)

    # whole seconds shouldn't change
    assert btf.msb == JAN_01_2022_BTF.msb
    assert btf.lsb == subseconds

    # now convert back
    to_dt = btf.to_datetime()

    to_dt_microsecond = to_dt.microsecond
    # comparison is tricky since imprecision in the conversion to NI-BTF are
    # caught by the higher precision values in hightime, so we round here.
    if to_dt.femtosecond > AbsoluteTime.MAX_FS / 2:
        to_dt_microsecond += 1

    assert to_dt_microsecond == microsecond


@pytest.mark.parametrize(
    "from_dt, femtosecond, subseconds", [
        (JAN_01_2022_HIGHTIME, 0, 0),
        (JAN_01_2022_HIGHTIME, 1, 0x480F),
    ]
)
def test___datetime___convert_femtoseconds_to_and_from_subseconds___succeeds(from_dt, femtosecond, subseconds):
    precise_dt = from_dt.replace(femtosecond=femtosecond)
    btf = AbsoluteTime.from_datetime(precise_dt)

    # whole seconds shouldn't change
    assert btf.msb == JAN_01_2022_BTF.msb
    assert btf.lsb == subseconds

    # now convert back
    to_dt = btf.to_datetime()

    to_dt_femtosecond = to_dt.femtosecond
    # comparison is tricky since imprecision in the conversion to NI-BTF are
    # caught by the higher precision values in hightime, so we round here.
    if to_dt.yoctosecond > AbsoluteTime.MAX_YS / 2:
        to_dt_femtosecond += 1

    assert to_dt_femtosecond == femtosecond


@pytest.mark.parametrize(
    "from_dt, yoctosecond, subseconds, yoctosecond_round_trip", [
        (JAN_01_2022_HIGHTIME, 0, 0, 0),
        # Yoctoseconds is quite a bit more precise than NI-BTF
        (JAN_01_2022_HIGHTIME, 54210, 1, 54210),
        (JAN_01_2022_HIGHTIME, 54211, 1, 54210),
    ]
)
def test___datetime___convert_yoctoseconds_to_and_from_subseconds___succeeds(from_dt, yoctosecond, subseconds, yoctosecond_round_trip):
    precise_dt = from_dt.replace(yoctosecond=yoctosecond)
    btf = AbsoluteTime.from_datetime(precise_dt)

    # whole seconds shouldn't change
    assert btf.msb == JAN_01_2022_BTF.msb
    assert btf.lsb == subseconds

    # now convert back
    to_dt = btf.to_datetime()
    assert to_dt.yoctosecond == yoctosecond_round_trip


# Note: I can't actually test overflow because Python's datetime object is
# limited to years 1-9999, but the NI-BTF format can represent time before the
# Big Bang and until about year 292 billion. Oh well.