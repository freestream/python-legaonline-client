from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.integration import IntegrationService
from lega_soap.query import OrderInfoSpec


def test_integration_integration_create_miljobud_order_calls_IntegrationCreateMiljobudOrder(zeep_service, tzinfo) -> None:
    svc = IntegrationService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "integration_create_miljobud_order"))
    
    kwargs.pop("fleet_101_auth_token", None)
    kwargs.pop("order_info", None)
    
    # Provide required arguments for the method call
    getattr(svc, "integration_create_miljobud_order")(
        fleet_101_auth_token="dummy_token",
        order_info=OrderInfoSpec(reservation_id=1, message="test"),
        **kwargs
    )

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "IntegrationCreateMiljobudOrder"
    assert args[0] == "TOKEN123"
