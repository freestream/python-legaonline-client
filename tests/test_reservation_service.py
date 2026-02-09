from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.reservation import ReservationService


def test_reservation_add_reservation_to_job_calls_AddReservationToJob(zeep_service, tzinfo) -> None:
    svc = ReservationService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "add_reservation_to_job"))
    getattr(svc, "add_reservation_to_job")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "AddReservationToJob"
    assert args[0] == "TOKEN123"
