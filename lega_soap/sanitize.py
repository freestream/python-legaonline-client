from __future__ import annotations

from typing import Any
import datetime as dt


def sanitize_object(obj: Any, target_tz: dt.tzinfo) -> Any:
    """
    Recursively sanitize an object by ensuring all datetime objects have the correct timezone.

    This function traverses through nested data structures (dictionaries, lists, tuples) and
    processes datetime objects to ensure they have the specified timezone. If a datetime is
    naive (no timezone), it assigns the target timezone. If it already has a timezone, it
    converts it to the target timezone.

    Args:
        obj (Any): The object to sanitize. Can be a dict, list, tuple, datetime, or any other type.
        target_tz (dt.tzinfo): The target timezone to apply to datetime objects.

    Returns:
        Any: A sanitized copy of the input object with all datetime objects adjusted to the
             target timezone. Non-datetime objects are returned unchanged. Container types
             (dict, list, tuple) are recursively processed.

    Examples:
        >>> import datetime as dt
        >>> from zoneinfo import ZoneInfo
        >>> target_tz = ZoneInfo("Europe/Stockholm")
        >>> naive_dt = dt.datetime(2023, 1, 1, 12, 0, 0)
        >>> sanitize_object(naive_dt, target_tz)
        datetime.datetime(2023, 1, 1, 12, 0, 0, tzinfo=ZoneInfo('Europe/Stockholm'))
        
        >>> data = {"timestamp": naive_dt, "values": [naive_dt, "text"]}
        >>> sanitize_object(data, target_tz)
        {'timestamp': datetime.datetime(2023, 1, 1, 12, 0, 0, tzinfo=ZoneInfo('Europe/Stockholm')), 
         'values': [datetime.datetime(2023, 1, 1, 12, 0, 0, tzinfo=ZoneInfo('Europe/Stockholm')), 'text']}
    """
    if isinstance(obj, dict):
        return {k: sanitize_object(v, target_tz) for k, v in obj.items()}
    if isinstance(obj, list):
        return [sanitize_object(x, target_tz) for x in obj]
    if isinstance(obj, tuple):
        return tuple(sanitize_object(x, target_tz) for x in obj)
    if isinstance(obj, dt.datetime):
        if obj.tzinfo is None:
            return obj.replace(tzinfo=target_tz)
        return obj.astimezone(target_tz)
    return obj
