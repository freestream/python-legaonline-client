from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.financial_account_setting import FinancialAccountSettingService


def test_get_account_setting_calls_GetAccountSetting(zeep_service, tzinfo) -> None:
    svc = FinancialAccountSettingService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(svc.get_account_setting)
    svc.get_account_setting(**kwargs)

    assert zeep_service.calls
    name, args, _ = zeep_service.calls[0]
    assert name == "GetAccountSetting"
    assert args[0] == "TOKEN123"


def test_set_empty_account_setting_calls_SetEmptyAccountSetting(zeep_service, tzinfo) -> None:
    svc = FinancialAccountSettingService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(svc.set_empty_account_setting)
    svc.set_empty_account_setting(**kwargs)

    assert zeep_service.calls
    name, args, _ = zeep_service.calls[0]
    assert name == "SetEmptyAccountSetting"
    assert args[0] == "TOKEN123"
