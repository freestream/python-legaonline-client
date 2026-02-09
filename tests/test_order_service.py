from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.order import OrderService


def test_order_calculate_price_calls_CalculatePrice(zeep_service, tzinfo) -> None:
    svc = OrderService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "calculate_price"))
    getattr(svc, "calculate_price")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "CalculatePrice"
    assert args[0] == "TOKEN123"
