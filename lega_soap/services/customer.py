from __future__ import annotations

import datetime as dt
from typing import Any

from ..types import SoapResponse
from typing import Optional
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

    def delete_customer_contact(self, customer_contact_list: Optional[IntListSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Delete customer contact(s) from the system.

        Args:
            customer_contact_list (Optional[IntListSpec], optional): A list specification containing
                the IDs of customer contacts to be deleted. If None, no contacts will be deleted.
                Defaults to None.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response object containing the result of the delete operation.

        Raises:
            May raise exceptions related to SOAP communication or invalid customer contact IDs,
            depending on the implementation of the underlying _call method.
        """
        customer_contact_list_xml = customer_contact_list.to_xml() if customer_contact_list else ""
        return self._call("DeleteCustomerContact", customerContactIDs=customer_contact_list_xml, **kwargs)

    def delete_customer_contact_attribute(self, customer_contact_attribute_list: Optional[IntListSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Delete customer contact attributes.

        Args:
            customer_contact_attribute_list (Optional[IntListSpec], optional): A list specification
                containing the IDs of customer contact attributes to delete. Defaults to None.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response from the DeleteCustomerContactAttribute operation.

        Raises:
            May raise exceptions related to SOAP communication or service errors.
        """
        customer_contact_attribute_list_xml = customer_contact_attribute_list.to_xml() if customer_contact_attribute_list else ""
        return self._call("DeleteCustomerContactAttribute", CustomerContactAttributeLnkIDs=customer_contact_attribute_list_xml, **kwargs)

    def get_customer(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any
    ) -> SoapResponse:
        """
        Retrieve customer information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.
            include_attributes (bool, optional): Whether to include customer attributes in the response.
                Defaults to False.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing customer data.

        Raises:
            May raise exceptions from the underlying _call method depending on SOAP service errors.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomer", sort_xml, filter_xml, include_attributes, **kwargs)

    def get_customer_attribute(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        **kwargs: Any
    ) -> SoapResponse:
        """
        Retrieve customer attributes from the SOAP service.

        This method calls the GetCustomerAttribute SOAP endpoint with optional sorting
        and filtering parameters.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the customer attribute data
                returned by the SOAP service.

        Example:
            >>> service = CustomerService()
            >>> response = service.get_customer_attribute(
            ...     sorting=SortSpec(field="name", order="asc"),
            ...     filtering=FilterSpec(field="status", value="active")
            ... )
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerAttribute", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_customer_attribute_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        **kwargs: Any
    ) -> SoapResponse:
        """
        Retrieve customer attribute data in XML format from the SOAP service.

        This method calls the GetCustomerAttributeXml SOAP operation with optional
        sorting and filtering specifications.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the customer attribute data in XML format.

        Example:
            >>> response = service.get_customer_attribute_xml(
            ...     sorting=SortSpec(field="name", order="asc"),
            ...     filtering=FilterSpec(field="status", value="active")
            ... )
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerAttributeXml", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_customer_contact(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any
    ) -> SoapResponse:
        """
        Retrieve customer contact information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            include_attributes (bool, optional): Whether to include additional attributes
                in the response. Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the underlying
                SOAP service call.

        Returns:
            SoapResponse: The response object containing customer contact information
                returned from the SOAP service.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerContact", sort=sort_xml, filter=filter_xml, include_attributes=include_attributes, **kwargs)

    def get_customer_contact_attribute(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        **kwargs: Any
    ) -> SoapResponse:
        """
        Retrieve customer contact attributes from the SOAP service.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                customer contact attribute data.

        Example:
            >>> response = customer_service.get_customer_contact_attribute(
            ...     sorting=SortSpec(...),
            ...     filtering=FilterSpec(...)
            ... )
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerContactAttribute", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_customer_contact_attribute_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer contact attribute data in XML format.

        SOAP operation: GetCustomerContactAttributeXml
        WSDL params: sort, filter

        Args:
            sorting: Optional SortSpec used to generate the sort XML string.
            filtering: Optional FilterSpec used to generate the filter XML string.
            **kwargs: Additional keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse containing XML data (as returned by the API).
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerContactAttributeXml", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_customer_contact_v2(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any
    ) -> SoapResponse:
        """
        Retrieve customer contacts (v2).

        SOAP operation: GetCustomerContactV2
        WSDL params: sort, filter, includeAttributes

        Args:
            sorting: Optional SortSpec used to generate the sort XML string.
            filtering: Optional FilterSpec used to generate the filter XML string.
            include_attributes: Include attribute data for each contact.
            **kwargs: Additional keyword arguments passed to the SOAP call.

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
            **kwargs,
        **kwargs,
    )

    def get_customer_contact_v2_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer contacts (v2) in XML format.

        SOAP operation: GetCustomerContactV2Xml
        WSDL params: sort, filter, includeAttributes

        Args:
            sorting: Optional SortSpec used to generate the sort XML string.
            filtering: Optional FilterSpec used to generate the filter XML string.
            include_attributes: Include attribute data for each contact.
            **kwargs: Additional keyword arguments passed to the SOAP call.

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
            **kwargs,
        **kwargs,
    )

    def get_customer_contact_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer contacts in XML format.

        SOAP operation: GetCustomerContactXml
        WSDL params: sort, filter, includeAttributes

        Args:
            sorting: Optional SortSpec used to generate the sort XML string.
            filtering: Optional FilterSpec used to generate the filter XML string.
            include_attributes: Include attribute data for each contact.
            **kwargs: Additional keyword arguments passed to the SOAP call.

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
            **kwargs,
        **kwargs,
    )

    def get_customer_group(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer group information from the SOAP service.
        This method fetches customer group data with optional sorting and filtering capabilities.
        It constructs the appropriate XML for sorting and filtering specifications before making
        the SOAP call.
        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the underlying SOAP call.
        Returns:
            SoapResponse: The response object containing the customer group data returned
                from the SOAP service.
        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="active", value=True)
            >>> response = service.get_customer_group(sorting=sort_spec, filtering=filter_spec)
        """
        
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerGroup", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_customer_group_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer group data in XML format from the SOAP service.

        This method calls the GetCustomerGroupXml SOAP operation with optional sorting
        and filtering parameters.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the underlying
                SOAP call.

        Returns:
            SoapResponse: The response object containing the customer group data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerGroupXml", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_customer_shipping(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer shipping information from the SOAP service.
        This method calls the 'GetCustomerShipping' SOAP operation with optional
        sorting and filtering parameters.
        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.
        Returns:
            SoapResponse: The response object containing customer shipping information
                returned by the SOAP service.
        Example:
            >>> response = service.get_customer_shipping(
            ...     sorting=SortSpec(field="name", order="asc"),
            ...     filtering=FilterSpec(field="status", value="active")
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerShipping", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_customer_shipping_and_pickup(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer shipping and pickup information from the SOAP service.

        This method fetches customer shipping and pickup data, with optional sorting
        and filtering capabilities. The sorting and filtering specifications are
        converted to XML format before being passed to the SOAP service.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the underlying
                SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                customer shipping and pickup information.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_customer_shipping_and_pickup(
            ...     sorting=sort_spec,
            ...     filtering=filter_spec
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerShippingAndPickup", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_customer_v2(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer data using the GetCustomerV2 SOAP operation.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.
            include_attributes (bool, optional): Whether to include customer attributes in the response.
                Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing customer data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV2", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)

    def get_customer_v2_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer data in XML format using the GetCustomerV2Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. 
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. 
                Defaults to None.
            include_attributes (bool, optional): Whether to include customer attributes in the response. 
                Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing customer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV2Xml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)
    
    def get_customer_v3(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer information using the GetCustomerV3 SOAP method.
        This method fetches customer data with optional sorting, filtering, and attribute inclusion.
        The sorting and filtering specifications are converted to XML format before being passed
        to the SOAP service.
        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the customer results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering customer results.
                If provided, will be converted to XML format. Defaults to None.
            include_attributes (bool, optional): Whether to include customer attributes in the response.
                Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the underlying SOAP call.
        Returns:
            SoapResponse: The response from the GetCustomerV3 SOAP method containing customer data.
        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_customer_v3(
            ...     sorting=sort_spec,
            ...     filtering=filter_spec,
            ...     include_attributes=True
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        
        return self._call("GetCustomerV3", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)

    def get_customer_v3_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer data in XML format using the GetCustomerV3Xml SOAP method.
        This method fetches customer information with optional sorting, filtering, and 
        attribute inclusion capabilities.
        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. 
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. 
                If provided, will be converted to XML format. Defaults to None.
            include_attributes (bool, optional): Whether to include customer attributes in the response. 
                Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.
        Returns:
            SoapResponse: The response object containing the customer data in XML format.
        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_customer_v3_xml(
            ...     sorting=sort_spec,
            ...     filtering=filter_spec,
            ...     include_attributes=True
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        
        return self._call("GetCustomerV3Xml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)

    def get_customer_v4(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieves customer information using the GetCustomerV4 SOAP operation.
        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.
            include_attributes (bool, optional): Whether to include customer attributes in the response.
                Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.
        Returns:
            SoapResponse: The response from the GetCustomerV4 SOAP operation containing
                customer data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        
        return self._call("GetCustomerV4", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)

    def get_customer_v4_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customers (v4) in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            include_attributes (bool): Whether to include customer attributes in the response.
                Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing customer data in XML format.

        Notes:
            - SOAP operation: GetCustomerV4Xml
            - WSDL parameters: sort, filter, includeAttributes
            - If sorting or filtering are None, empty strings are passed to the SOAP call
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV4Xml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)

    def get_customer_v5(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customers using the v5 API endpoint.

        This method fetches customer data from the SOAP service with optional sorting,
        filtering, and attribute inclusion capabilities.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the customer results.
                If provided, will be converted to XML format for the SOAP request.
                Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the customer results.
                If provided, will be converted to XML format for the SOAP request.
                Defaults to None.
            include_attributes (bool): Whether to include customer attributes in the response.
                Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the underlying SOAP call.

        Returns:
            SoapResponse: The response from the GetCustomerV5 SOAP operation containing
                customer data.

        Example:
            >>> customer_service = CustomerService()
            >>> response = customer_service.get_customer_v5(
            ...     sorting=SortSpec(field="name", order="asc"),
            ...     filtering=FilterSpec(field="active", value=True),
            ...     include_attributes=True
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV5", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)

    def get_customer_v5_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer data in XML format using the GetCustomerV5Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. 
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. 
                Defaults to None.
            include_attributes (bool, optional): Whether to include customer attributes in the response. 
                Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP method.

        Returns:
            SoapResponse: The response object containing the customer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerV5Xml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)

    def get_customer_xml(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Retrieve customer data in XML format from the SOAP service.

        This method calls the 'GetCustomerXml' SOAP operation with optional sorting,
        filtering, and attribute inclusion parameters.

        Args:
            sorting (Optional[SortSpec], optional): Specification for how to sort the
                customer results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering
                which customers to retrieve. Defaults to None.
            include_attributes (bool, optional): Whether to include additional attributes
                in the response. Defaults to False.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the customer data in XML format.

        Raises:
            SoapException: If the SOAP call fails or returns an error.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCustomerXml", sort=sort_xml, filter=filter_xml, includeAttributes=include_attributes, **kwargs)

    def send_customer_contact_password(
        self,
        *,
        customer_contact_id: int,
        sender_description: Optional[str] = None,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Send a password reset email to a customer contact.

        This method sends a password reset email to the specified customer contact,
        allowing them to set or reset their password.

        Args:
            customer_contact_id (int): The unique identifier of the customer contact
                who should receive the password reset email.
            sender_description (Optional[str], optional): A description of the sender
                to be included in the email. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response from the SOAP service indicating whether the
                password reset email was sent successfully.

        Raises:
            SoapException: If the SOAP service call fails or returns an error.
        """
        return self._call("SendCustomerContactPassword", customerContactID=customer_contact_id, strSenderDescription=sender_description, **kwargs)

    def send_customer_contact_password_english(
        self,
        *,
        customer_contact_id: int,
        sender_description: Optional[str] = None,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Send a password email to a customer contact in English.

        This method triggers an email containing password information to be sent to the specified
        customer contact using an English language template.

        Args:
            customer_contact_id (int): The unique identifier of the customer contact to send the password to.
            sender_description (Optional[str], optional): A description of the sender to include in the email.
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service call containing the result
                of the password email send operation.

        Raises:
            May raise exceptions from the underlying SOAP service call depending on the implementation
            of the _call method.
        """
        return self._call(
            "SendCustomerContactPasswordEnglish",
            customerContactID=customer_contact_id,
            strSenderDescription=sender_description,
            **kwargs,
        **kwargs,
    )

    def send_customer_password(
        self,
        *,
        customer_id: int,
        sender_description: Optional[str] = None,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Send a password reset email to a customer.

        Args:
            customer_id (int): The unique identifier of the customer.
            sender_description (Optional[str], optional): A description of the sender 
                to be included in the email. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service.

        Returns:
            SoapResponse: The response object from the SOAP service containing the 
                result of the password send operation.
        """
        return self._call("SendCustomerPassword", customerID=customer_id, strSenderDescription=sender_description, **kwargs)

    def set_customer(self, *, customer: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set or update customer information in the LegaOnline system.

        Args:
            customer (Optional[Any], optional): The customer object or data to be set/updated. 
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result 
                of the SetCustomer operation.

        Raises:
            May raise exceptions related to SOAP communication or service errors.
        """
        return self._call("SetCustomer", customer=customer, **kwargs)

    def set_customer_contact(self, *, customer_contact: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set or update customer contact information in the LegaOnline system.

        Args:
            customer_contact (Optional[Any], optional): The customer contact object or data 
                structure containing contact information to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to be passed to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result 
                of the SetCustomerContact operation.

        Raises:
            May raise exceptions related to SOAP service calls depending on the underlying 
            _call implementation.
        """
        return self._call("SetCustomerContact", customerContact=customer_contact, **kwargs)

    def set_customer_contact_attributes(self, *, customer_contact_attribute: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set or update customer contact attributes in the LegaOnline system.

        Args:
            customer_contact_attribute (Optional[Any], optional): The customer contact attribute object or data 
                structure containing attribute information to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to be passed to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result 
                of the SetCustomerContactAttributes operation.

        Raises:
            May raise exceptions related to SOAP service calls depending on the underlying 
            _call implementation.
        """
        return self._call("SetCustomerContactAttributes", customerContactAttribute=customer_contact_attribute, **kwargs)

    def set_customer_contact_attributes_xml(self, *, customer_contact_attribute: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer contact attributes using XML format.

        This method calls the SOAP service operation "SetCustomerContactAttributesXml" to update
        customer contact attributes.

        Args:
            customer_contact_attribute (Optional[str], optional): XML string containing the customer 
                contact attributes to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service call containing the result
                of the operation.

        Raises:
            Any exceptions raised by the underlying _call method during SOAP communication.
        """
        return self._call("SetCustomerContactAttributesXml", customerContactAttribute=customer_contact_attribute, **kwargs)

    def set_customer_contact_v2(self, *, customer_contact: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer contact information using version 2 of the API.

        Args:
            customer_contact (Optional[Any], optional): The customer contact data to set.
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the
                SetCustomerContactV2 operation.
        """
        return self._call("SetCustomerContactV2", customerContact=customer_contact, **kwargs)

    def set_customer_contact_v2_xml(self, *, customer_contact: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer contact information using V2 XML format.

        Args:
            customer_contact (Optional[str], optional): The customer contact information in XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service call containing the result of setting customer contact information.
        """
        return self._call("SetCustomerContactV2Xml", customerContact=customer_contact, **kwargs)

    def set_customer_contact_xml(self, *, customer_contact: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer contact information using XML format.

        This method calls the SOAP service's SetCustomerContactXml operation to update
        customer contact details.

        Args:
            customer_contact (Optional[str], optional): XML string containing customer contact
                information. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: Response object from the SOAP service containing the result of
                the operation.
        """
        return self._call("SetCustomerContactXml", customerContact=customer_contact, **kwargs)

    def set_customer_shipping(self, *, customer_shipping_list: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer shipping information.

        Args:
            customer_shipping_list (Optional[Any], optional): A list or object containing customer shipping 
                information to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service call containing the result of the 
                SetCustomerShipping operation.

        Raises:
            May raise exceptions from the underlying SOAP service call depending on the implementation 
            of the _call method.
        """
        return self._call("SetCustomerShipping", customerShippingList=customer_shipping_list, **kwargs)

    def set_customer_shipping_and_pickup(self, *, customer_shipping_list: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer shipping and pickup information.

        Args:
            customer_shipping_list (Optional[Any], optional): The list of customer shipping and pickup details 
                to be set in the system. Defaults to None.
            **kwargs (Any): Additional keyword arguments to be passed to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result of the operation.

        Raises:
            Any exceptions raised by the underlying _call method during the SOAP service invocation.
        """
        return self._call("SetCustomerShippingAndPickup", customerShippingList=customer_shipping_list, **kwargs)

    def set_customer_v2(self, *, customer: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer information using the SetCustomerV2 SOAP method.

        Args:
            customer (Optional[Any], optional): The customer data to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP method.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("SetCustomerV2", customer=customer, **kwargs)

    def set_customer_v3(self, *, customer: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer information using the SetCustomerV3 SOAP method.

        Args:
            customer (Optional[Any], optional): The customer data to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP method.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("SetCustomerV3", customer=customer, **kwargs)

    def set_customer_v4(self, *, customer: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer information using the SetCustomerV4 SOAP method.

        Args:
            customer (Optional[Any], optional): The customer data to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP method.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("SetCustomerV4", customer=customer, **kwargs)

    def set_customer_v5(self, *, customer: Optional[Any] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer information using the SetCustomerV5 SOAP method.

        Args:
            customer (Optional[Any], optional): The customer data to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP method.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("SetCustomerV5", customer=customer, **kwargs)

    def set_customer_xml(self, *, customer: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Set customer information using the SetCustomerXml SOAP method.

        Args:
            customer (Optional[str], optional): The customer data in XML format to be set. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP method.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("SetCustomerXml", customer=customer, **kwargs)

    def set_master_customer_contact_id(
        self,
        *,
        customer_contact_id: int,
        master_customer_contact_id: int,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Sets the master customer contact ID for a given customer contact.

        This method associates a customer contact with a master customer contact by setting
        the master customer contact ID reference.

        Args:
            customer_contact_id (int): The ID of the customer contact to update.
            master_customer_contact_id (int): The ID of the master customer contact to associate with.
            **kwargs (Any): Additional optional parameters to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                          of the operation.
        """
        return self._call("SetMasterCustomerContactID", customerContactID=customer_contact_id, masterCustomerContactID=master_customer_contact_id, **kwargs)

    def set_master_customer_id(
        self,
        *,
        customer_id: int,
        master_customer_id: int,
        **kwargs: Any,
    ) -> SoapResponse:
        """
        Set the master customer ID for a customer.

        This method associates a customer with a master customer by setting the master customer ID.
        This is typically used in scenarios where customers have parent-child relationships or
        when managing customer hierarchies.

        Args:
            customer_id (int): The ID of the customer to set the master customer ID for.
            master_customer_id (int): The ID of the master customer to associate with the customer.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call( "SetMasterCustomerID", customerID=customer_id, masterCustomerID=master_customer_id, **kwargs)
