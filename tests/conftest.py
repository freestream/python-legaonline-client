
import datetime as dt
from zoneinfo import ZoneInfo
import pytest

import lega_soap.services.base as base_mod


class RecordingZeepService:
    """A zeep.service stand-in that records any SOAP method call."""
    def __init__(self):
        self.calls = []

    def __getattr__(self, name):
        def _method(*args, **kwargs):
            self.calls.append((name, args, kwargs))
            return {"ok": True, "method": name, "ts": dt.datetime(2026, 2, 4, 12, 0, 0)}
        return _method


class FakeZeepClient:
    def __init__(self, service):
        self.service = service


@pytest.fixture()
def tzinfo():
    return ZoneInfo("Europe/Stockholm")


@pytest.fixture(autouse=True)
def patch_serialize_object(monkeypatch):
    monkeypatch.setattr(base_mod, "serialize_object", lambda x: x)
    yield


@pytest.fixture()
def zeep_service():
    return RecordingZeepService()
