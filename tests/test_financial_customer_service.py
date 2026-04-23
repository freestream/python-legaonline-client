from tests.helpers import FakeAuth, build_required_kwargs

from lega_soap.services.financial_customer import FinancialCustomerService


def test_get_customer_transaction_data_calls_GetCustomerTransactionData(zeep_service, tzinfo) -> None:
    svc = FinancialCustomerService(zeep_service, FakeAuth(), tzinfo)
    kwargs = build_required_kwargs(svc.get_customer_transaction_data)
    svc.get_customer_transaction_data(**kwargs)

    assert zeep_service.calls
    name, args, _ = zeep_service.calls[0]
    assert name == "GetCustomerTransactionData"
    assert args[0] == "TOKEN123"


def test_get_customer_calls_GetCustomer(zeep_service, tzinfo) -> None:
    svc = FinancialCustomerService(zeep_service, FakeAuth(), tzinfo)
    svc.get_customer()

    assert zeep_service.calls
    name, args, _ = zeep_service.calls[0]
    assert name == "GetCustomer"
    assert args[0] == "TOKEN123"


def test_get_customer_group_calls_GetCustomerGroup(zeep_service, tzinfo) -> None:
    svc = FinancialCustomerService(zeep_service, FakeAuth(), tzinfo)
    svc.get_customer_group()

    assert zeep_service.calls
    name, args, _ = zeep_service.calls[0]
    assert name == "GetCustomerGroup"
    assert args[0] == "TOKEN123"
