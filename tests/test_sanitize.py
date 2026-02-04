import datetime as dt
from zoneinfo import ZoneInfo

from lega_soap.sanitize import sanitize_object


def test_sanitize_naive_datetime_attaches_tz():
    tz = ZoneInfo("Europe/Stockholm")
    naive = dt.datetime(2026, 2, 4, 12, 0, 0)  # naive
    out = sanitize_object(naive, tz)
    assert isinstance(out, dt.datetime)
    assert out.tzinfo is not None
    assert out.tzinfo == tz


def test_sanitize_aware_datetime_converts_tz():
    tz = ZoneInfo("Europe/Stockholm")
    utc = dt.timezone.utc
    aware = dt.datetime(2026, 2, 4, 10, 0, 0, tzinfo=utc)
    out = sanitize_object(aware, tz)
    assert out.tzinfo == tz


def test_sanitize_nested_structures():
    tz = ZoneInfo("Europe/Stockholm")
    data = {
        "a": [dt.datetime(2026, 2, 4, 12, 0, 0)],
        "b": ("x", dt.datetime(2026, 2, 4, 13, 0, 0)),
    }
    out = sanitize_object(data, tz)
    assert out["a"][0].tzinfo == tz
    assert out["b"][1].tzinfo == tz
