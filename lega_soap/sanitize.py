from __future__ import annotations

from typing import Any
import datetime as dt


def _extract_raw_elements(raw_elements: Any) -> dict:
    # Zeep puts unrecognised XML elements into _raw_elements as lxml Element objects.
    # Extract their text values so they are not silently dropped.
    result = {}
    try:
        from lxml.etree import QName
        XSI_NIL = "{http://www.w3.org/2001/XMLSchema-instance}nil"
        for elem in raw_elements:
            tag = QName(elem.tag).localname
            if elem.get(XSI_NIL) == "true":
                result[tag] = None
            else:
                result[tag] = elem.text
    except Exception:
        pass
    return result


def sanitize_object(obj: Any, target_tz: dt.tzinfo) -> Any:
    """
    Recursively sanitize an object by ensuring all datetime objects have the correct timezone.

    This function traverses through nested data structures (dictionaries, lists, tuples) and
    processes datetime objects to ensure they have the specified timezone. If a datetime is
    naive (no timezone), it assigns the target timezone. If it already has a timezone, it
    converts it to the target timezone.

    Dicts containing a ``_raw_elements`` key (a Zeep artefact for schema-unrecognised XML
    elements) are handled specially: the raw lxml elements are extracted into the dict and the
    ``_raw_elements`` key is removed from the output.

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
        raw = obj.get("_raw_elements")
        extracted = _extract_raw_elements(raw) if raw is not None else {}
        sanitized = {k: sanitize_object(v, target_tz) for k, v in obj.items() if k != "_raw_elements"}
        for k, v in extracted.items():
            if sanitized.get(k) is None:
                sanitized[k] = v
        return sanitized
    if isinstance(obj, list):
        return [sanitize_object(x, target_tz) for x in obj]
    if isinstance(obj, tuple):
        return tuple(sanitize_object(x, target_tz) for x in obj)
    if isinstance(obj, dt.datetime):
        if obj.tzinfo is None:
            return obj.replace(tzinfo=target_tz)
        return obj.astimezone(target_tz)
    return obj
