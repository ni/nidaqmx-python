from datetime import datetime as std_datetime
from datetime import timezone

from hightime import datetime as ht_datetime

# Jan 1, 2002 = 32 years + 8 leapdays = 11688 days = 1009843200 seconds
JAN_01_2002_TIMESTAMP_1970_EPOCH = 0x3C30FC00
JAN_01_1850_TIMESTAMP_1970_EPOCH = -0xE1B65F80
# Jan 1, 2002 = 98 years + 25 leapdays = 35795 days = 3092688000 seconds
JAN_01_2002_TIMESTAMP_1904_EPOCH = 0xB856AC80
JAN_01_1904_TIMESTAMP_1904_EPOCH = 0
JAN_01_1850_TIMESTAMP_1904_EPOCH = -0x6590AF00

JAN_01_2002_DATETIME = std_datetime(2002, 1, 1, tzinfo=timezone.utc)
JAN_01_2002_HIGHTIME = ht_datetime(2002, 1, 1, tzinfo=timezone.utc)
JAN_01_1904_DATETIME = std_datetime(1904, 1, 1, tzinfo=timezone.utc)
JAN_01_1904_HIGHTIME = ht_datetime(1904, 1, 1, tzinfo=timezone.utc)
JAN_01_1850_DATETIME = std_datetime(1850, 1, 1, tzinfo=timezone.utc)
JAN_01_1850_HIGHTIME = ht_datetime(1850, 1, 1, tzinfo=timezone.utc)
