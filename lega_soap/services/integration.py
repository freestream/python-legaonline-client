from __future__ import annotations

from typing import Any, Optional

from ..query import OrderInfoSpec
from ..types import SoapResponse
from .base import BaseService

class IntegrationService(BaseService):
    """
    IntegrationService provides methods for interacting with the integration SOAP service, specifically for creating Miljobud orders.

    Methods:
        integration_create_miljobud_order(*args, fleet_101_auth_token, order_info, **kwargs):
            - *args: Additional positional arguments for the SOAP call.
            - fleet_101_auth_token (Optional[str]): Authentication token for Fleet101.
            - order_info (Optional[OrderInfoSpec]): Order information as an OrderInfoSpec object.
            - **kwargs: Additional keyword arguments for the SOAP call.

        integration_create_miljobud_order_xml(*args, fleet_101_auth_token, **kwargs):
            Creates a Miljobud order XML via the integration service by calling the 'IntegrationCreateMiljobudOrderXml' SOAP operation.
            - *args: Positional arguments for the SOAP call.
            - fleet_101_auth_token (Optional[str]): Authentication token for Fleet101.
            - **kwargs: Additional keyword arguments for the SOAP call.
    """
    __slots__ = ()

    def integration_create_miljobud_order(self, *args: Any, fleet_101_auth_token: Optional[str], order_info: Optional[OrderInfoSpec], **kwargs: Any) -> SoapResponse:
        """
        Creates a Miljobud order by calling the 'IntegrationCreateMiljobudOrder' SOAP method.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            fleet_101_auth_token (Optional[str]): Authentication token for Fleet101.
            order_info (Optional[OrderInfoSpec]): Order information to be sent, as an OrderInfoSpec object.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service.

        """
        order_info_xml = order_info.to_xml() if order_info else ""
        return self._call("IntegrationCreateMiljobudOrder", *args, fleet101AuthToken=fleet_101_auth_token, orderInfo=order_info_xml, **kwargs)

    def integration_create_miljobud_order_xml(self, *args: Any, fleet_101_auth_token: Optional[str], **kwargs: Any) -> SoapResponse:
        """
        Creates a Miljobud order XML via the integration service.

        This method calls the "IntegrationCreateMiljobudOrderXml" SOAP operation, passing the provided arguments and authentication token.

        Args:
            *args (Any): Positional arguments to pass to the SOAP call.
            fleet_101_auth_token (Optional[str]): Authentication token for Fleet101.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service.
        """
        return self._call("IntegrationCreateMiljobudOrderXml", *args, fleet101AuthToken=fleet_101_auth_token, **kwargs)