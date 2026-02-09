from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.report import ReportService


def test_report_get_printer_profile_calls_GetPrinterProfile(zeep_service, tzinfo) -> None:
    svc = ReportService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_printer_profile"))
    getattr(svc, "get_printer_profile")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetPrinterProfile"
    assert args[0] == "TOKEN123"
