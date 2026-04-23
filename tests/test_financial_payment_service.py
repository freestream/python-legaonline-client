from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.financial_payment import FinancialPaymentService


def _make_svc(zeep_service, tzinfo):
    return FinancialPaymentService(zeep_service, FakeAuth(), tzinfo)


def _assert_called(zeep_service, expected_name):
    assert zeep_service.calls
    name, args, _ = zeep_service.calls[0]
    assert name == expected_name
    assert args[0] == "TOKEN123"


def test_add_payment_calls_AddPayment(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    kwargs = build_required_kwargs(svc.add_payment)
    svc.add_payment(**kwargs)
    _assert_called(zeep_service, "AddPayment")


def test_add_payment_xml_calls_AddPaymentXml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    kwargs = build_required_kwargs(svc.add_payment_xml)
    svc.add_payment_xml(**kwargs)
    _assert_called(zeep_service, "AddPaymentXml")


def test_set_balance_calls_SetBalance(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    kwargs = build_required_kwargs(svc.set_balance)
    svc.set_balance(**kwargs)
    _assert_called(zeep_service, "SetBalance")


def test_set_balance_xml_calls_SetBalanceXml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    kwargs = build_required_kwargs(svc.set_balance_xml)
    svc.set_balance_xml(**kwargs)
    _assert_called(zeep_service, "SetBalanceXml")
