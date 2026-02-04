from __future__ import annotations

import os
import datetime as dt
from zoneinfo import ZoneInfo


def get_default_tzinfo() -> dt.tzinfo:
    """
    Default timezone selection:

    1) If environment variable TZ is set to an IANA name, use it (e.g. "Europe/Stockholm")
    2) Else use OS local timezone via datetime.now().astimezone().tzinfo
    3) Else fallback to UTC
    """
    tz_env = os.environ.get("TZ")
    if tz_env:
        try:
            return ZoneInfo(tz_env)
        except Exception:
            pass

    local_tz = dt.datetime.now().astimezone().tzinfo
    if local_tz is not None:
        return local_tz

    return dt.timezone.utc
