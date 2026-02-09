from __future__ import annotations

from typing import Any, Optional

from ..query import FilterSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService


class ObjectService(BaseService):
    """
    Service class for handling object-related SOAP operations.
    This class provides methods to interact with various object-related endpoints in the SOAP API,
    including object images, seating information, packet members, rent objects, and room objects.
    All methods support optional sorting and filtering specifications.
    The service handles the following types of operations:
        - Object image retrieval (standard and XML formats)
        - Seating information retrieval (multiple versions and formats)
        - Packet member data access
        - Rent object queries (multiple versions and formats)
        - Room object data retrieval
        - General seating queries
    Each method converts SortSpec and FilterSpec objects to XML format before making the SOAP call.
    Inherits:
        BaseService: Base class providing core SOAP service functionality.
    Attributes:
        __slots__ (tuple): Empty tuple to prevent dynamic attribute assignment for memory optimization.
    """
    __slots__ = ()

    def get_object_image(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve object image data from the SOAP service.

        This method calls the GetObjectImage SOAP operation with optional sorting and filtering parameters.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification for the result set. 
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to apply to the query. 
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the object image data.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_object_image(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectImage", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_image_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve object image data in XML format with optional sorting and filtering.

        Args:
            *args: Variable length argument list passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results. 
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. 
                Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The response from the GetObjectImageXml SOAP operation containing 
                the object image data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectImageXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_seating(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve seating information for an object.

        This method calls the SOAP service's GetObjectSeating operation with optional
        sorting and filtering parameters.

        Args:
            *args: Variable length argument list passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing seating information.

        Examples:
            >>> # Get seating without sorting or filtering
            >>> response = service.get_object_seating()
            >>> 
            >>> # Get seating with custom sorting
            >>> sort_spec = SortSpec(field="seat_number", order="asc")
            >>> response = service.get_object_seating(sorting=sort_spec)
            >>> 
            >>> # Get seating with filtering and sorting
            >>> filter_spec = FilterSpec(section="A")
            >>> response = service.get_object_seating(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectSeating", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_seating_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve seating information for an object using version 2 of the API.

        This method calls the GetObjectSeatingV2 SOAP operation with optional sorting
        and filtering specifications.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the GetObjectSeatingV2 SOAP operation containing
                seating information for the requested object.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectSeatingV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_seating_v2_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve object seating information in XML format using SOAP API version 2.

        This method calls the GetObjectSeatingV2Xml SOAP service with optional sorting
        and filtering specifications.

        Args:
            *args (Any): Variable positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Variable keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the seating information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectSeatingV2Xml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_seating_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves object seating information in XML format.

        Args:
            *args: Variable length argument list passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing object seating information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectSeatingXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_packet_member(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve packet member information from the SOAP service.

        This method calls the GetPacketMember SOAP operation with optional sorting
        and filtering specifications.

        Args:
            *args: Variable length argument list passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing packet member data.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_packet_member(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetPacketMember", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_packet_member_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves packet member data in XML format with optional sorting and filtering.

        This method calls the SOAP service's 'GetPacketMemberXml' operation to fetch
        packet member information. The response can be customized using sorting and
        filtering specifications.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the packet member data in XML format.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_packet_member_xml(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetPacketMemberXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_rent_object(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve rent object information from the SOAP service.

        This method fetches rent object data by calling the 'GetRentObject' SOAP operation
        with optional sorting and filtering parameters.

        Args:
            *args (Any): Variable positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs (Any): Variable keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing rent object data.

        Example:
            >>> service = ObjectService()
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_rent_object(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRentObject", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_rent_object_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve rent object information using the V2 API endpoint.

        This method calls the GetRentObjectV2 SOAP service with optional sorting and filtering parameters.

        Args:
            *args (Any): Variable length argument list passed to the SOAP service call.
            sorting (Optional[SortSpec], optional): Sorting specification object that defines how results 
                should be sorted. Will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that defines which 
                results should be included. Will be converted to XML format. Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments passed to the SOAP service call.

        Returns:
            SoapResponse: The response object from the GetRentObjectV2 SOAP service call containing 
                rent object information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRentObjectV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_rent_object_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve rent object data in XML format from the SOAP service.

        This method calls the GetRentObjectXml SOAP operation with optional sorting
        and filtering parameters.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML and passed to the SOAP service.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML and passed to the SOAP service.
                Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing rent object
                data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRentObjectXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_room_object(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve room object data from the SOAP service.

        This method calls the 'GetRoomObject' SOAP operation with optional sorting and filtering parameters.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification for the query results. 
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to filter query results. 
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing room object data.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_room_object(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRoomObject", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_room_object_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve room object data in XML format from the SOAP service.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results. 
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. 
                Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing room object data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetRoomObjectXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_seating(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve seating information with optional sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): Specification for sorting the results. 
                If provided, will be converted to XML format.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If provided, will be converted to XML format.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the GetSeating SOAP operation containing
                seating information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetSeating", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_seating_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve seating information in XML format from the SOAP service.

        This method calls the 'GetSeatingXml' SOAP operation with optional sorting
        and filtering specifications.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting: Optional sorting specification to order the seating results.
                If provided, will be converted to XML format.
            filtering: Optional filtering specification to filter the seating results.
                If provided, will be converted to XML format.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing seating
                information in XML format.

        Example:
            >>> service.get_seating_xml(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetSeatingXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)
