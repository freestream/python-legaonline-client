
import datetime as dt
from zoneinfo import ZoneInfo
from lega_soap.sanitize import sanitize_object


def test_sanitize_converts_datetime_timezone() -> None:
    tz = ZoneInfo("Europe/Stockholm")
    d = {"ts": dt.datetime(2026, 2, 4, 12, 0, 0)}
    out = sanitize_object(d, tz)
    assert out["ts"].tzinfo == tz
