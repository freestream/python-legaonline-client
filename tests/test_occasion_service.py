from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.occasion import OccasionService


def test_occasion_activate_occasion_calls_ActivateOccasion(zeep_service, tzinfo) -> None:
    svc = OccasionService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "activate_occasion"))
    getattr(svc, "activate_occasion")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "ActivateOccasion"
    assert args[0] == "TOKEN123"
