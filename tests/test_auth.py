import pytest
from lega_soap.auth import AuthManager, Credentials
from lega_soap.exceptions import AuthError


class FakeService:
    def __init__(self):
        self._token = "TOKEN123"
        self.get_calls = 0
        self.validate_calls = 0
        self.valid = True

    def GetAuthToken(self, user_id, hash_):
        self.get_calls += 1
        return self._token

    def ValidateAuthToken(self, token):
        self.validate_calls += 1
        return self.valid and token == self._token


def test_authenticate_sets_token():
    svc = FakeService()
    auth = AuthManager(svc, Credentials(user_id=1, hash="h"))
    token = auth.authenticate()
    assert token == "TOKEN123"
    assert auth.token == "TOKEN123"
    assert svc.get_calls == 1


def test_token_property_requires_auth():
    svc = FakeService()
    auth = AuthManager(svc, Credentials(user_id=1, hash="h"))
    with pytest.raises(AuthError):
        _ = auth.token


def test_ensure_valid_token_uses_validate_when_present():
    svc = FakeService()
    auth = AuthManager(svc, Credentials(user_id=1, hash="h"))
    auth.authenticate()
    token = auth.ensure_valid_token()
    assert token == "TOKEN123"
    assert svc.validate_calls >= 1


def test_ensure_valid_token_reauth_when_invalid():
    svc = FakeService()
    auth = AuthManager(svc, Credentials(user_id=1, hash="h"))
    auth.authenticate()
    svc.valid = False
    token = auth.ensure_valid_token()
    assert token == "TOKEN123"
    assert svc.get_calls == 2  # authenticate called again
