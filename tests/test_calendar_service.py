from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.calendar import CalendarService


def test_calendar_get_day_calendar_data_calls_GetDayCalendarData(zeep_service, tzinfo) -> None:
    svc = CalendarService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "get_day_calendar_data"))
    getattr(svc, "get_day_calendar_data")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetDayCalendarData"
    assert args[0] == "TOKEN123"
