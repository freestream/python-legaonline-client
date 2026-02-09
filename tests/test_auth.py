
from lega_soap.auth import AuthManager, Credentials
from lega_soap.exceptions import AuthError


class FakeZeepService:
    def __init__(self, token: str = "TOKEN123", valid: bool = True) -> None:
        self.token = token
        self.valid = valid
        self.get_auth_calls = 0
        self.validate_calls = 0

    def GetAuthToken(self, user_id: int, hash_: str) -> str:
        self.get_auth_calls += 1
        return self.token

    def ValidateAuthToken(self, token: str) -> bool:
        self.validate_calls += 1
        return self.valid and token == self.token


def test_authenticate_sets_token() -> None:
    svc = FakeZeepService()
    auth = AuthManager(svc, Credentials(user_id=1, hash="h"))
    token = auth.authenticate()

    assert token == "TOKEN123"
    assert auth.token == "TOKEN123"
    assert svc.get_auth_calls == 1


def test_token_property_raises_before_authenticate() -> None:
    svc = FakeZeepService()
    auth = AuthManager(svc, Credentials(user_id=1, hash="h"))
    try:
        _ = auth.token
        assert False, "Expected AuthError"
    except AuthError:
        pass


def test_ensure_valid_token_reauthenticates_if_invalid() -> None:
    svc = FakeZeepService(valid=False)
    auth = AuthManager(svc, Credentials(user_id=1, hash="h"))
    token = auth.ensure_valid_token()
    assert token == "TOKEN123"
    assert svc.get_auth_calls >= 1
