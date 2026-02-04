from __future__ import annotations

import datetime as dt
from typing import Optional, Any

from .base import BaseService
from ..query import FilterSpec, SortSpec
from ..types import SoapResponse

class CustomerService(BaseService):
    """
    Service class for managing customer-related operations.

    This class provides methods to interact with customer data through a ZEEP SOAP service.
    It extends BaseService and handles customer retrieval with optional sorting, filtering,
    and attribute inclusion.

    Args:
        zeep_service: The ZEEP service client for making SOAP requests.
        auth_manager: Manager for handling authentication and authorization.
        tzinfo (dt.tzinfo): Timezone information for datetime operations.

    Methods:
        get_customer: Retrieves customer data with optional sorting, filtering, and attributes.
    """
    def __init__(
        self,
        zeep_service: Any,
        auth_manager: Any,
        tzinfo: dt.tzinfo,
    ) -> None:
        super().__init__(zeep_service, auth_manager, tzinfo)

    def get_customer(
        self,
        *,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ) -> SoapResponse:
        """
        Retrieve customer information from the SOAP service.

        This method fetches customer data with optional sorting, filtering, and attribute inclusion.
        It constructs the necessary XML elements for sorting and filtering specifications before
        making the SOAP call.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the customer results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the customer results.
                If provided, it will be converted to XML format. Defaults to None.
            include_attributes (bool, optional): Flag to indicate whether to include customer attributes
                in the response. Defaults to False.

        Returns:
            SoapResponse: The response object from the SOAP service containing the customer data.

        Example:
            >>> customer_service.get_customer(
            ...     sorting=SortSpec(field="name", order="asc"),
            ...     filtering=FilterSpec(field="status", value="active"),
            ...     include_attributes=True
            ... )
        """
        
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""

        return self._call("GetCustomer", sort_xml, filter_xml, include_attributes)
