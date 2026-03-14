from __future__ import annotations

from typing import Optional

from lega_soap.query import FilterSpec, SortSpec

from ..types import SoapResponse
from .base import BaseService

class ShippingService(BaseService):
    """
    Service class for interacting with shipping methods via SOAP API.

    This class provides methods to retrieve shipping method information, either as structured data
    or in XML format, by making SOAP calls to the backend service.

    Methods:
        get_shipping_method(sorting, filtering): Retrieve shipping methods with optional sorting and filtering.
        get_shipping_method_xml(sorting, filtering): Retrieve shipping methods in XML format.
    """
    __slots__ = ()

    def get_shipping_method(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves shipping method information using optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results. Defaults to None.

        Returns:
            SoapResponse: The response object containing the shipping method details.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetShippingMethod", sort=sort_xml, filter=filter_xml)

    def get_shipping_method_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves shipping method information in XML format via a SOAP call.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification to apply to the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to apply to the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing shipping method information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetShippingMethodXml", sort=sort_xml, filter=filter_xml)
