import datetime as dt
from zoneinfo import ZoneInfo

import lega_soap.services.base as base_mod
from lega_soap.client import Client
from lega_soap.auth import Credentials
from lega_soap.query import FilterSpec, SortSpec


class FakeZeepService:
    def __init__(self):
        self.calls = []
        self._token = "TOKEN123"

    def GetAuthToken(self, user_id, hash_):
        return self._token

    def ValidateAuthToken(self, token):
        return token == self._token

    def GetCustomer(self, authToken, sorting, filtering, includeAttributes):
        self.calls.append((authToken, sorting, filtering, includeAttributes))
        return {"customers": [], "ts": dt.datetime(2026, 2, 4, 12, 0, 0)}


class FakeZeepClient:
    def __init__(self, service):
        self.service = service


def test_client_authenticates_on_init_and_sets_services(monkeypatch):
    service = FakeZeepService()
    zeep_client = FakeZeepClient(service)

    # Patch serialize_object => identity för enklare assert
    monkeypatch.setattr(base_mod, "serialize_object", lambda x: x)

    tz = ZoneInfo("Europe/Stockholm")
    client = Client(
        creds=Credentials(user_id=1, hash="h"),
        zeep_client=zeep_client,
        authenticate_on_init=True,
        tzinfo=tz,
    )

    assert client.auth.token == "TOKEN123"
    assert client.customers is not None


def test_get_customer_uses_filter_sort_objects_and_injects_token(monkeypatch):
    service = FakeZeepService()
    zeep_client = FakeZeepClient(service)

    monkeypatch.setattr(base_mod, "serialize_object", lambda x: x)

    tz = ZoneInfo("Europe/Stockholm")
    client = Client(
        creds=Credentials(user_id=1, hash="h"),
        zeep_client=zeep_client,
        authenticate_on_init=True,
        tzinfo=tz,
    )

    filters = FilterSpec.from_tuples(("Status", "active", "eq"))
    sorts = SortSpec.from_tuples(("Status", "asc"))

    result = client.customers.get_customer(
        sorting=sorts,
        filtering=filters,
        include_attributes=False,
    )

    # Kontrollera SOAP-call
    assert len(service.calls) == 1
    authToken, sorting_xml, filtering_xml, includeAttributes = service.calls[0]
    assert authToken == "TOKEN123"
    assert sorting_xml.startswith("<Sorting>")
    assert filtering_xml.startswith("<Filtering>")
    assert includeAttributes is False

    # Kontrollera sanitize på response datetime
    assert result["ts"].tzinfo == tz
