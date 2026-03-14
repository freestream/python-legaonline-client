from __future__ import annotations

import datetime as dt
from typing import Optional

from ..query import FilterSpec, IntListSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService

class CalendarService(BaseService):
    """
    Service class for interacting with calendar-related SOAP operations.

    This class provides methods to retrieve calendar data and user location information
    through various SOAP endpoints. It inherits from BaseService and manages calendar-specific
    operations.

    Methods:
        get_day_calendar_data: Retrieves calendar data for a specific day.
        get_day_calendar_data_v2: Retrieves calendar data using the V2 endpoint (newer version).
        get_user_location_xml: Retrieves user location data in XML format.
        get_user_location: Retrieves user location information.
    """
    __slots__ = ()

    def get_day_calendar_data(self, period_start: Optional[dt.date] = None, period_end: Optional[dt.date] = None, object_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Retrieves day calendar data from the SOAP service for a specified period and objects.

        Args:
            period_start (Optional[dt.date], optional): The start date of the period to retrieve calendar data for.
                If None, defaults to service-specific behavior. Defaults to None.
            period_end (Optional[dt.date], optional): The end date of the period to retrieve calendar data for.
                If None, defaults to service-specific behavior. Defaults to None.
            object_ids (Optional[IntListSpec], optional): List or specification of object IDs to retrieve calendar data for.
                If None, retrieves data for all available objects. Defaults to None.

        Returns:
            SoapResponse: The response object containing the day calendar data returned by the SOAP service.
        """
        return self._call("GetDayCalendarData", periodStart=period_start, periodEnd=period_end, objectIDs=object_ids.to_zeep() if object_ids else None)

    def get_day_calendar_data_v2(self, period_start: Optional[dt.date] = None, period_end: Optional[dt.date] = None, object_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Retrieves day calendar data using version 2 of the SOAP API method.

        Args:
            period_start (Optional[dt.date], optional): The start date of the period to retrieve calendar data for. Defaults to None.
            period_end (Optional[dt.date], optional): The end date of the period to retrieve calendar data for. Defaults to None.
            object_ids (Optional[IntListSpec], optional): List or specification of object IDs to retrieve calendar data for. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                          the day calendar data.
        """
        return self._call("GetDayCalendarDataV2", periodStart=period_start, periodEnd=period_end, objectIDs=object_ids.to_zeep() if object_ids else None)

    def get_user_location_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves user location data in XML format.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing user location data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetGetUserLocationXml", sort=sort_xml, filter=filter_xml)

    def get_user_location(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve user location information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response object containing user location data from the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetUserLocation", sort=sort_xml, filter=filter_xml)
