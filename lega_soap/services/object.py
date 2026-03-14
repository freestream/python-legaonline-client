from __future__ import annotations

from typing import Optional

from ..query import FilterSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService


class ObjectService(BaseService):
    """
    Service class for handling object-related SOAP operations.
    This class provides methods to interact with various object-related endpoints in the SOAP API,
    including object images, seating information, packet members, rent objects, and room objects.
    All methods support optional sorting and filtering specifications.
    """
    __slots__ = ()

    def get_object_image(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve object image data from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the result set. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to apply to the query. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the object image data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectImage", sort=sort_xml, filter=filter_xml)

    def get_object_image_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve object image data in XML format with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response from the GetObjectImageXml SOAP operation containing
                the object image data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectImageXml", sort=sort_xml, filter=filter_xml)

    def get_object_seating(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve seating information for an object.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing seating information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectSeating", sort=sort_xml, filter=filter_xml)

    def get_object_seating_v2(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve seating information for an object using version 2 of the API.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the GetObjectSeatingV2 SOAP operation containing
                seating information for the requested object.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectSeatingV2", sort=sort_xml, filter=filter_xml)

    def get_object_seating_v2_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve object seating information in XML format using SOAP API version 2.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the seating information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectSeatingV2Xml", sort=sort_xml, filter=filter_xml)

    def get_object_seating_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves object seating information in XML format.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing object seating information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectSeatingXml", sort=sort_xml, filter=filter_xml)

    def get_packet_member(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve packet member information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing packet member data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetPacketMember", sort=sort_xml, filter=filter_xml)

    def get_packet_member_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves packet member data in XML format with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the packet member data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetPacketMemberXml", sort=sort_xml, filter=filter_xml)

    def get_rent_object(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve rent object information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing rent object data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRentObject", sort=sort_xml, filter=filter_xml)

    def get_rent_object_v2(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve rent object information using the V2 API endpoint.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification object. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object. Defaults to None.

        Returns:
            SoapResponse: The response object from the GetRentObjectV2 SOAP service call containing
                rent object information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRentObjectV2", sort=sort_xml, filter=filter_xml)

    def get_rent_object_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve rent object data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML and passed to the SOAP service. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML and passed to the SOAP service. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing rent object
                data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRentObjectXml", sort=sort_xml, filter=filter_xml)

    def get_room_object(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve room object data from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the query results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to filter query results. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing room object data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRoomObject", sort=sort_xml, filter=filter_xml)

    def get_room_object_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve room object data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing room object data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRoomObjectXml", sort=sort_xml, filter=filter_xml)

    def get_seating(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve seating information with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the GetSeating SOAP operation containing
                seating information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetSeating", sort=sort_xml, filter=filter_xml)

    def get_seating_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve seating information in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the seating results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the seating results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing seating
                information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetSeatingXml", sort=sort_xml, filter=filter_xml)
