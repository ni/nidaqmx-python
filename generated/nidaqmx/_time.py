from __future__ import annotations

import pytz
from tzlocal import get_localzone
from datetime import timezone
from datetime import datetime as std_datetime
from hightime import datetime as ht_datetime
from typing import Optional, Union

# theoretically the same as astimezone(), but with support for dates before 1970
def _convert_to_desired_timezone(expected_time_utc: Union[std_datetime, ht_datetime], tzinfo: Optional[timezone] = None):
    # if timezone matches, no need to do conversion
    if expected_time_utc.tzinfo is tzinfo:
        return expected_time_utc

    # if timezone is not defined, use system timezone
    if tzinfo is None:
        local_timezone = get_localzone()
        tzinfo = pytz.timezone(str(local_timezone))

    # use pytz here to account for daylight savings
    if isinstance(tzinfo, pytz.tzinfo.BaseTzInfo):
        target_tz = pytz.timezone(str(tzinfo))
        # we need to make expected_time_utc naive in order to use localize
        expected_time_utc = expected_time_utc.replace(tzinfo=None)
        localized_time = target_tz.localize(expected_time_utc)
        desired_expected_time = target_tz.fromutc(localized_time)
        return(desired_expected_time)

    # if the tzinfo passed in is a timedelta function, then we don't need to consider daylight savings
    elif isinstance(tzinfo, timezone) and tzinfo.utcoffset(None) is not None:
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