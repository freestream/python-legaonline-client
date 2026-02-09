from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.availability import AvailabilityService


def test_availability_get_availability_calls_GetAvailability(zeep_service, tzinfo) -> None:
    svc = AvailabilityService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_availability"))
    getattr(svc, "get_availability")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetAvailability"
    assert args[0] == "TOKEN123"
