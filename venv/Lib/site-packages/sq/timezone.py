import calendar
import datetime
import time

import pytz

ZERO = datetime.timedelta(0)
HOUR = datetime.timedelta(hours=1)


def as_timestamp(value, precision=1000):
    """Convert a datetime, date or time object to a UNIX
    timestamp.
    """
    d = 0
    t = 0
    offset = 0
    if isinstance(value, (datetime.datetime, datetime.date)):
        d = int(calendar.timegm(value.timetuple()) * precision)
    elif isinstance(value, datetime.time):
        t = int((value.hour * 60 * 60 * precision)\
            + (value.minute * 60 * precision)\
            + (value.second * precision)\
            + (value.microsecond / precision))
    else:
        raise TypeError("Invalid input type: %s" % repr(type(value)))

    if isinstance(value, (datetime.datetime, datetime.time)):
        tz = value.utcoffset()
        if tz is not None:
            offset = tz.total_seconds() * precision

    return int(d + t + offset)


def now():
    return int(time.time() * 1000)


class utc(datetime.tzinfo):
    """UTC"""

    def __init__(self, offset):
        self.hours = float(offset) / 3600
        self.offset = datetime.timedelta(seconds=offset)

    def utcoffset(self, dt):
        return self.offset

    def tzname(self, dt):
        return "UTC+%f" % self.hours

    def dst(self, dt):
        return self.offset


UTC = utc(0)


def as_datetime(value, timezone=None):
    """Convert a timestamp, in milliseconds from the UNIX
    epoch, to a :class:`datetime.datetime` object.
    """
    tzinfo = None
    if timezone is not None:
        try:
            tzinfo = pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            raise ValueError(timezone)

    return datetime.datetime.fromtimestamp(value / 1000, tzinfo)
