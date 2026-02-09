from __future__ import annotations

from typing import Any, Optional

from lega_soap.query import FilterSpec, SortSpec

from ..types import SoapResponse
from .base import BaseService

class ShippingService(BaseService):
    """
    Service class for interacting with shipping methods via SOAP API.

    This class provides methods to retrieve shipping method information, either as structured data or in XML format, by making SOAP calls to the backend service.

    Methods:
        get_shipping_method(*args, shipping_method_id=None, shipping_method_name=None, shipping_method_description=None, **kwargs)

        get_shipping_method_xml(*args, sorting=None, filtering=None, **kwargs)
            Retrieves shipping method information in XML format, with optional sorting and filtering specifications.
    """
    __slots__ = ()

    def get_shipping_method(self, *args: Any, shipping_method_id: Any = Optional[int], shipping_method_name: Any = Optional[str], shipping_method_description: Any = Optional[str], **kwargs: Any) -> SoapResponse:
        """
        Retrieves shipping method information using the provided parameters.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            shipping_method_id (Optional[int], optional): The unique identifier of the shipping method. Defaults to None.
            shipping_method_name (Optional[str], optional): The name of the shipping method. Defaults to None.
            shipping_method_description (Optional[str], optional): The description of the shipping method. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the shipping method details.
        """
        return self._call("GetShippingMethod", *args, ShippingMethodID=shipping_method_id, ShippingMethodName=shipping_method_name, ShippingMethodDescription=shipping_method_description, **kwargs)

    def get_shipping_method_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves shipping method information in XML format via a SOAP call.

        Args:
            *args (Any): Positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification to apply to the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to apply to the results. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing shipping method information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetShippingMethodXml", *args, sort=sort_xml, filter=filter_xml, **kwargs)
