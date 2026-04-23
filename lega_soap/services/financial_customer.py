from __future__ import annotations

from typing import Optional

from ..query import IntListSpec
from ..types import SoapResponse
from .customer import CustomerService


class FinancialCustomerService(CustomerService):
    """
    CustomerService extended with Financial API-specific operations.

    Inherits all customer get/set/group operations from CustomerService and adds
    GetCustomerTransactionData which is only available in the Financial API.

    Attributes:
        __slots__: Empty tuple indicating no additional instance attributes.

    Note:
        Methods inherited from CustomerService that do not exist in the Financial API
        WSDL (e.g. DeleteCustomer, SetCustomerContact) will raise ServiceError if called
        against a FinancialClient instance.
    """

    __slots__ = ()

    def get_customer_transaction_data(
        self,
        customer_ids: Optional[IntListSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve transaction data for the specified customers.

        Args:
            customer_ids (Optional[IntListSpec], optional): A list specification containing
                the IDs of the customers whose transaction data should be retrieved.
                If None, no data will be returned. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the customer
                transaction data as an XML string.
        """
        return self._call(
            "GetCustomerTransactionData",
            customerIDs=customer_ids.to_zeep() if customer_ids else None,
        )
