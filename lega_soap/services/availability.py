from __future__ import annotations

import datetime as dt
from typing import Any, Optional

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

    Args:
        zeep_service (Any): The Zeep SOAP service client instance.
        auth_manager (Any): The authentication manager for handling credentials.
        tzinfo (dt.tzinfo): Timezone information for datetime operations.

    Methods:
        get_availability(*args, **kwargs) -> SoapResponse:
            Retrieves availability information by calling the GetAvailability SOAP method.
            
        get_availability_xml(*args, **kwargs) -> SoapResponse:
            Retrieves availability information in XML format by calling the 
            GetAvailabilityXml SOAP method.
    """
    __slots__ = ()

    def get_availability(self, *, object_ids: Optional[IntListSpec] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve availability information from the SOAP service.

        This method calls the 'GetAvailability' SOAP operation to fetch availability data.

        Args:
            object_ids (Optional[IntListSpec], optional): List of object IDs to filter availability. Defaults to None.
            start_date (Optional[dt.date], optional): The start date for the availability range. Defaults to None.
            end_date (Optional[dt.date], optional): The end date for the availability range. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing availability information returned
                by the SOAP service.

        Raises:
            May raise exceptions from the underlying SOAP client depending on the
            implementation of _call method (e.g., connection errors, SOAP faults).
        """
        return self._call("GetAvailability", objectIDs=object_ids, startDate=start_date, endDate=end_date, **kwargs)

    def get_availability_xml(self, *, object_ids: Optional[IntListSpec] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve availability information in XML format from the SOAP service.

        This method calls the 'GetAvailabilityXml' SOAP operation and returns the response.

        Args:
            object_ids (Optional[IntListSpec], optional): List of object IDs to filter availability. Defaults to None.
            start_date (Optional[dt.date], optional): The start date for the availability range. Defaults to None.
            end_date (Optional[dt.date], optional): The end date for the availability range. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing availability data in XML format.

        Raises:
            May raise exceptions related to SOAP communication errors or service-specific errors
            depending on the implementation of the _call method.
        """
        return self._call("GetAvailabilityXml", objectIDs=object_ids, startDate=start_date, endDate=end_date, **kwargs)
