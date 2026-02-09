
from zoneinfo import ZoneInfo

from lega_soap.client import Client
from lega_soap.auth import Credentials
from lega_soap.exceptions import AuthError
from lega_soap.services.customer import CustomerService


class FakeZeepService:
    def __init__(self, token: str = "TOKEN123") -> None:
        self._token = token
        self.get_auth_calls = 0
        self.validate_calls = 0

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
    service = FakeZeepService("TOKEN123")
    client = Client(
        creds=Credentials(user_id=1, hash="h"),
        zeep_client=FakeZeepClient(service),
        authenticate_on_init=True,
        tzinfo=ZoneInfo("Europe/Stockholm"),
    )

    assert service.get_auth_calls == 1
    assert client.auth.token == "TOKEN123"
    assert isinstance(client.customers, CustomerService)


def test_client_does_not_authenticate_when_disabled() -> None:
    service = FakeZeepService("TOKEN123")
    client = Client(
        creds=Credentials(user_id=1, hash="h"),
        zeep_client=FakeZeepClient(service),
        authenticate_on_init=False,
    )

    assert service.get_auth_calls == 0
    try:
        _ = client.auth.token
        assert False, "Expected AuthError when token not set"
    except AuthError:
        pass
