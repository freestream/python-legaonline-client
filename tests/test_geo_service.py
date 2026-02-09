from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.geo import GeoService


def test_geo_get_countries_calls_GetCountries(zeep_service, tzinfo) -> None:
    svc = GeoService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_countries"))
    getattr(svc, "get_countries")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetCountries"
    assert args[0] == "TOKEN123"
