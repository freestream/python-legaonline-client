import pytest
from zoneinfo import ZoneInfo

from lega_soap.client import Client
from lega_soap.auth import Credentials
from lega_soap.exceptions import AuthError
from lega_soap.services.customer import CustomerService


class FakeZeepService:
    def __init__(self, token: str = "TOKEN123") -> None:
        self._token = token
        self.get_auth_calls: int = 0
        self.validate_calls: int = 0

    def GetAuthToken(self, user_id: int, hash_: str) -> str:
        self.get_auth_calls += 1
        return self._token

    def ValidateAuthToken(self, token: str) -> bool:
        self.validate_calls += 1
        return token == self._token


class FakeZeepClient:
    def __init__(self, service: FakeZeepService) -> None:
        self.service = service


def test_client_authenticates_on_init_and_sets_services() -> None:
    service = FakeZeepService(token="TOKEN123")
    zeep_client = FakeZeepClient(service)

    tz = ZoneInfo("Europe/Stockholm")
    client = Client(
        creds=Credentials(user_id=1, hash="h"),
        zeep_client=zeep_client,
        authenticate_on_init=True,
        tzinfo=tz,
    )

    assert service.get_auth_calls == 1
    assert client.auth.token == "TOKEN123"

    assert client.tzinfo == tz
    assert isinstance(client.customers, CustomerService)


def test_client_does_not_authenticate_when_disabled() -> None:
    service = FakeZeepService(token="TOKEN123")
    zeep_client = FakeZeepClient(service)

    client = Client(
        creds=Credentials(user_id=1, hash="h"),
        zeep_client=zeep_client,
        authenticate_on_init=False,
    )

    assert service.get_auth_calls == 0

    with pytest.raises(AuthError):
        _ = client.auth.token

    assert isinstance(client.customers, CustomerService)
