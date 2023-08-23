from datetime import timezone
from hightime import datetime as ht_datetime

from google.protobuf.internal.well_known_types import Timestamp as grpc_Timestanp


class Timestamp(grpc_Timestanp):
    _NS_PER_US = 1000
    _YS_PER_US = 10**18
    _YS_PER_NS = 10**15
    _YS_PER_FS = 10**9

    def FromDatetime(self, dt):
        utc_dt = dt.astimezone(tz=timezone.utc)
        self.seconds = int(utc_dt.timestamp())

        if isinstance(dt, ht_datetime):
            total_yoctoseconds = dt.yoctosecond
            total_yoctoseconds += dt.femtosecond * Timestamp._YS_PER_FS
            total_yoctoseconds += dt.microsecond * Timestamp._YS_PER_US
            self.nanos, remainder_yoctoseconds = divmod(total_yoctoseconds, Timestamp._YS_PER_NS)
            # round up, if necessary
            if remainder_yoctoseconds >= Timestamp._YS_PER_NS / 2:
                self.nanos += 1
        else:
            self.nanos = utc_dt.microsecond * Timestamp._NS_PER_US

    def ToDatetime(self, tzinfo=None):
        # Convert the subseconds to micro and nanoseconds.
        total_yoctoseconds = int(round(Timestamp._YS_PER_NS * self.nanos))
        microsecond, remainder_yoctoseconds = divmod(total_yoctoseconds, Timestamp._YS_PER_US)
        femtosecond, remainder_yoctoseconds = divmod(remainder_yoctoseconds, Timestamp._YS_PER_FS)
        yoctosecond = remainder_yoctoseconds

        # Start with UTC
        dt = ht_datetime.fromtimestamp(self.seconds, timezone.utc)
        # Add in precision
        dt = dt.replace(microsecond=microsecond, femtosecond=femtosecond, yoctosecond=yoctosecond)
        # Then convert to requested timezone
        return dt.astimezone(tz=tzinfo)
