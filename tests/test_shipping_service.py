from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.shipping import ShippingService


def test_shipping_get_shipping_method_calls_GetShippingMethod(zeep_service, tzinfo) -> None:
    svc = ShippingService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_shipping_method"))
    getattr(svc, "get_shipping_method")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetShippingMethod"
    assert args[0] == "TOKEN123"
