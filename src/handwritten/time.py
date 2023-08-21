import ctypes
import functools
from datetime import datetime, timezone

@functools.total_ordering
class AbsoluteTime(ctypes.Structure):
    # Please visit ni.com/info and enter the Info Code NI_BTF for detailed information.
    # The summary is:
    #    * lsb - positive fractions (2^-64) of a second
    #    * msb - number of whole seconds since 12am, Friday, January 1, 1904, UTC

    _pack_ = 4
    _fields_ = [("lsb", ctypes.c_uint64), ("msb", ctypes.c_int64)]

    BIAS_FROM_1970_EPOCH = 2082844800
    NUM_SUBSECONDS = 2 ** 64
    NUM_MICROSECONDS = 1000000

    @classmethod
    def from_datetime(cls, dt):
        utc_dt = dt.astimezone(tz=timezone.utc)

        # First, calculate whole seconds by converting from the 1970 to 1904 epoch.
        timestamp_1970_epoch = utc_dt.timestamp()
        was_negative = timestamp_1970_epoch < 0
        timestamp_1904_epoch = int(timestamp_1970_epoch + AbsoluteTime.BIAS_FROM_1970_EPOCH)

        # Our bias is positive, so our sign should only change if we were previously negative.
        is_negative = timestamp_1904_epoch < 0
        if is_negative != was_negative and not was_negative:
            raise OverflowError(f"Can't represent {dt.isoformat()} in AbsoluteTime (1904 epoch)")

        # Finally, convert the microseconds to subseconds.
        lsb = int(round(AbsoluteTime.NUM_SUBSECONDS * utc_dt.microsecond / AbsoluteTime.NUM_MICROSECONDS))

        return AbsoluteTime(lsb=lsb, msb=timestamp_1904_epoch)

    def to_datetime(self, tzinfo=timezone.utc):
        # First, calculate whole seconds by converting from the 1904 to 1970 epoch.
        timestamp_1904_epoch = self.msb
        was_positive = timestamp_1904_epoch > 0
        timestamp_1970_epoch = int(timestamp_1904_epoch - AbsoluteTime.BIAS_FROM_1970_EPOCH)

        # Our bias is negative, so our sign should only change if we were previously positive.
        is_positive = timestamp_1970_epoch > 0
        if is_positive != was_positive and not was_positive:
            raise OverflowError(f"Can't represent {str(self)} in datetime (1970 epoch)")

        # Finally, convert the subseconds to microseconds.
        microsecond = int(round(AbsoluteTime.NUM_MICROSECONDS * self.lsb / AbsoluteTime.NUM_SUBSECONDS))

        # Start with UTC
        dt = datetime.fromtimestamp(timestamp_1970_epoch, timezone.utc)
        dt = dt.replace(microsecond=microsecond)
        # Then convert to what was requested
        return dt.astimezone(tz=tzinfo)

    def __str__(self):
        return f"AbsoluteTime(lsb=0x{self.lsb:x}, msb=0x{self.msb:x})"

    def __eq__(self, other):
        return self.msb == other.msb and self.lsb == other.lsb

    def __lt__(self, other):
        if self.msb == other.msb:
            return self.lsb < other.lsb
        else:
            return self.msb < other.msb