from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.customer import CustomerService


def test_customer_delete_customer_contact_calls_DeleteCustomerContact(zeep_service, tzinfo) -> None:
    svc = CustomerService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(getattr(svc, "delete_customer_contact"))
    getattr(svc, "delete_customer_contact")(**kwargs)

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "DeleteCustomerContact"
    assert args[0] == "TOKEN123"


def test_customer_get_customer_v6_calls_GetCustomerV6(zeep_service, tzinfo) -> None:
    svc = CustomerService(zeep_service, FakeAuth(), tzinfo)
    svc.get_customer_v6()

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetCustomerV6"
    assert args[0] == "TOKEN123"


def test_customer_get_customer_v6_xml_calls_GetCustomerV6Xml(zeep_service, tzinfo) -> None:
    svc = CustomerService(zeep_service, FakeAuth(), tzinfo)
    svc.get_customer_v6_xml()

    assert zeep_service.calls, "Expected at least one SOAP call"
    name, args, _ = zeep_service.calls[0]
    assert name == "GetCustomerV6Xml"
    assert args[0] == "TOKEN123"
