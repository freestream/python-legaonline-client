import datetime as dt

from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.financial_invoice import FinancialInvoiceService


def _make_svc(zeep_service, tzinfo):
    return FinancialInvoiceService(zeep_service, FakeAuth(), tzinfo)


def _assert_called(zeep_service, expected_name):
    assert zeep_service.calls
    name, args, _ = zeep_service.calls[0]
    assert name == expected_name
    assert args[0] == "TOKEN123"


def test_get_invoice_calls_GetInvoice(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice()
    _assert_called(zeep_service, "GetInvoice")


def test_get_invoice_xml_calls_GetInvoiceXml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_xml()
    _assert_called(zeep_service, "GetInvoiceXml")


def test_get_invoice_v2_calls_GetInvoiceV2(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v2()
    _assert_called(zeep_service, "GetInvoiceV2")


def test_get_invoice_v2_xml_calls_GetInvoiceV2Xml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v2_xml()
    _assert_called(zeep_service, "GetInvoiceV2Xml")


def test_get_invoice_v3_calls_GetInvoiceV3(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v3()
    _assert_called(zeep_service, "GetInvoiceV3")


def test_get_invoice_v3_xml_calls_GetInvoiceV3Xml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v3_xml()
    _assert_called(zeep_service, "GetInvoiceV3Xml")


def test_get_invoice_v4_calls_GetInvoiceV4(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v4()
    _assert_called(zeep_service, "GetInvoiceV4")


def test_get_invoice_v4_xml_calls_GetInvoiceV4Xml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v4_xml()
    _assert_called(zeep_service, "GetInvoiceV4Xml")


def test_get_invoice_v5_calls_GetInvoiceV5(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v5()
    _assert_called(zeep_service, "GetInvoiceV5")


def test_get_invoice_v5_xml_calls_GetInvoiceV5Xml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v5_xml()
    _assert_called(zeep_service, "GetInvoiceV5Xml")


def test_get_invoice_v6_calls_GetInvoiceV6(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v6()
    _assert_called(zeep_service, "GetInvoiceV6")


def test_get_invoice_v6_xml_calls_GetInvoiceV6Xml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v6_xml()
    _assert_called(zeep_service, "GetInvoiceV6Xml")


def test_get_invoice_v7_calls_GetInvoiceV7(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v7()
    _assert_called(zeep_service, "GetInvoiceV7")


def test_get_invoice_v7_xml_calls_GetInvoiceV7Xml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v7_xml()
    _assert_called(zeep_service, "GetInvoiceV7Xml")


def test_get_invoice_v8_calls_GetInvoiceV8(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_v8()
    _assert_called(zeep_service, "GetInvoiceV8")


def test_get_invoice_customer_contact_calls_GetInvoiceCustomerContact(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_customer_contact()
    _assert_called(zeep_service, "GetInvoiceCustomerContact")


def test_get_invoice_customer_contact_xml_calls_GetInvoiceCustomerContactXml(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_invoice_customer_contact_xml()
    _assert_called(zeep_service, "GetInvoiceCustomerContactXml")


def test_get_invoice_transaction_data_calls_GetInvoiceTransactionData(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    kwargs = build_required_kwargs(svc.get_invoice_transaction_data)
    svc.get_invoice_transaction_data(**kwargs)
    _assert_called(zeep_service, "GetInvoiceTransactionData")


def test_get_unpaid_invoice_calls_GetUnpaidInvoice(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.get_unpaid_invoice(from_date=dt.datetime(2026, 1, 1))
    _assert_called(zeep_service, "GetUnpaidInvoice")


def test_invalidate_invoice_calls_InvalidateInvoice(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.invalidate_invoice(invoice_id=1, notes="test")
    _assert_called(zeep_service, "InvalidateInvoice")


def test_set_exported_calls_SetExported(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.set_exported(invoice_id=1, exported=True)
    _assert_called(zeep_service, "SetExported")


def test_set_invoice_number_calls_SetInvoiceNumber(zeep_service, tzinfo) -> None:
    svc = _make_svc(zeep_service, tzinfo)
    svc.set_invoice_number(invoice_id=1, invoice_number="INV-001")
    _assert_called(zeep_service, "SetInvoiceNumber")
