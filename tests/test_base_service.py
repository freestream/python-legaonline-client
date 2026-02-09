
from lega_soap.services.base import BaseService
from lega_soap.exceptions import ServiceError


class BadService:
    pass


class Auth:
    def ensure_valid_token(self) -> str:
        return "TOKEN123"


def test_base_service_raises_on_missing_method(tzinfo) -> None:
    svc = BaseService(BadService(), Auth(), tzinfo)
    try:
        svc._call("NoSuchMethod")
        assert False, "Expected ServiceError"
    except ServiceError:
        pass
