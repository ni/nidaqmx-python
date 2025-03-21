from __future__ import annotations

from tzlocal import get_localzone
from datetime import timezone
from datetime import tzinfo as dt_tzinfo
from datetime import datetime as std_datetime
from hightime import datetime as ht_datetime
from typing import Optional, Union
from zoneinfo import ZoneInfo

# theoretically the same as astimezone(), but with support for dates before 1970
def _convert_to_desired_timezone(expected_time_utc: std_datetime | ht_datetime, tzinfo: dt_tzinfo | None = None) -> std_datetime | ht_datetime:
    # if timezone matches, no need to do conversion
    if expected_time_utc.tzinfo is tzinfo:
        return expected_time_utc

    # if timezone is not defined, use system timezone
    if tzinfo is None:
        tzinfo = get_localzone()

    # use ZoneInfo here to account for daylight savings
    if isinstance(tzinfo, ZoneInfo):
        localized_time = expected_time_utc.replace(tzinfo=tzinfo)
        desired_expected_time = tzinfo.fromutc(localized_time)
        return(desired_expected_time)

    # if the tzinfo passed in is a timedelta function, then we don't need to consider daylight savings
    elif tzinfo.utcoffset(None) is not None:
        current_time_utc = ht_datetime.now(timezone.utc)
        desired_timezone_offset = current_time_utc.astimezone(tz=tzinfo).utcoffset()
        desired_expected_time = expected_time_utc + desired_timezone_offset
        new_datetime = desired_expected_time.replace(tzinfo=tzinfo)
        return new_datetime

    # if the tzinfo passed in is none of the above, fall back to original astimezone()
    else:
        return expected_time_utc.astimezone(tzinfo)
