import datetime as dt
from zoneinfo import ZoneInfo

import lega_soap.services.base as base_mod
from lega_soap.services.reservation import ReservationService


class FakeAuth:
    def __init__(self, token: str = "TOKEN123") -> None:
        self._token = token

    def ensure_valid_token(self) -> str:
        return self._token


class FakeZeepService:
    def __init__(self) -> None:
        self.calls = []

    def CreateReservation(self, authToken, customerID, customerContactID):
        self.calls.append((authToken, customerID, customerContactID))
        return {"reservation_id": 999, "ts": dt.datetime(2026, 2, 4, 12, 0, 0)}


def test_create_reservation_injects_token_and_sanitizes(monkeypatch):
    monkeypatch.setattr(base_mod, "serialize_object", lambda x: x)

    tz = ZoneInfo("Europe/Stockholm")
    svc = ReservationService(FakeZeepService(), FakeAuth(), tz)

    result = svc.create_reservation(customer_id=1, customer_contact_id=2)

    assert result["reservation_id"] == 999
    assert result["ts"].tzinfo == tz
