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
    def test_sanitize_non_datetime_objects_unchanged():
        tz = ZoneInfo("Europe/Stockholm")
        assert sanitize_object("string", tz) == "string"
        assert sanitize_object(123, tz) == 123
        assert sanitize_object(None, tz) is None
        assert sanitize_object(45.67, tz) == 45.67


    def test_sanitize_empty_containers():
        tz = ZoneInfo("Europe/Stockholm")
        assert sanitize_object({}, tz) == {}
        assert sanitize_object([], tz) == []
        assert sanitize_object((), tz) == ()


    def test_sanitize_deeply_nested_structures():
        tz = ZoneInfo("Europe/Stockholm")
        naive = dt.datetime(2026, 2, 4, 12, 0, 0)
        data = {
            "level1": {
                "level2": {
                    "level3": [naive, {"dt": naive}]
                }
            }
        }
        out = sanitize_object(data, tz)
        assert out["level1"]["level2"]["level3"][0].tzinfo == tz
        assert out["level1"]["level2"]["level3"][1]["dt"].tzinfo == tz


    def test_sanitize_mixed_container_types():
        tz = ZoneInfo("Europe/Stockholm")
        naive = dt.datetime(2026, 2, 4, 12, 0, 0)
        data = [{"tuple": (naive, [naive])}, naive]
        out = sanitize_object(data, tz)
        assert out[0]["tuple"][0].tzinfo == tz
        assert out[0]["tuple"][1][0].tzinfo == tz
        assert out[1].tzinfo == tz


    def test_sanitize_preserves_datetime_values():
        tz = ZoneInfo("Europe/Stockholm")
        naive = dt.datetime(2026, 2, 4, 12, 30, 45)
        out = sanitize_object(naive, tz)
        assert out.year == 2026
        assert out.month == 2
        assert out.day == 4
        assert out.hour == 12
        assert out.minute == 30
        assert out.second == 45

