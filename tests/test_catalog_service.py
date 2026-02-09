from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.catalog import CatalogService


def test_catalog_get_attribute_calls_GetAttribute(zeep_service, tzinfo) -> None:
    svc = CatalogService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_attribute"))
    getattr(svc, "get_attribute")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetAttribute"
    assert args[0] == "TOKEN123"
