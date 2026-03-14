from __future__ import annotations

from typing import Optional

from ..query import OrderInfoSpec
from ..types import SoapResponse
from .base import BaseService

class IntegrationService(BaseService):
    """
    IntegrationService provides methods for interacting with the integration SOAP service,
    specifically for creating Miljobud orders.

    Methods:
        integration_create_miljobud_order(fleet_101_auth_token, order_info):
            Creates a Miljobud order via the integration service.

        integration_create_miljobud_order_xml(fleet_101_auth_token, order_info):
            Creates a Miljobud order XML via the integration service.
    """
    __slots__ = ()

    def integration_create_miljobud_order(self, fleet_101_auth_token: Optional[str] = None, order_info: Optional[OrderInfoSpec] = None) -> SoapResponse:
        """
        Creates a Miljobud order by calling the 'IntegrationCreateMiljobudOrder' SOAP method.

        Args:
            fleet_101_auth_token (Optional[str], optional): Authentication token for Fleet101. Defaults to None.
            order_info (Optional[OrderInfoSpec], optional): Order information to be sent, as an OrderInfoSpec object. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service.
        """
        order_info_xml = order_info.to_xml() if order_info else ""
        return self._call("IntegrationCreateMiljobudOrder", fleet101AuthToken=fleet_101_auth_token, orderInfo=order_info_xml)

    def integration_create_miljobud_order_xml(self, fleet_101_auth_token: Optional[str] = None, order_info: Optional[OrderInfoSpec] = None) -> SoapResponse:
        """
        Creates a Miljobud order XML via the integration service.

        This method calls the "IntegrationCreateMiljobudOrderXml" SOAP operation.

        Args:
            fleet_101_auth_token (Optional[str], optional): Authentication token for Fleet101. Defaults to None.
            order_info (Optional[OrderInfoSpec], optional): Order information to be sent, as an OrderInfoSpec object. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service.
        """
        order_info_xml = order_info.to_xml() if order_info else ""
        return self._call("IntegrationCreateMiljobudOrderXml", fleet101AuthToken=fleet_101_auth_token, orderInfo=order_info_xml)
