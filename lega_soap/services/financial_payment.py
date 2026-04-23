from __future__ import annotations

from decimal import Decimal
from typing import Optional

from ..types import SoapResponse
from .base import BaseService


class FinancialPaymentService(BaseService):
    """
    Service class for payment and balance operations in the Financial API.

    Provides methods for registering payments against invoices and setting invoice
    balances, both via structured objects and raw XML strings.

    Attributes:
        __slots__: Empty tuple indicating no additional instance attributes.

    Note:
        This class inherits from BaseService which provides the underlying _call method
        for executing authenticated SOAP operations.
    """

    __slots__ = ()

    def add_payment(
        self,
        invoice_id: Optional[int] = None,
        sum: Optional[Decimal] = None,
        payment_type_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Register a payment against an invoice.

        Args:
            invoice_id (Optional[int], optional): The ID of the invoice to register
                the payment against. Defaults to None.
            sum (Optional[Decimal], optional): The payment amount. Defaults to None.
            payment_type_id (Optional[int], optional): The ID of the payment type.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service (void operation).
        """
        record = {k: v for k, v in {
            "InvoiceID": invoice_id,
            "Sum": sum,
            "PaymentTypeID": payment_type_id,
        }.items() if v is not None}
        return self._call("AddPayment", payment={"Payment": [record]})

    def add_payment_xml(self, payment: Optional[str] = None) -> SoapResponse:
        """
        Register a payment against an invoice using raw XML.

        Args:
            payment (Optional[str], optional): The payment data serialized as an XML
                string. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service (void operation).
        """
        return self._call("AddPaymentXml", payment=payment)

    def set_balance(
        self,
        invoice_id: Optional[int] = None,
        sum: Optional[Decimal] = None,
        payment_type_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set the balance for an invoice.

        Args:
            invoice_id (Optional[int], optional): The ID of the invoice whose balance
                should be set. Defaults to None.
            sum (Optional[Decimal], optional): The balance amount to set. Defaults to None.
            payment_type_id (Optional[int], optional): The ID of the payment type.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service (void operation).
        """
        record = {k: v for k, v in {
            "InvoiceID": invoice_id,
            "Sum": sum,
            "PaymentTypeID": payment_type_id,
        }.items() if v is not None}
        return self._call("SetBalance", payment={"Payment": [record]})

    def set_balance_xml(self, payment: Optional[str] = None) -> SoapResponse:
        """
        Set the balance for an invoice using raw XML.

        Args:
            payment (Optional[str], optional): The payment data serialized as an XML
                string. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service (void operation).
        """
        return self._call("SetBalanceXml", payment=payment)
