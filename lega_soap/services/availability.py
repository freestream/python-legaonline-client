from __future__ import annotations

import datetime as dt
from typing import Optional

from ..query import IntListSpec
from ..types import SoapResponse
from .base import BaseService

class AvailabilityService(BaseService):
    """
    Service for handling availability-related SOAP operations.

    This service provides methods to retrieve availability information from the SOAP API,
    either as structured data or in XML format.

    Attributes:
        Inherits all slots from BaseService (no additional slots defined).

    Methods:
        get_availability(object_ids, start_date, end_date) -> SoapResponse:
            Retrieves availability information by calling the GetAvailability SOAP method.

        get_availability_xml(object_ids, start_date, end_date) -> SoapResponse:
            Retrieves availability information in XML format by calling the
            GetAvailabilityXml SOAP method.
    """
    __slots__ = ()

    def get_availability(self, object_ids: Optional[IntListSpec] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None) -> SoapResponse:
        """
        Retrieve availability information from the SOAP service.

        This method calls the 'GetAvailability' SOAP operation to fetch availability data.

        Args:
            object_ids (Optional[IntListSpec], optional): List of object IDs to filter availability. Defaults to None.
            start_date (Optional[dt.date], optional): The start date for the availability range. Defaults to None.
            end_date (Optional[dt.date], optional): The end date for the availability range. Defaults to None.

        Returns:
            SoapResponse: The response object containing availability information returned
                by the SOAP service.
        """
        return self._call("GetAvailability", objectIDs=object_ids.to_zeep() if object_ids else None, startDate=start_date, endDate=end_date)

    def get_availability_xml(self, object_ids: Optional[IntListSpec] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None) -> SoapResponse:
        """
        Retrieve availability information in XML format from the SOAP service.

        This method calls the 'GetAvailabilityXml' SOAP operation and returns the response.

        Args:
            object_ids (Optional[IntListSpec], optional): List of object IDs to filter availability. Defaults to None.
            start_date (Optional[dt.date], optional): The start date for the availability range. Defaults to None.
            end_date (Optional[dt.date], optional): The end date for the availability range. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing availability data in XML format.
        """
        return self._call("GetAvailabilityXml", objectIDs=object_ids.to_zeep() if object_ids else None, startDate=start_date, endDate=end_date)
