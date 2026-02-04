from __future__ import annotations

from typing import Any
import datetime as dt


def sanitize_object(obj: Any, target_tz: dt.tzinfo) -> Any:
    """
    Recursively sanitizes an object by converting all datetime.datetime instances to target_tz.

    - If tzinfo is missing: assume the datetime is in target_tz and attach it.
      Note: attaching tzinfo to naive datetimes can be ambiguous around DST transitions.
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
