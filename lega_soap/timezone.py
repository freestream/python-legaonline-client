from __future__ import annotations

import os
import datetime as dt
from zoneinfo import ZoneInfo


def get_default_tzinfo() -> dt.tzinfo:
    """
    Get the default timezone information for the application.

    This function attempts to determine the appropriate timezone in the following order:
    1. Uses the timezone specified in the 'TZ' environment variable if available
    2. Falls back to the system's local timezone
    3. Defaults to UTC if neither of the above can be determined

    Returns:
        dt.tzinfo: A timezone info object representing the default timezone.
            Returns ZoneInfo from TZ environment variable if set and valid,
            otherwise returns the local timezone, or UTC as a last resort.

    Examples:
        >>> # With TZ environment variable set
        >>> os.environ['TZ'] = 'America/New_York'
        >>> tz = get_default_tzinfo()
        >>> # Returns ZoneInfo('America/New_York')
        
        >>> # Without TZ environment variable
        >>> del os.environ['TZ']
        >>> tz = get_default_tzinfo()
        >>> # Returns system local timezone or UTC
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
