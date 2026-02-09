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
