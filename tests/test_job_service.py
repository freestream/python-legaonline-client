from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.job import JobService


def test_job_get_job_calls_GetJob(zeep_service, tzinfo) -> None:
    svc = JobService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_job"))
    getattr(svc, "get_job")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetJob"
    assert args[0] == "TOKEN123"
