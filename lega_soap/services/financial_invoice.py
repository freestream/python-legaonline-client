from __future__ import annotations

import datetime as dt
from typing import Optional

from ..query import FilterSpec, IntListSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService


class FinancialInvoiceService(BaseService):
    """
    Service class for invoice-related SOAP operations in the Financial API.

    Provides methods for retrieving invoices in multiple schema versions (V1–V8),
    managing invoice state (exported flag, invoice number, invalidation), retrieving
    unpaid invoices, and fetching transaction data.

    Attributes:
        __slots__: Empty tuple indicating no additional instance attributes.

    Note:
        This class inherits from BaseService which provides the underlying _call method
        for executing authenticated SOAP operations.
    """

    __slots__ = ()

    def get_invoice(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records using the base invoice schema.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                Invoice objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoice", sort=sort_xml, filter=filter_xml)

    def get_invoice_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records in XML format using the base invoice schema.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing invoice data
                serialized as an XML string.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceXml", sort=sort_xml, filter=filter_xml)

    def get_invoice_v2(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records using the V2 schema.

        V2 extends the base schema with: ``InvoiceEmail``, ``UnitName``,
        ``InvoiceDate``, ``EdiReference``.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoiceV2 objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV2", sort=sort_xml, filter=filter_xml)

    def get_invoice_v2_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records in XML format using the V2 schema.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing V2 invoice data
                serialized as an XML string.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV2Xml", sort=sort_xml, filter=filter_xml)

    def get_invoice_v3(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records using the V3 schema.

        V3 extends V2 with: ``InvoiceDeliveryMethodID``, ``BookingNumbers``.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoiceV3 objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV3", sort=sort_xml, filter=filter_xml)

    def get_invoice_v3_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records in XML format using the V3 schema.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing V3 invoice data
                serialized as an XML string.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV3Xml", sort=sort_xml, filter=filter_xml)

    def get_invoice_v4(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records using the V4 schema.

        V4 extends V3 with: ``ExtraFields`` (key/value pairs per invoice).

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoiceV4 objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV4", sort=sort_xml, filter=filter_xml)

    def get_invoice_v4_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records in XML format using the V4 schema.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing V4 invoice data
                serialized as an XML string.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV4Xml", sort=sort_xml, filter=filter_xml)

    def get_invoice_v5(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records using the V5 schema.

        V5 extends V4 with: ``CustomerID``, ``InvoiceCustomerNumber``.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoiceV5 objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV5", sort=sort_xml, filter=filter_xml)

    def get_invoice_v5_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records in XML format using the V5 schema.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing V5 invoice data
                serialized as an XML string.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV5Xml", sort=sort_xml, filter=filter_xml)

    def get_invoice_v6(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records using the V6 schema.

        V6 uses the same header fields as V5 but invoice rows use InvoiceRowV2,
        which adds: ``StartDate``, ``EndDate``, ``Cost`` per row.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoiceV6 objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV6", sort=sort_xml, filter=filter_xml)

    def get_invoice_v6_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records in XML format using the V6 schema.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing V6 invoice data
                serialized as an XML string.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV6Xml", sort=sort_xml, filter=filter_xml)

    def get_invoice_v7(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records using the V7 schema.

        V7 uses the same header fields as V6 but invoice rows use InvoiceRowV3,
        which adds: ``ExtraFields`` (key/value pairs) per row.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoiceV7 objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV7", sort=sort_xml, filter=filter_xml)

    def get_invoice_v7_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records in XML format using the V7 schema.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing V7 invoice data
                serialized as an XML string.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV7Xml", sort=sort_xml, filter=filter_xml)

    def get_invoice_v8(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice records using the V8 schema.

        V8 uses the same fields as V7 but invoice rows use InvoiceRowV4, where
        ``VatPercent`` is typed as ``decimal`` instead of ``int``.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoiceV8 objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceV8", sort=sort_xml, filter=filter_xml)

    def get_invoice_customer_contact(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice customer contact records.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoiceCustomerContact objects.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceCustomerContact", sort=sort_xml, filter=filter_xml)

    def get_invoice_customer_contact_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve invoice customer contact records in XML format.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing invoice customer
                contact data serialized as an XML string.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetInvoiceCustomerContactXml", sort=sort_xml, filter=filter_xml)

    def get_invoice_transaction_data(
        self,
        invoice_ids: Optional[IntListSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve transaction data for the specified invoices.

        Args:
            invoice_ids (Optional[IntListSpec], optional): A list specification containing
                the IDs of the invoices whose transaction data should be retrieved.
                If None, no data will be returned. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing an
                InvoiceTransactionDataList with per-invoice data strings and any errors.
        """
        return self._call(
            "GetInvoiceTransactionData",
            invoiceIDs=invoice_ids.to_zeep() if invoice_ids else None,
        )

    def get_unpaid_invoice(self, from_date: dt.datetime) -> SoapResponse:
        """
        Retrieve invoices that have not been paid since a given date.

        Args:
            from_date (datetime.datetime): The earliest date from which to retrieve
                unpaid invoices.

        Returns:
            SoapResponse: The response from the SOAP service containing an array of
                InvoicePayment objects with invoice ID and invoice number.
        """
        return self._call("GetUnpaidInvoice", fromDate=from_date)

    def invalidate_invoice(self, invoice_id: int, notes: str) -> SoapResponse:
        """
        Invalidate an invoice.

        Args:
            invoice_id (int): The ID of the invoice to invalidate.
            notes (str): Notes explaining the reason for invalidation.

        Returns:
            SoapResponse: The response from the SOAP service containing a boolean
                indicating whether the invalidation was successful.
        """
        return self._call("InvalidateInvoice", invoiceID=invoice_id, notes=notes)

    def set_exported(self, invoice_id: int, exported: bool) -> SoapResponse:
        """
        Mark an invoice as exported or clear the exported flag.

        Args:
            invoice_id (int): The ID of the invoice to update.
            exported (bool): Whether the invoice should be marked as exported.

        Returns:
            SoapResponse: The response from the SOAP service (void operation).
        """
        return self._call("SetExported", invoiceID=invoice_id, exported=exported)

    def set_invoice_number(self, invoice_id: int, invoice_number: str) -> SoapResponse:
        """
        Set the invoice number for a specific invoice.

        Args:
            invoice_id (int): The ID of the invoice to update.
            invoice_number (str): The new invoice number to assign.

        Returns:
            SoapResponse: The response from the SOAP service (void operation).
        """
        return self._call("SetInvoiceNumber", invoiceID=invoice_id, invoiceNumber=invoice_number)
