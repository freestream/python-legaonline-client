import datetime as dt
from zoneinfo import ZoneInfo

import lega_soap.services.base as base_mod
from lega_soap.services.base import BaseService


class FakeAuth:
    def __init__(self, token="TOK"):
        self._token = token
        self.calls = 0

    def ensure_valid_token(self):
        self.calls += 1
        return self._token


class FakeZeepService:
    def __init__(self):
        self.calls = []

    def SomeMethod(self, authToken, **kwargs):
        self.calls.append((authToken, kwargs))
        # Returnera ett "zeep-ish" objekt, vi patchar serialize_object ändå
        return {"dt": dt.datetime(2026, 2, 4, 12, 0, 0), "ok": True}


def test_base_service_call_injects_token_filters_kwargs_and_sanitizes(monkeypatch):
    tz = ZoneInfo("Europe/Stockholm")
    zeep_service = FakeZeepService()
    auth = FakeAuth(token="ABC123")

    # Patcha serialize_object så att vi vet exakt vad som går in i sanitizer
    def fake_serialize(obj):
        return obj

    monkeypatch.setattr(base_mod, "serialize_object", fake_serialize)

    svc = BaseService(zeep_service, auth, tz)

    result = svc._call(
        "SomeMethod",
        a=1,
        b=None,   # ska filtreras bort
        c="",     # ska filtreras bort
        d=[],     # ska filtreras bort
        e={},     # ska filtreras bort
        f="x",
    )

    # Verifiera token-injektion och filtrering
    assert zeep_service.calls[0][0] == "ABC123"
    sent_kwargs = zeep_service.calls[0][1]
    assert sent_kwargs == {"a": 1, "f": "x"}

    # Verifiera sanering av datetime
    assert result["ok"] is True
    assert result["dt"].tzinfo == tz
