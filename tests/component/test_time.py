from copy import copy
import pytest
import random

from datetime import datetime, timedelta, timezone
from nidaqmx.time import AbsoluteTime

# Jan 1, 2002 = 98 years + 25 leapdays = 35,795 days = 3,092,688,000 seconds
JAN_01_2022_BTF = AbsoluteTime(lsb=0, msb=0xb856ac80)
JAN_01_2022_DATETIME = datetime(2002, 1, 1, tzinfo=timezone.utc)


def test___time___convert_from_utc___succeeds():
    btf = AbsoluteTime.from_datetime(JAN_01_2022_DATETIME)
    assert btf == JAN_01_2022_BTF


def test___time___convert_to_utc___succeeds():
    dt = JAN_01_2022_BTF.to_datetime()
    assert dt == JAN_01_2022_DATETIME


@pytest.mark.parametrize(
    "tzinfo, expected_offset", [
        (timezone(timedelta(minutes=30)), -1800),
        (timezone(timedelta(minutes=-30)), 1800),
        (timezone(timedelta(hours=1)), -3600),
        (timezone(timedelta(hours=-1)), 3600),
    ]
)
def test___time___convert_to_and_from_tz___succeeds(tzinfo, expected_offset):
    from_dt = datetime(2002, 1, 1, tzinfo=tzinfo)
    btf = AbsoluteTime.from_datetime(from_dt)

    assert btf.msb == JAN_01_2022_BTF.msb + expected_offset
    assert btf.lsb == JAN_01_2022_BTF.lsb

    # now convert back
    to_dt = btf.to_datetime(tzinfo=tzinfo)
    assert from_dt == to_dt


@pytest.mark.parametrize(
    "microsecond, subseconds", [
        (0, 0),
        (1, 0x10C6F7A0B5EE),
        (250000, 0x4000000000000000),
        (500000, 0x8000000000000000),
        (750000, 0xC000000000000000),
        (999999, 0xFFFFEF39085F4800),
    ]
)
def test___time___convert_microseconds_to_and_from_subseconds___succeeds(microsecond, subseconds):
    from_dt = JAN_01_2022_DATETIME.replace(microsecond=microsecond)
    btf = AbsoluteTime.from_datetime(from_dt)

    # whole seconds shouldn't change
    assert btf.msb == JAN_01_2022_BTF.msb
    assert btf.lsb == subseconds

    # now convert back
    to_dt = btf.to_datetime()
    assert to_dt.microsecond == microsecond

    # zero out microsecond, and we should be back
    assert to_dt.replace(microsecond=0) == JAN_01_2022_DATETIME


# Note: I can't actually test overflow because Python's datetime object is
# limited to years 1-9999, but the NI-BTF format can represent time before the
# Big Bang and until about year 292 billion. Oh well.


def test___time___ordering___succeeds():
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