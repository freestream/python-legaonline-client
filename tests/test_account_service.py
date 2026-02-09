from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.account import AccountService


def test_account_get_account_calls_GetAccount(zeep_service, tzinfo) -> None:
    svc = AccountService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_account"))
    getattr(svc, "get_account")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetAccount"
    assert args[0] == "TOKEN123"
