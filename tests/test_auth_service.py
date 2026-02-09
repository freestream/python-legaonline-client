
from tests.helpers import build_required_kwargs
from lega_soap.services.auth import AuthService


def test_auth_service_get_auth_token_noauth(zeep_service, tzinfo) -> None:
    svc = AuthService(zeep_service, tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_auth_token"))
    svc.get_auth_token(**kwargs)
    name, args, _ = zeep_service.calls[0]
    assert name == "GetAuthToken"


def test_auth_service_validate_auth_token_noauth(zeep_service, tzinfo) -> None:
    svc = AuthService(zeep_service, tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "validate_auth_token"))
    svc.validate_auth_token(**kwargs)
    name, args, _ = zeep_service.calls[0]
    assert name == "ValidateAuthToken"
