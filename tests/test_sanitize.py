
import datetime as dt
from collections import deque
from zoneinfo import ZoneInfo
from unittest.mock import MagicMock

from lega_soap.sanitize import sanitize_object


def test_sanitize_converts_datetime_timezone() -> None:
    tz = ZoneInfo("Europe/Stockholm")
    d = {"ts": dt.datetime(2026, 2, 4, 12, 0, 0)}
    out = sanitize_object(d, tz)
    assert out["ts"].tzinfo == tz


def test_sanitize_extracts_raw_elements() -> None:
    from lxml import etree

    tz = ZoneInfo("Europe/Stockholm")

    number_elem = etree.fromstring("<ReservationNumber xmlns='http://www.legaonline.se/'>11161</ReservationNumber>")
    notes_elem = etree.fromstring("<InvoiceNotes xmlns='http://www.legaonline.se/'>Some note</InvoiceNotes>")
    nil_elem = etree.fromstring(
        "<ExternalReservationID xmlns='http://www.legaonline.se/'"
        " xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'"
        " xsi:nil='true'/>"
    )

    obj = {
        "ReservationID": 1,
        "ReservationNumber": None,
        "InvoiceNotes": None,
        "ExternalReservationID": None,
        "_raw_elements": deque([nil_elem, number_elem, notes_elem]),
    }

    out = sanitize_object(obj, tz)

    assert "_raw_elements" not in out
    assert out["ReservationNumber"] == "11161"
    assert out["InvoiceNotes"] == "Some note"
    assert out["ExternalReservationID"] is None  # xsi:nil preserved


def test_sanitize_does_not_overwrite_existing_values() -> None:
    from lxml import etree

    tz = ZoneInfo("Europe/Stockholm")
    elem = etree.fromstring("<ReservationID xmlns='http://www.legaonline.se/'>99</ReservationID>")

    obj = {"ReservationID": 42, "_raw_elements": deque([elem])}
    out = sanitize_object(obj, tz)

    assert out["ReservationID"] == 42  # existing non-null value not overwritten
