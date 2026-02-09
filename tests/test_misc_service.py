from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.misc import MiscService


def test_misc_get_company_logo_url_calls_GetCompanyLogoUrl(zeep_service, tzinfo) -> None:
    svc = MiscService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_company_logo_url"))
    getattr(svc, "get_company_logo_url")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetCompanyLogoUrl"
    assert args[0] == "TOKEN123"
