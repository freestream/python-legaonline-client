from __future__ import annotations

import datetime as dt
from decimal import Decimal
from typing import Any, Optional

from ..types import SoapResponse
from ..query import FilterSpec, IntListSpec, SortSpec
from .base import BaseService


class CustomerService(BaseService):
    """
    Service class for managing customer-related SOAP operations.
    This class provides methods for creating, retrieving, updating, and deleting customer data,
    including customer contacts, attributes, shipping information, and group management through
    SOAP API calls.
    The service supports multiple versions of customer and contact operations (V2-V5) and offers
    both standard and XML-based data formats for flexibility in integration.
    Key Features:
        - Customer CRUD operations (Create, Read, Update, Delete)
        - Customer contact management with multiple versions
        - Customer attribute handling
        - Customer group operations
        - Shipping and pickup information management
        - Password management for customers and contacts
        - Master customer relationship management
        - Support for sorting and filtering across operations
        - XML and object-based data formats
        >>> from lega_soap.services.customer import CustomerService
        >>> service = CustomerService(client)
        >>> response = service.get_customer(
        ...     filtering=FilterSpec(field="status", value="active"),
        ...     sorting=SortSpec(field="name", order="asc")
    Attributes:
        __slots__: Empty tuple indicating no additional instance attributes.
    Note:
        This class inherits from BaseService which provides the underlying _call method
        for executing SOAP operations.
    """
    __slots__ = ()

    def delete_customer_contact(self, customer_contact_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Delete customer contact(s) from the system.

        Args:
            customer_contact_ids (Optional[IntListSpec], optional): A list specification containing
                the IDs of customer contacts to be deleted. If None, no contacts will be deleted.
                Defaults to None.

        Returns:
            SoapResponse: The SOAP response object containing the result of the delete operation.
        """
        return self._call("DeleteCustomerContact", customerContactIDs=customer_contact_ids.to_zeep() if customer_contact_ids else None)

    def delete_customer_contact_attribute(self, customer_contact_attribute_lnk_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Delete customer contact attributes.

        Args:
            customer_contact_attribute_lnk_ids (Optional[IntListSpec], optional): A list specification
                containing the IDs of customer contact attributes to delete. Defaults to None.

        Returns:
            SoapResponse: The SOAP response from the DeleteCustomerContactAttribute operation.
        """
        return self._call("DeleteCustomerContactAttribute", CustomerContactAttributeLnkIDs=customer_contact_attribute_lnk_ids.to_zeep() if customer_contact_attribute_lnk_ids else None)

    def get_customer(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing customer data.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomer", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_attribute(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve customer attributes from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the customer attribute data
                returned by the SOAP service.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerAttribute", sort=sort_xml, filter=filter_xml)

    def get_customer_attribute_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve customer attribute data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the customer attribute data in XML format.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerAttributeXml", sort=sort_xml, filter=filter_xml)

    def get_customer_contact(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer contact information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include additional attributes
                in the response. Defaults to None.

        Returns:
            SoapResponse: The response object containing customer contact information
                returned from the SOAP service.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerContact", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_contact_attribute(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve customer contact attributes from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                customer contact attribute data.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerContactAttribute", sort=sort_xml, filter=filter_xml)

    def get_customer_contact_attribute_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve customer contact attribute data in XML format.

        SOAP operation: GetCustomerContactAttributeXml
        WSDL params: sort, filter

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse containing XML data (as returned by the API).
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerContactAttributeXml", sort=sort_xml, filter=filter_xml)

    def get_customer_contact_v2(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer contacts (v2).

        SOAP operation: GetCustomerContactV2
        WSDL params: sort, filter, includeAttributes

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            include_attributes (bool): Include attribute data for each contact. Defaults to False.

        Returns:
            SoapResponse containing customer contact data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""

        return self._call(
            "GetCustomerContactV2",
            sort=sort_xml,
            filter=filter_xml,
            includeAttributes=include_attributes,
        )

    def get_customer_contact_v2_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer contacts (v2) in XML format.

        SOAP operation: GetCustomerContactV2Xml
        WSDL params: sort, filter, includeAttributes

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            include_attributes (bool): Include attribute data for each contact. Defaults to False.

        Returns:
            SoapResponse containing XML data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call(
            "GetCustomerContactV2Xml",
            sort=sort_xml,
            filter=filter_xml,
            includeAttributes=include_attributes,
        )

    def get_customer_contact_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer contacts in XML format.

        SOAP operation: GetCustomerContactXml
        WSDL params: sort, filter, includeAttributes

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            include_attributes (bool): Include attribute data for each contact. Defaults to False.

        Returns:
            SoapResponse containing XML data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call(
            "GetCustomerContactXml",
            sort=sort_xml,
            filter=filter_xml,
            includeAttributes=include_attributes,
        )

    def get_customer_group(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve customer group information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the customer group data returned
                from the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerGroup", sort=sort_xml, filter=filter_xml)

    def get_customer_group_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve customer group data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the customer group data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerGroupXml", sort=sort_xml, filter=filter_xml)

    def get_customer_shipping(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve customer shipping information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing customer shipping information
                returned by the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerShipping", sort=sort_xml, filter=filter_xml)

    def get_customer_shipping_and_pickup(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
    ) -> SoapResponse:
        """
        Retrieve customer shipping and pickup information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                customer shipping and pickup information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerShippingAndPickup", sort=sort_xml, filter=filter_xml)

    def get_customer_v2(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer data using the GetCustomerV2 SOAP operation.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing customer data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV2", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_v2_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer data in XML format using the GetCustomerV2Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing customer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV2Xml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_v3(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer information using the GetCustomerV3 SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the customer results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering customer results.
                If provided, will be converted to XML format. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The response from the GetCustomerV3 SOAP method containing customer data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV3", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_v3_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer data in XML format using the GetCustomerV3Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The response object containing the customer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV3Xml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_v4(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieves customer information using the GetCustomerV4 SOAP operation.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The response from the GetCustomerV4 SOAP operation containing customer data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV4", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_v4_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customers (v4) in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing customer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV4Xml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_v5(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customers using the v5 API endpoint.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the customer results.
                If provided, will be converted to XML format for the SOAP request. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the customer results.
                If provided, will be converted to XML format for the SOAP request. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The response from the GetCustomerV5 SOAP operation containing customer data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV5", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_v5_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer data in XML format using the GetCustomerV5Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include customer attributes in the response.
                Defaults to None.

        Returns:
            SoapResponse: The response object containing the customer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV5Xml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def get_customer_xml(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for how to sort the
                customer results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering
                which customers to retrieve. Defaults to None.
            include_attributes (Optional[bool], optional): Whether to include additional attributes
                in the response. Defaults to None.

        Returns:
            SoapResponse: The response object containing the customer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerXml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes)

    def send_customer_contact_password(
        self,
        customer_contact_id: Optional[int] = None,
        sender_description: Optional[str] = None,
    ) -> SoapResponse:
        """
        Send a password reset email to a customer contact.

        Args:
            customer_contact_id (Optional[int], optional): The unique identifier of the customer contact
                who should receive the password reset email. Defaults to None.
            sender_description (Optional[str], optional): A description of the sender
                to be included in the email. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service indicating whether the
                password reset email was sent successfully.
        """
        return self._call("SendCustomerContactPassword", customerContactID=customer_contact_id, strSenderDescription=sender_description)

    def send_customer_contact_password_english(
        self,
        customer_contact_id: Optional[int] = None,
        sender_description: Optional[str] = None,
    ) -> SoapResponse:
        """
        Send a password email to a customer contact in English.

        Args:
            customer_contact_id (Optional[int], optional): The unique identifier of the customer contact to send the password to. Defaults to None.
            sender_description (Optional[str], optional): A description of the sender to include in the email.
                Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service call containing the result
                of the password email send operation.
        """
        return self._call(
            "SendCustomerContactPasswordEnglish",
            customerContactID=customer_contact_id,
            strSenderDescription=sender_description,
        )

    def send_customer_password(
        self,
        customer_id: Optional[int] = None,
        sender_description: Optional[str] = None,
    ) -> SoapResponse:
        """
        Send a password reset email to a customer.

        Args:
            customer_id (Optional[int], optional): The unique identifier of the customer. Defaults to None.
            sender_description (Optional[str], optional): A description of the sender
                to be included in the email. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the
                result of the password send operation.
        """
        return self._call("SendCustomerPassword", customerID=customer_id, strSenderDescription=sender_description)

    def set_customer(
        self,
        customer_id: Optional[int] = None,
        customer_number: Optional[str] = None,
        customer_name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        phone: Optional[str] = None,
        mobile: Optional[str] = None,
        fax: Optional[str] = None,
        email: Optional[str] = None,
        homepage: Optional[str] = None,
        invoice_name: Optional[str] = None,
        invoice_address1: Optional[str] = None,
        invoice_address2: Optional[str] = None,
        invoice_zip: Optional[str] = None,
        invoice_city: Optional[str] = None,
        invoice_country: Optional[str] = None,
        invoice_orgnr: Optional[str] = None,
        customer_group_name: Optional[str] = None,
        customer_group_id: Optional[int] = None,
        password: Optional[str] = None,
        invoice_vatnr: Optional[str] = None,
        customer_reference: Optional[str] = None,
        vat_free: Optional[bool] = None,
        attribute: Optional[Any] = None,
    ) -> SoapResponse:
        """
        Set or update customer information in the LegaOnline system.

        Args:
            customer_id (Optional[int]): The unique ID of the customer. Required in WSDL.
            customer_number (Optional[str]): The customer number.
            customer_name (Optional[str]): The customer name.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            country (Optional[str]): Country.
            phone (Optional[str]): Phone number.
            mobile (Optional[str]): Mobile number.
            fax (Optional[str]): Fax number.
            email (Optional[str]): Email address.
            homepage (Optional[str]): Homepage URL.
            invoice_name (Optional[str]): Invoice name.
            invoice_address1 (Optional[str]): Invoice primary address.
            invoice_address2 (Optional[str]): Invoice secondary address.
            invoice_zip (Optional[str]): Invoice zip/postal code.
            invoice_city (Optional[str]): Invoice city.
            invoice_country (Optional[str]): Invoice country.
            invoice_orgnr (Optional[str]): Invoice organisation number.
            customer_group_name (Optional[str]): Customer group name.
            customer_group_id (Optional[int]): Customer group ID. Required in WSDL.
            password (Optional[str]): Customer password.
            invoice_vatnr (Optional[str]): Invoice VAT number.
            customer_reference (Optional[str]): Customer reference.
            vat_free (Optional[bool]): Whether the customer is VAT-free. Required in WSDL.
            attribute (Optional[Any]): Complex attribute data.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                of the SetCustomer operation.
        """
        record = {k: v for k, v in {
            "CustomerID": customer_id,
            "CustomerNumber": customer_number,
            "CustomerName": customer_name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "Country": country,
            "Phone": phone,
            "Mobile": mobile,
            "Fax": fax,
            "Email": email,
            "Homepage": homepage,
            "InvoiceName": invoice_name,
            "InvoiceAddress1": invoice_address1,
            "InvoiceAddress2": invoice_address2,
            "InvoiceZip": invoice_zip,
            "InvoiceCity": invoice_city,
            "InvoiceCountry": invoice_country,
            "InvoiceOrgnr": invoice_orgnr,
            "CustomerGroupName": customer_group_name,
            "CustomerGroupID": customer_group_id,
            "Password": password,
            "InvoiceVatnr": invoice_vatnr,
            "CustomerReference": customer_reference,
            "VatFree": vat_free,
            "Attribute": attribute,
        }.items() if v is not None}
        return self._call("SetCustomer", customer={"Customer": [record]})

    def set_customer_v2(
        self,
        invoice_email: Optional[str] = None,
        our_reference: Optional[str] = None,
        edi_reference: Optional[str] = None,
        notes: Optional[str] = None,
        can_login: Optional[bool] = None,
        discount_percent: Optional[Decimal] = None,
        participant_discount_percent: Optional[Decimal] = None,
        not_creditworthy: Optional[bool] = None,
        customer_id: Optional[int] = None,
        customer_number: Optional[str] = None,
        customer_name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        phone: Optional[str] = None,
        mobile: Optional[str] = None,
        fax: Optional[str] = None,
        email: Optional[str] = None,
        homepage: Optional[str] = None,
        invoice_name: Optional[str] = None,
        invoice_address1: Optional[str] = None,
        invoice_address2: Optional[str] = None,
        invoice_zip: Optional[str] = None,
        invoice_city: Optional[str] = None,
        invoice_country: Optional[str] = None,
        invoice_orgnr: Optional[str] = None,
        customer_group_name: Optional[str] = None,
        customer_group_id: Optional[int] = None,
        password: Optional[str] = None,
        invoice_vatnr: Optional[str] = None,
        customer_reference: Optional[str] = None,
        vat_free: Optional[bool] = None,
        attribute: Optional[Any] = None,
    ) -> SoapResponse:
        """
        Set customer information using the SetCustomerV2 SOAP method.

        Args:
            invoice_email (Optional[str]): Invoice email address.
            our_reference (Optional[str]): Our reference.
            edi_reference (Optional[str]): EDI reference.
            notes (Optional[str]): Notes.
            can_login (Optional[bool]): Whether the customer can log in. Required in WSDL.
            discount_percent (Optional[Decimal]): Discount percentage. Required in WSDL.
            participant_discount_percent (Optional[Decimal]): Participant discount percentage. Required in WSDL.
            not_creditworthy (Optional[bool]): Whether the customer is not creditworthy. Required in WSDL.
            customer_id (Optional[int]): The unique ID of the customer. Required in WSDL.
            customer_number (Optional[str]): The customer number.
            customer_name (Optional[str]): The customer name.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            country (Optional[str]): Country.
            phone (Optional[str]): Phone number.
            mobile (Optional[str]): Mobile number.
            fax (Optional[str]): Fax number.
            email (Optional[str]): Email address.
            homepage (Optional[str]): Homepage URL.
            invoice_name (Optional[str]): Invoice name.
            invoice_address1 (Optional[str]): Invoice primary address.
            invoice_address2 (Optional[str]): Invoice secondary address.
            invoice_zip (Optional[str]): Invoice zip/postal code.
            invoice_city (Optional[str]): Invoice city.
            invoice_country (Optional[str]): Invoice country.
            invoice_orgnr (Optional[str]): Invoice organisation number.
            customer_group_name (Optional[str]): Customer group name.
            customer_group_id (Optional[int]): Customer group ID. Required in WSDL.
            password (Optional[str]): Customer password.
            invoice_vatnr (Optional[str]): Invoice VAT number.
            customer_reference (Optional[str]): Customer reference.
            vat_free (Optional[bool]): Whether the customer is VAT-free. Required in WSDL.
            attribute (Optional[Any]): Complex attribute data.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        record = {k: v for k, v in {
            "InvoiceEmail": invoice_email,
            "OurReference": our_reference,
            "EdiReference": edi_reference,
            "Notes": notes,
            "CanLogin": can_login,
            "DiscountPercent": discount_percent,
            "ParticipantDiscountPercent": participant_discount_percent,
            "NotCreditworthy": not_creditworthy,
            "CustomerID": customer_id,
            "CustomerNumber": customer_number,
            "CustomerName": customer_name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "Country": country,
            "Phone": phone,
            "Mobile": mobile,
            "Fax": fax,
            "Email": email,
            "Homepage": homepage,
            "InvoiceName": invoice_name,
            "InvoiceAddress1": invoice_address1,
            "InvoiceAddress2": invoice_address2,
            "InvoiceZip": invoice_zip,
            "InvoiceCity": invoice_city,
            "InvoiceCountry": invoice_country,
            "InvoiceOrgnr": invoice_orgnr,
            "CustomerGroupName": customer_group_name,
            "CustomerGroupID": customer_group_id,
            "Password": password,
            "InvoiceVatnr": invoice_vatnr,
            "CustomerReference": customer_reference,
            "VatFree": vat_free,
            "Attribute": attribute,
        }.items() if v is not None}
        return self._call("SetCustomerV2", customer={"CustomerV2": [record]})

    def set_customer_v3(
        self,
        invoice_delivery_method_id: Optional[int] = None,
        invoice_email: Optional[str] = None,
        our_reference: Optional[str] = None,
        edi_reference: Optional[str] = None,
        notes: Optional[str] = None,
        can_login: Optional[bool] = None,
        discount_percent: Optional[Decimal] = None,
        participant_discount_percent: Optional[Decimal] = None,
        not_creditworthy: Optional[bool] = None,
        customer_id: Optional[int] = None,
        customer_number: Optional[str] = None,
        customer_name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        phone: Optional[str] = None,
        mobile: Optional[str] = None,
        fax: Optional[str] = None,
        email: Optional[str] = None,
        homepage: Optional[str] = None,
        invoice_name: Optional[str] = None,
        invoice_address1: Optional[str] = None,
        invoice_address2: Optional[str] = None,
        invoice_zip: Optional[str] = None,
        invoice_city: Optional[str] = None,
        invoice_country: Optional[str] = None,
        invoice_orgnr: Optional[str] = None,
        customer_group_name: Optional[str] = None,
        customer_group_id: Optional[int] = None,
        password: Optional[str] = None,
        invoice_vatnr: Optional[str] = None,
        customer_reference: Optional[str] = None,
        vat_free: Optional[bool] = None,
        attribute: Optional[Any] = None,
    ) -> SoapResponse:
        """
        Set customer information using the SetCustomerV3 SOAP method.

        Args:
            invoice_delivery_method_id (Optional[int]): Invoice delivery method ID. Required in WSDL.
            invoice_email (Optional[str]): Invoice email address.
            our_reference (Optional[str]): Our reference.
            edi_reference (Optional[str]): EDI reference.
            notes (Optional[str]): Notes.
            can_login (Optional[bool]): Whether the customer can log in. Required in WSDL.
            discount_percent (Optional[Decimal]): Discount percentage. Required in WSDL.
            participant_discount_percent (Optional[Decimal]): Participant discount percentage. Required in WSDL.
            not_creditworthy (Optional[bool]): Whether the customer is not creditworthy. Required in WSDL.
            customer_id (Optional[int]): The unique ID of the customer. Required in WSDL.
            customer_number (Optional[str]): The customer number.
            customer_name (Optional[str]): The customer name.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            country (Optional[str]): Country.
            phone (Optional[str]): Phone number.
            mobile (Optional[str]): Mobile number.
            fax (Optional[str]): Fax number.
            email (Optional[str]): Email address.
            homepage (Optional[str]): Homepage URL.
            invoice_name (Optional[str]): Invoice name.
            invoice_address1 (Optional[str]): Invoice primary address.
            invoice_address2 (Optional[str]): Invoice secondary address.
            invoice_zip (Optional[str]): Invoice zip/postal code.
            invoice_city (Optional[str]): Invoice city.
            invoice_country (Optional[str]): Invoice country.
            invoice_orgnr (Optional[str]): Invoice organisation number.
            customer_group_name (Optional[str]): Customer group name.
            customer_group_id (Optional[int]): Customer group ID. Required in WSDL.
            password (Optional[str]): Customer password.
            invoice_vatnr (Optional[str]): Invoice VAT number.
            customer_reference (Optional[str]): Customer reference.
            vat_free (Optional[bool]): Whether the customer is VAT-free. Required in WSDL.
            attribute (Optional[Any]): Complex attribute data.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        record = {k: v for k, v in {
            "InvoiceDeliveryMethodID": invoice_delivery_method_id,
            "InvoiceEmail": invoice_email,
            "OurReference": our_reference,
            "EdiReference": edi_reference,
            "Notes": notes,
            "CanLogin": can_login,
            "DiscountPercent": discount_percent,
            "ParticipantDiscountPercent": participant_discount_percent,
            "NotCreditworthy": not_creditworthy,
            "CustomerID": customer_id,
            "CustomerNumber": customer_number,
            "CustomerName": customer_name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "Country": country,
            "Phone": phone,
            "Mobile": mobile,
            "Fax": fax,
            "Email": email,
            "Homepage": homepage,
            "InvoiceName": invoice_name,
            "InvoiceAddress1": invoice_address1,
            "InvoiceAddress2": invoice_address2,
            "InvoiceZip": invoice_zip,
            "InvoiceCity": invoice_city,
            "InvoiceCountry": invoice_country,
            "InvoiceOrgnr": invoice_orgnr,
            "CustomerGroupName": customer_group_name,
            "CustomerGroupID": customer_group_id,
            "Password": password,
            "InvoiceVatnr": invoice_vatnr,
            "CustomerReference": customer_reference,
            "VatFree": vat_free,
            "Attribute": attribute,
        }.items() if v is not None}
        return self._call("SetCustomerV3", customer={"CustomerV3": [record]})

    def set_customer_v4(
        self,
        no_invoice_fee: Optional[bool] = None,
        invoice_delivery_method_id: Optional[int] = None,
        invoice_email: Optional[str] = None,
        our_reference: Optional[str] = None,
        edi_reference: Optional[str] = None,
        notes: Optional[str] = None,
        can_login: Optional[bool] = None,
        discount_percent: Optional[Decimal] = None,
        participant_discount_percent: Optional[Decimal] = None,
        not_creditworthy: Optional[bool] = None,
        customer_id: Optional[int] = None,
        customer_number: Optional[str] = None,
        customer_name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        phone: Optional[str] = None,
        mobile: Optional[str] = None,
        fax: Optional[str] = None,
        email: Optional[str] = None,
        homepage: Optional[str] = None,
        invoice_name: Optional[str] = None,
        invoice_address1: Optional[str] = None,
        invoice_address2: Optional[str] = None,
        invoice_zip: Optional[str] = None,
        invoice_city: Optional[str] = None,
        invoice_country: Optional[str] = None,
        invoice_orgnr: Optional[str] = None,
        customer_group_name: Optional[str] = None,
        customer_group_id: Optional[int] = None,
        password: Optional[str] = None,
        invoice_vatnr: Optional[str] = None,
        customer_reference: Optional[str] = None,
        vat_free: Optional[bool] = None,
        attribute: Optional[Any] = None,
    ) -> SoapResponse:
        """
        Set customer information using the SetCustomerV4 SOAP method.

        Args:
            no_invoice_fee (Optional[bool]): Whether there is no invoice fee. Required in WSDL.
            invoice_delivery_method_id (Optional[int]): Invoice delivery method ID. Required in WSDL.
            invoice_email (Optional[str]): Invoice email address.
            our_reference (Optional[str]): Our reference.
            edi_reference (Optional[str]): EDI reference.
            notes (Optional[str]): Notes.
            can_login (Optional[bool]): Whether the customer can log in. Required in WSDL.
            discount_percent (Optional[Decimal]): Discount percentage. Required in WSDL.
            participant_discount_percent (Optional[Decimal]): Participant discount percentage. Required in WSDL.
            not_creditworthy (Optional[bool]): Whether the customer is not creditworthy. Required in WSDL.
            customer_id (Optional[int]): The unique ID of the customer. Required in WSDL.
            customer_number (Optional[str]): The customer number.
            customer_name (Optional[str]): The customer name.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            country (Optional[str]): Country.
            phone (Optional[str]): Phone number.
            mobile (Optional[str]): Mobile number.
            fax (Optional[str]): Fax number.
            email (Optional[str]): Email address.
            homepage (Optional[str]): Homepage URL.
            invoice_name (Optional[str]): Invoice name.
            invoice_address1 (Optional[str]): Invoice primary address.
            invoice_address2 (Optional[str]): Invoice secondary address.
            invoice_zip (Optional[str]): Invoice zip/postal code.
            invoice_city (Optional[str]): Invoice city.
            invoice_country (Optional[str]): Invoice country.
            invoice_orgnr (Optional[str]): Invoice organisation number.
            customer_group_name (Optional[str]): Customer group name.
            customer_group_id (Optional[int]): Customer group ID. Required in WSDL.
            password (Optional[str]): Customer password.
            invoice_vatnr (Optional[str]): Invoice VAT number.
            customer_reference (Optional[str]): Customer reference.
            vat_free (Optional[bool]): Whether the customer is VAT-free. Required in WSDL.
            attribute (Optional[Any]): Complex attribute data.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        record = {k: v for k, v in {
            "NoInvoiceFee": no_invoice_fee,
            "InvoiceDeliveryMethodID": invoice_delivery_method_id,
            "InvoiceEmail": invoice_email,
            "OurReference": our_reference,
            "EdiReference": edi_reference,
            "Notes": notes,
            "CanLogin": can_login,
            "DiscountPercent": discount_percent,
            "ParticipantDiscountPercent": participant_discount_percent,
            "NotCreditworthy": not_creditworthy,
            "CustomerID": customer_id,
            "CustomerNumber": customer_number,
            "CustomerName": customer_name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "Country": country,
            "Phone": phone,
            "Mobile": mobile,
            "Fax": fax,
            "Email": email,
            "Homepage": homepage,
            "InvoiceName": invoice_name,
            "InvoiceAddress1": invoice_address1,
            "InvoiceAddress2": invoice_address2,
            "InvoiceZip": invoice_zip,
            "InvoiceCity": invoice_city,
            "InvoiceCountry": invoice_country,
            "InvoiceOrgnr": invoice_orgnr,
            "CustomerGroupName": customer_group_name,
            "CustomerGroupID": customer_group_id,
            "Password": password,
            "InvoiceVatnr": invoice_vatnr,
            "CustomerReference": customer_reference,
            "VatFree": vat_free,
            "Attribute": attribute,
        }.items() if v is not None}
        return self._call("SetCustomerV4", customer={"CustomerV4": [record]})

    def set_customer_v5(
        self,
        gln: Optional[str] = None,
        no_invoice_fee: Optional[bool] = None,
        invoice_delivery_method_id: Optional[int] = None,
        invoice_email: Optional[str] = None,
        our_reference: Optional[str] = None,
        edi_reference: Optional[str] = None,
        notes: Optional[str] = None,
        can_login: Optional[bool] = None,
        discount_percent: Optional[Decimal] = None,
        participant_discount_percent: Optional[Decimal] = None,
        not_creditworthy: Optional[bool] = None,
        customer_id: Optional[int] = None,
        customer_number: Optional[str] = None,
        customer_name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        phone: Optional[str] = None,
        mobile: Optional[str] = None,
        fax: Optional[str] = None,
        email: Optional[str] = None,
        homepage: Optional[str] = None,
        invoice_name: Optional[str] = None,
        invoice_address1: Optional[str] = None,
        invoice_address2: Optional[str] = None,
        invoice_zip: Optional[str] = None,
        invoice_city: Optional[str] = None,
        invoice_country: Optional[str] = None,
        invoice_orgnr: Optional[str] = None,
        customer_group_name: Optional[str] = None,
        customer_group_id: Optional[int] = None,
        password: Optional[str] = None,
        invoice_vatnr: Optional[str] = None,
        customer_reference: Optional[str] = None,
        vat_free: Optional[bool] = None,
        attribute: Optional[Any] = None,
    ) -> SoapResponse:
        """
        Set customer information using the SetCustomerV5 SOAP method.

        Args:
            gln (Optional[str]): Global Location Number.
            no_invoice_fee (Optional[bool]): Whether there is no invoice fee. Required in WSDL.
            invoice_delivery_method_id (Optional[int]): Invoice delivery method ID. Required in WSDL.
            invoice_email (Optional[str]): Invoice email address.
            our_reference (Optional[str]): Our reference.
            edi_reference (Optional[str]): EDI reference.
            notes (Optional[str]): Notes.
            can_login (Optional[bool]): Whether the customer can log in. Required in WSDL.
            discount_percent (Optional[Decimal]): Discount percentage. Required in WSDL.
            participant_discount_percent (Optional[Decimal]): Participant discount percentage. Required in WSDL.
            not_creditworthy (Optional[bool]): Whether the customer is not creditworthy. Required in WSDL.
            customer_id (Optional[int]): The unique ID of the customer. Required in WSDL.
            customer_number (Optional[str]): The customer number.
            customer_name (Optional[str]): The customer name.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            country (Optional[str]): Country.
            phone (Optional[str]): Phone number.
            mobile (Optional[str]): Mobile number.
            fax (Optional[str]): Fax number.
            email (Optional[str]): Email address.
            homepage (Optional[str]): Homepage URL.
            invoice_name (Optional[str]): Invoice name.
            invoice_address1 (Optional[str]): Invoice primary address.
            invoice_address2 (Optional[str]): Invoice secondary address.
            invoice_zip (Optional[str]): Invoice zip/postal code.
            invoice_city (Optional[str]): Invoice city.
            invoice_country (Optional[str]): Invoice country.
            invoice_orgnr (Optional[str]): Invoice organisation number.
            customer_group_name (Optional[str]): Customer group name.
            customer_group_id (Optional[int]): Customer group ID. Required in WSDL.
            password (Optional[str]): Customer password.
            invoice_vatnr (Optional[str]): Invoice VAT number.
            customer_reference (Optional[str]): Customer reference.
            vat_free (Optional[bool]): Whether the customer is VAT-free. Required in WSDL.
            attribute (Optional[Any]): Complex attribute data.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        record = {k: v for k, v in {
            "GLN": gln,
            "NoInvoiceFee": no_invoice_fee,
            "InvoiceDeliveryMethodID": invoice_delivery_method_id,
            "InvoiceEmail": invoice_email,
            "OurReference": our_reference,
            "EdiReference": edi_reference,
            "Notes": notes,
            "CanLogin": can_login,
            "DiscountPercent": discount_percent,
            "ParticipantDiscountPercent": participant_discount_percent,
            "NotCreditworthy": not_creditworthy,
            "CustomerID": customer_id,
            "CustomerNumber": customer_number,
            "CustomerName": customer_name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "Country": country,
            "Phone": phone,
            "Mobile": mobile,
            "Fax": fax,
            "Email": email,
            "Homepage": homepage,
            "InvoiceName": invoice_name,
            "InvoiceAddress1": invoice_address1,
            "InvoiceAddress2": invoice_address2,
            "InvoiceZip": invoice_zip,
            "InvoiceCity": invoice_city,
            "InvoiceCountry": invoice_country,
            "InvoiceOrgnr": invoice_orgnr,
            "CustomerGroupName": customer_group_name,
            "CustomerGroupID": customer_group_id,
            "Password": password,
            "InvoiceVatnr": invoice_vatnr,
            "CustomerReference": customer_reference,
            "VatFree": vat_free,
            "Attribute": attribute,
        }.items() if v is not None}
        return self._call("SetCustomerV5", customer={"CustomerV5": [record]})

    def set_customer_xml(self, customer: Optional[str] = None) -> SoapResponse:
        """
        Set customer information using the SetCustomerXml SOAP method.

        Args:
            customer (Optional[str], optional): The customer data in XML format to be set. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("SetCustomerXml", customer=customer)

    def set_customer_contact(
        self,
        customer_contact_id: Optional[int] = None,
        contact_number: Optional[str] = None,
        customer_id: Optional[int] = None,
        contact_name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        phone: Optional[str] = None,
        mobile: Optional[str] = None,
        fax: Optional[str] = None,
        email: Optional[str] = None,
        position: Optional[str] = None,
        loginpass: Optional[str] = None,
        notes: Optional[str] = None,
        customer_group_name: Optional[str] = None,
        public_group: Optional[bool] = None,
        civic_registration_number: Optional[str] = None,
        can_login: Optional[bool] = None,
        attribute: Optional[Any] = None,
    ) -> SoapResponse:
        """
        Set or update customer contact information in the LegaOnline system.

        Args:
            customer_contact_id (Optional[int]): The unique ID of the customer contact. Required in WSDL.
            contact_number (Optional[str]): The contact number.
            customer_id (Optional[int]): The customer ID. Required in WSDL.
            contact_name (Optional[str]): The contact name.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            phone (Optional[str]): Phone number.
            mobile (Optional[str]): Mobile number.
            fax (Optional[str]): Fax number.
            email (Optional[str]): Email address.
            position (Optional[str]): Position/title.
            loginpass (Optional[str]): Login password.
            notes (Optional[str]): Notes.
            customer_group_name (Optional[str]): Customer group name.
            public_group (Optional[bool]): Whether the group is public. Required in WSDL.
            civic_registration_number (Optional[str]): Civic registration number.
            can_login (Optional[bool]): Whether the contact can log in. Required in WSDL.
            attribute (Optional[Any]): Complex attribute data.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                of the SetCustomerContact operation.
        """
        record = {k: v for k, v in {
            "CustomerContactID": customer_contact_id,
            "ContactNumber": contact_number,
            "CustomerID": customer_id,
            "ContactName": contact_name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "Phone": phone,
            "Mobile": mobile,
            "Fax": fax,
            "Email": email,
            "Position": position,
            "Loginpass": loginpass,
            "Notes": notes,
            "CustomerGroupName": customer_group_name,
            "PublicGroup": public_group,
            "CivicRegistrationNumber": civic_registration_number,
            "CanLogin": can_login,
            "Attribute": attribute,
        }.items() if v is not None}
        return self._call("SetCustomerContact", customerContact={"CustomerContact": [record]})

    def set_customer_contact_v2(
        self,
        purchase_order_number: Optional[str] = None,
        contact_reference: Optional[str] = None,
        country: Optional[str] = None,
        customer_contact_id: Optional[int] = None,
        contact_number: Optional[str] = None,
        customer_id: Optional[int] = None,
        contact_name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        phone: Optional[str] = None,
        mobile: Optional[str] = None,
        fax: Optional[str] = None,
        email: Optional[str] = None,
        position: Optional[str] = None,
        loginpass: Optional[str] = None,
        notes: Optional[str] = None,
        customer_group_name: Optional[str] = None,
        public_group: Optional[bool] = None,
        civic_registration_number: Optional[str] = None,
        can_login: Optional[bool] = None,
        attribute: Optional[Any] = None,
    ) -> SoapResponse:
        """
        Set customer contact information using version 2 of the API.

        Args:
            purchase_order_number (Optional[str]): Purchase order number.
            contact_reference (Optional[str]): Contact reference.
            country (Optional[str]): Country.
            customer_contact_id (Optional[int]): The unique ID of the customer contact. Required in WSDL.
            contact_number (Optional[str]): The contact number.
            customer_id (Optional[int]): The customer ID. Required in WSDL.
            contact_name (Optional[str]): The contact name.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            phone (Optional[str]): Phone number.
            mobile (Optional[str]): Mobile number.
            fax (Optional[str]): Fax number.
            email (Optional[str]): Email address.
            position (Optional[str]): Position/title.
            loginpass (Optional[str]): Login password.
            notes (Optional[str]): Notes.
            customer_group_name (Optional[str]): Customer group name.
            public_group (Optional[bool]): Whether the group is public. Required in WSDL.
            civic_registration_number (Optional[str]): Civic registration number.
            can_login (Optional[bool]): Whether the contact can log in. Required in WSDL.
            attribute (Optional[Any]): Complex attribute data.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the
                SetCustomerContactV2 operation.
        """
        record = {k: v for k, v in {
            "PurchaseOrderNumber": purchase_order_number,
            "ContactReference": contact_reference,
            "Country": country,
            "CustomerContactID": customer_contact_id,
            "ContactNumber": contact_number,
            "CustomerID": customer_id,
            "ContactName": contact_name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "Phone": phone,
            "Mobile": mobile,
            "Fax": fax,
            "Email": email,
            "Position": position,
            "Loginpass": loginpass,
            "Notes": notes,
            "CustomerGroupName": customer_group_name,
            "PublicGroup": public_group,
            "CivicRegistrationNumber": civic_registration_number,
            "CanLogin": can_login,
            "Attribute": attribute,
        }.items() if v is not None}
        return self._call("SetCustomerContactV2", customerContact={"CustomerContactV2": [record]})

    def set_customer_contact_v2_xml(self, customer_contact: Optional[str] = None) -> SoapResponse:
        """
        Set customer contact information using V2 XML format.

        Args:
            customer_contact (Optional[str], optional): The customer contact information in XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service call containing the result of setting customer contact information.
        """
        return self._call("SetCustomerContactV2Xml", customerContact=customer_contact)

    def set_customer_contact_xml(self, customer_contact: Optional[str] = None) -> SoapResponse:
        """
        Set customer contact information using XML format.

        Args:
            customer_contact (Optional[str], optional): XML string containing customer contact
                information. Defaults to None.

        Returns:
            SoapResponse: Response object from the SOAP service containing the result of
                the operation.
        """
        return self._call("SetCustomerContactXml", customerContact=customer_contact)

    def set_customer_contact_attributes(
        self,
        customer_contact_id: Optional[int] = None,
        customer_contact_attribute_id: Optional[int] = None,
        attribute_checked: Optional[bool] = None,
        attribute_date: Optional[dt.datetime] = None,
        attribute_id: Optional[int] = None,
        attribute_type_id: Optional[int] = None,
        attribute_type_description: Optional[str] = None,
        attribute_owner_type_id: Optional[int] = None,
        attribute_owner_type_description: Optional[str] = None,
        attribute_description: Optional[str] = None,
        attribute_value: Optional[str] = None,
        attribute_alternative: Optional[Any] = None,
    ) -> SoapResponse:
        """
        Set or update customer contact attributes in the LegaOnline system.

        Args:
            customer_contact_id (Optional[int]): The customer contact ID. Required in WSDL.
            customer_contact_attribute_id (Optional[int]): The customer contact attribute ID. Required in WSDL.
            attribute_checked (Optional[bool]): Whether the attribute is checked. Required in WSDL.
            attribute_date (Optional[dt.datetime]): Attribute date. Required in WSDL.
            attribute_id (Optional[int]): Attribute ID. Required in WSDL.
            attribute_type_id (Optional[int]): Attribute type ID. Required in WSDL.
            attribute_type_description (Optional[str]): Attribute type description.
            attribute_owner_type_id (Optional[int]): Attribute owner type ID. Required in WSDL.
            attribute_owner_type_description (Optional[str]): Attribute owner type description.
            attribute_description (Optional[str]): Attribute description.
            attribute_value (Optional[str]): Attribute value.
            attribute_alternative (Optional[Any]): Complex attribute alternative data.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                of the SetCustomerContactAttributes operation.
        """
        record = {k: v for k, v in {
            "CustomerContactID": customer_contact_id,
            "CustomerContactAttributeID": customer_contact_attribute_id,
            "AttributeChecked": attribute_checked,
            "AttributeDate": attribute_date,
            "AttributeID": attribute_id,
            "AttributeTypeID": attribute_type_id,
            "AttributeTypeDescription": attribute_type_description,
            "AttributeOwnerTypeID": attribute_owner_type_id,
            "AttributeOwnerTypeDescription": attribute_owner_type_description,
            "AttributeDescription": attribute_description,
            "AttributeValue": attribute_value,
            "AttributeAlternative": attribute_alternative,
        }.items() if v is not None}
        return self._call("SetCustomerContactAttributes", customerContactAttribute={"CustomerContactAttribute": [record]})

    def set_customer_contact_attributes_xml(self, customer_contact_attribute: Optional[str] = None) -> SoapResponse:
        """
        Set customer contact attributes using XML format.

        Args:
            customer_contact_attribute (Optional[str], optional): XML string containing the customer
                contact attributes to be set. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service call containing the result
                of the operation.
        """
        return self._call("SetCustomerContactAttributesXml", customerContactAttribute=customer_contact_attribute)

    def set_customer_shipping(
        self,
        customer_shipping_address_lnk_id: Optional[int] = None,
        customer_id: Optional[int] = None,
        name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        shipping_notes: Optional[str] = None,
    ) -> SoapResponse:
        """
        Set customer shipping information.

        Args:
            customer_shipping_address_lnk_id (Optional[int]): Shipping address link ID. Required in WSDL.
            customer_id (Optional[int]): The customer ID. Required in WSDL.
            name (Optional[str]): Name for the shipping address.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            shipping_notes (Optional[str]): Shipping notes.

        Returns:
            SoapResponse: The response object from the SOAP service call containing the result of the
                SetCustomerShipping operation.
        """
        record = {k: v for k, v in {
            "CustomerShippingAddressLnkID": customer_shipping_address_lnk_id,
            "CustomerID": customer_id,
            "Name": name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "ShippingNotes": shipping_notes,
        }.items() if v is not None}
        return self._call("SetCustomerShipping", customerShippingList={"CustomerShipping": [record]})

    def set_customer_shipping_and_pickup(
        self,
        customer_shipping_address_lnk_id: Optional[int] = None,
        customer_id: Optional[int] = None,
        name: Optional[str] = None,
        address1: Optional[str] = None,
        address2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        shipping_notes: Optional[str] = None,
    ) -> SoapResponse:
        """
        Set customer shipping and pickup information.

        Args:
            customer_shipping_address_lnk_id (Optional[int]): Shipping address link ID. Required in WSDL.
            customer_id (Optional[int]): The customer ID. Required in WSDL.
            name (Optional[str]): Name for the shipping address.
            address1 (Optional[str]): Primary address line.
            address2 (Optional[str]): Secondary address line.
            zip (Optional[str]): Zip/postal code.
            city (Optional[str]): City.
            shipping_notes (Optional[str]): Shipping notes.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result of the operation.
        """
        record = {k: v for k, v in {
            "CustomerShippingAddressLnkID": customer_shipping_address_lnk_id,
            "CustomerID": customer_id,
            "Name": name,
            "Address1": address1,
            "Address2": address2,
            "Zip": zip,
            "City": city,
            "ShippingNotes": shipping_notes,
        }.items() if v is not None}
        return self._call("SetCustomerShippingAndPickup", customerShippingList={"CustomerShipping": [record]})

    def set_master_customer_id(
        self,
        customer_id: Optional[int] = None,
        master_customer_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set the master customer ID for a customer.

        Args:
            customer_id (Optional[int], optional): The ID of the customer to set the master customer ID for. Defaults to None.
            master_customer_id (Optional[int], optional): The ID of the master customer to associate with the customer. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("SetMasterCustomerID", customerID=customer_id, masterCustomerID=master_customer_id)

    def set_master_customer_contact_id(
        self,
        customer_contact_id: Optional[int] = None,
        master_customer_contact_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Sets the master customer contact ID for a given customer contact.

        Args:
            customer_contact_id (Optional[int], optional): The ID of the customer contact to update. Defaults to None.
            master_customer_contact_id (Optional[int], optional): The ID of the master customer contact to associate with. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                          of the operation.
        """
        return self._call("SetMasterCustomerContactID", customerContactID=customer_contact_id, masterCustomerContactID=master_customer_contact_id)
