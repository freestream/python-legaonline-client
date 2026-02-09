from __future__ import annotations

import datetime as dt
from typing import Any, Optional

from ..query import (
    IntListSpec,
    SortSpec,
    FilterSpec,
    OccasionAnswerSpec,
    OccasionQuantitySpec,
    OccasionLocationSpec,
    OccasionSeatingInfoSpec,
    OccasionObjectAnswerSpec,
    OccasionParticipantNumberSpec,
    XmlArray
)
from ..types import SoapResponse
from .base import BaseService


class OccasionService(BaseService):
    """
    Service class for managing occasion-related operations in the LegaOnline SOAP API.

    This class provides methods to interact with occasion data, including creating, updating,
    retrieving, and managing various aspects of occasions such as accessories, answers, locations,
    seating, and participant information. It supports multiple versions of API endpoints and
    offers flexible filtering and sorting capabilities.

    The OccasionService inherits from BaseService and provides a comprehensive interface for:
    - Creating and managing occasions (regular and preliminary)
    - Activating, canceling, and returning occasions
    - Managing occasion accessories, answers, locations, and seating arrangements
    - Retrieving occasion data with various filtering and sorting options
    - Handling participant numbers and quantities
    - Updating occasion dates and statuses
    - Checking availability with occasion exclusions

    All methods return SoapResponse objects containing the results of the SOAP operations.
    Most retrieval methods support optional SortSpec and FilterSpec parameters for customizing
    query results, and many operations are available in multiple API versions (V2, V3, V4) and
    XML variants.

        >>> # Create a new occasion
        >>> response = service.create_occasion(
        ...     reservation_id=123,
        ...     customer_id=456,
        ...     start_date=date(2024, 1, 1),
        ...     end_date=date(2024, 1, 5)
        >>> # Retrieve occasions with filtering
        >>> occasions = service.get_occasion_v4(filtering=filter_spec)

    Attributes:
        Inherits all attributes from BaseService.

        This class uses __slots__ = () for memory efficiency, preventing dynamic attribute assignment.
    """
    __slots__ = ()

    def activate_occasion(self, *, occasion_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Activate one or more occasions.
        Args:
            occasion_ids: Optional specification of occasion IDs to activate. If None,
                no ID list is included in the SOAP request.
        Returns:
            SoapResponse: The response from the SOAP service containing the result
                of the activation operation.
        Example:
            >>> service = OccasionService()
            >>> int_list = IntListSpec(ids=[123, 456])
            >>> response = service.activate_occasion(occasion_ids=int_list)
        """
        occasion_ids_xml = occasion_ids.to_xml() if occasion_ids else ""

        return self._call("ActivateOccasion", occasionIDs=occasion_ids_xml)

    def add_occasion_accessory(self, occasion_id: Optional[int] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, status_id: Optional[int] = None, object_id: Optional[int] = None, quantity: Optional[int] = None) -> SoapResponse:
        """
        Add an accessory to an occasion.

        Args:
            occasion_id (Optional[int], optional): The ID of the occasion to add the accessory to. Defaults to None.
            start_date (Optional[dt.date], optional): The start date for the accessory. Defaults to None.
            end_date (Optional[dt.date], optional): The end date for the accessory. Defaults to None.
            status_id (Optional[int], optional): The status ID for the accessory. Defaults to None.
            object_id (Optional[int], optional): The ID of the accessory object to add. Defaults to None.
            quantity (Optional[int], optional): The quantity of the accessory to add. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service call.
        """

        return self._call("AddOccasionAccessory", OccasionID=occasion_id, StartDate=start_date, EndDate=end_date, StatusID=status_id, ObjectID=object_id, Quantity=quantity)

    def cancel_occasion(self, occasion_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Cancel one or more occasions.
        Args:
            occasion_ids (Optional[IntListSpec], optional): A specification containing a list of
                occasion IDs to cancel. If None, no occasions will be cancelled. Defaults to None.
        Returns:
            SoapResponse: The SOAP response from the CancelOccasion operation.
        Raises:
            May raise exceptions related to SOAP communication or XML processing depending on
            the implementation of _call() and IntListSpec.to_xml().
        """
        occasion_ids_xml = occasion_ids.to_xml() if occasion_ids else ""

        return self._call("CancelOccasion", occasionIDs=occasion_ids_xml)

    def create_occasion(self, reservation_id: Optional[int] = None, occasion_id: Optional[int] = None, customer_id: Optional[int] = None, customer_contact_id: Optional[int] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, quantity: Optional[int] = None) -> SoapResponse:
        """
        Creates a new occasion.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation to associate with the occasion. Defaults to None.
            occasion_id (Optional[int], optional): The ID of the occasion to create or update. Defaults to None.
            customer_id (Optional[int], optional): The ID of the customer associated with the occasion. Defaults to None.
            customer_contact_id (Optional[int], optional): The ID of the customer contact associated with the occasion. Defaults to None.
            start_date (Optional[dt.date], optional): The start date of the occasion. Defaults to None.
            end_date (Optional[dt.date], optional): The end date of the occasion. Defaults to None.
            quantity (Optional[int], optional): The quantity for the occasion. Defaults to None.

        Returns:
            SoapResponse: The SOAP response object containing the result of the CreateOccasion operation.
        """
        return self._call("CreateOccasion", reservationID=reservation_id, OccasionID=occasion_id, CustomerID=customer_id, CustomerContactID=customer_contact_id, StartDate=start_date, EndDate=end_date, Quantity=quantity)

    def create_preliminary_occasion(self, reservation_id: Optional[int] = None, occasion_id: Optional[int] = None, customer_id: Optional[int] = None, customer_contact_id: Optional[int] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, quantity: Optional[int] = None) -> SoapResponse:
        """
        Create a preliminary occasion.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation. Defaults to None.
            occasion_id (Optional[int], optional): The ID of the occasion. Defaults to None.
            customer_id (Optional[int], optional): The ID of the customer. Defaults to None.
            customer_contact_id (Optional[int], optional): The ID of the customer contact. Defaults to None.
            start_date (Optional[dt.date], optional): The start date of the occasion. Defaults to None.
            end_date (Optional[dt.date], optional): The end date of the occasion. Defaults to None.
            quantity (Optional[int], optional): The quantity for the occasion. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service call.
        """
        return self._call("CreatePreliminaryOccasion", reservationID=reservation_id, OccasionID=occasion_id, CustomerID=customer_id, CustomerContactID=customer_contact_id, StartDate=start_date, EndDate=end_date, Quantity=quantity)

    def get_availability_exclude_occasion(self, *args: Any, occasion_ids: Optional[IntListSpec] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, exclude_occasion_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Get availability for occasions excluding a specific occasion.

        This method retrieves availability information for a set of occasions within a specified
        date range, while excluding data for a particular occasion ID.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            occasion_ids (Optional[IntListSpec], optional): List specification of occasion IDs to check
                availability for. Defaults to None.
            start_date (Optional[dt.date], optional): Start date for the availability query.
                Defaults to None.
            end_date (Optional[dt.date], optional): End date for the availability query.
                Defaults to None.
            exclude_occasion_id (Optional[int], optional): The occasion ID to exclude from the results.
                Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The SOAP response containing availability information for the requested
                occasions, excluding the specified occasion.
        """
        occasion_ids_xml = occasion_ids.to_xml() if occasion_ids else ""
        return self._call("GetAvailabilityExcludeOccasion", occasionIDs=occasion_ids_xml, StartDate=start_date, EndDate=end_date, ExcludeOccasionID=exclude_occasion_id, *args, **kwargs)

    def get_availability_exclude_occasion_xml(self, *args: Any, occasion_ids: Optional[IntListSpec] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, exclude_occasion_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Get availability for occasions excluding a specific occasion, returned as XML.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            occasion_ids (Optional[IntListSpec], optional): List specification of occasion IDs to check availability for.
                Defaults to None.
            start_date (Optional[dt.date], optional): Start date for the availability period. Defaults to None.
            end_date (Optional[dt.date], optional): End date for the availability period. Defaults to None.
            exclude_occasion_id (Optional[int], optional): ID of the occasion to exclude from availability check.
                Defaults to None.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: SOAP response containing availability information in XML format.
        """
        occasion_ids_xml = occasion_ids.to_xml() if occasion_ids else ""
        return self._call("GetAvailabilityExcludeOccasionXml", occasionIDs=occasion_ids_xml, StartDate=start_date, EndDate=end_date, ExcludeOccasionID=exclude_occasion_id, *args, **kwargs)

    def get_occasion(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion data from the SOAP service with optional sorting and filtering.

        This method calls the 'GetOccasion' SOAP endpoint to fetch occasion information.
        It supports flexible sorting and filtering capabilities through SortSpec and FilterSpec objects.

        Args:
            *args (Any): Variable positional arguments to be passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Variable keyword arguments to be passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion data.

        Example:
            >>> sort_spec = SortSpec(field="date", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_occasion(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasion", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_answer(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion answers from the SOAP service with optional sorting and filtering.

        This method calls the 'GetOccasionAnswer' SOAP operation and allows for customizable
        sorting and filtering of the results.

        Args:
            *args (Any): Variable length argument list passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification to apply to the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to apply to the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The response object containing the occasion answer data from the SOAP service.

        Example:
            >>> service = OccasionService()
            >>> sort_spec = SortSpec(field="date", order="desc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_occasion_answer(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionAnswer", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_answer_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves occasion answers using the GetOccasionAnswerV2 SOAP service.

        This method allows fetching occasion answer data with optional sorting and filtering
        capabilities. The sorting and filtering specifications are converted to XML format
        before being passed to the SOAP service.

        Args:
            *args (Any): Variable positional arguments to be passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs (Any): Variable keyword arguments to be passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion
                answer data.

        Example:
            >>> sort_spec = SortSpec(field="date", order="asc")
            >>> filter_spec = FilterSpec(status="active")
            >>> response = service.get_occasion_answer_v2(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionAnswerV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_answer_v2_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion answers in XML format using version 2 of the API.

        This method calls the GetOccasionAnswerV2Xml SOAP operation with optional
        sorting and filtering specifications. The sorting and filtering objects are
        converted to their XML representations before being passed to the service.

        Args:
            *args: Variable length argument list to be passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification to order the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to filter the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments to be passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the
                occasion answers in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionAnswerV2Xml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_answer_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves occasion answer data in XML format via SOAP service call.

        This method calls the GetOccasionAnswerXml SOAP endpoint with optional sorting
        and filtering parameters. The sorting and filtering specifications are converted
        to XML format before being passed to the underlying SOAP service.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting: Optional sorting specification that defines how results should be ordered.
                     If provided, it will be converted to XML format.
            filtering: Optional filtering specification that defines which results to include.
                       If provided, it will be converted to XML format.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion
                          answer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionAnswerXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_location(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion location information from the SOAP service.

        This method calls the GetOccasionLocation SOAP operation with optional sorting
        and filtering parameters.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                occasion location data.

        Example:
            >>> service = OccasionService()
            >>> response = service.get_occasion_location(
            ...     sorting=SortSpec(field="name", order="asc"),
            ...     filtering=FilterSpec(field="active", value=True)
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionLocation", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_location_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves occasion location data in XML format from the SOAP service.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting (Optional[SortSpec]): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion
                location data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionLocationXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_participant_number(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion participant numbers from the SOAP service.

        This method calls the GetOccasionParticipantNumber SOAP operation with optional
        sorting and filtering specifications.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting: Optional sorting specification to order the results.
            filtering: Optional filtering specification to filter the results.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion
                participant number data.

        Example:
            >>> sort_spec = SortSpec(field="participantNumber", order="asc")
            >>> filter_spec = FilterSpec(field="occasionId", value="123")
            >>> response = service.get_occasion_participant_number(
            ...     sorting=sort_spec,
            ...     filtering=filter_spec
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionParticipantNumber", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_participant_number_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion participant numbers in XML format.

        Args:
            *args: Variable length argument list to pass to the SOAP service.
            sorting: Optional sorting specification to apply to the results.
            filtering: Optional filtering specification to apply to the results.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP service.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion
                          participant numbers in XML format.

        Note:
            Both sorting and filtering specifications are converted to XML format
            before being passed to the GetOccasionParticipantNumberXml SOAP method.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionParticipantNumberXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_questions(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion questions with optional sorting and filtering.

        This method calls the SOAP service to fetch occasion participant number data
        in XML format, applying any specified sorting and filtering criteria.

        Args:
            *args (Any): Variable length argument list passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification to order the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to filter the results.
                Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object containing the occasion questions data.

        Example:
            >>> sort_spec = SortSpec(field="date", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_occasion_questions(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionQuestions", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_questions_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves occasion questions using version 2 of the API with optional sorting and filtering.

        Args:
            *args (Any): Variable length argument list to be passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments to be passed to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing the occasion questions data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionQuestionsV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_questions_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion questions in XML format with optional sorting and filtering.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            sorting (Optional[SortSpec]): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion questions data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionQuestionsXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_seating(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve seating information for an occasion.

        This method calls the SOAP service's GetOccasionSeating operation with optional
        sorting and filtering parameters.

        Args:
            *args: Variable length argument list passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion seating data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionSeating", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_seating_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve seating information for an occasion in XML format.

        This method calls the SOAP service's GetOccasionSeatingXml operation with optional
        sorting and filtering specifications.

        Args:
            *args: Variable length argument list passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the seating data.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the seating data.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion seating
                information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionSeatingXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion data using the GetOccasionV2 SOAP operation.

        This method calls the GetOccasionV2 SOAP service with optional sorting and filtering
        specifications. The sorting and filtering parameters are converted to XML format before
        being passed to the SOAP service.

        Args:
            *args: Variable length argument list to be passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification object that defines
                how the results should be ordered. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that
                defines what results should be included. Defaults to None.
            **kwargs: Arbitrary keyword arguments to be passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion data.

        Example:
            >>> service = OccasionService()
            >>> response = service.get_occasion_v2(
            ...     sorting=SortSpec(field="date", order="asc"),
            ...     filtering=FilterSpec(status="active")
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_v2_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion data in XML format using the V2 API endpoint with optional sorting and filtering.

        Args:
            *args: Variable length argument list to pass to the underlying SOAP call.
            sorting: Optional SortSpec object that defines the sorting criteria for the results.
                If provided, it will be converted to XML format.
            filtering: Optional FilterSpec object that defines the filtering criteria for the results.
                If provided, it will be converted to XML format.
            **kwargs: Arbitrary keyword arguments to pass to the underlying SOAP call.

        Returns:
            SoapResponse: The SOAP response object containing the occasion data in XML format.

        Note:
            This method calls the "GetOccasionV2Xml" SOAP operation with the specified
            sorting and filtering parameters converted to their XML representations.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV2Xml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_v3(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion data using the GetOccasionV3 SOAP operation.

        This method calls the GetOccasionV3 SOAP service with optional sorting and filtering
        specifications. The sorting and filtering parameters are converted to XML format before
        being passed to the underlying SOAP call.

        Args:
            *args: Variable length argument list to be passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments to be passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing occasion data.

        Example:
            >>> sort_spec = SortSpec(field="date", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_occasion_v3(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV3", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_v3_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion data in XML format using the GetOccasionV3Xml SOAP method.

        This method calls the GetOccasionV3Xml SOAP endpoint with optional sorting and filtering
        specifications. The sorting and filtering objects are converted to their XML representations
        before being passed to the underlying SOAP call.

        Args:
            *args (Any): Variable length argument list passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification object that defines how
                the results should be sorted. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that defines
                how the results should be filtered. Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion data
                in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV3Xml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_v4(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion data using version 4 of the GetOccasion SOAP method.

        This method calls the GetOccasionV4 SOAP endpoint with optional sorting and filtering
        parameters. The sorting and filtering specifications are converted to XML format before
        being passed to the SOAP service.

        Args:
            *args: Variable length argument list to be passed to the SOAP call.
            sorting: Optional sorting specification that defines how results should be ordered.
                If provided, it will be converted to XML format.
            filtering: Optional filtering specification that defines which results should be included.
                If provided, it will be converted to XML format.
            **kwargs: Arbitrary keyword arguments to be passed to the SOAP call.

        Returns:
            SoapResponse: The response object containing the result from the GetOccasionV4 SOAP call.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV4", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_v4_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion data in XML format using the V4 API endpoint.

        This method calls the GetOccasionV4Xml SOAP operation with optional sorting
        and filtering specifications.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            sorting: Optional sorting specification to order the results. If provided,
                it will be converted to XML format.
            filtering: Optional filtering specification to filter the results. If provided,
                it will be converted to XML format.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object containing the XML data for occasions
                matching the specified criteria.

        Example:
            >>> sort_spec = SortSpec(field="date", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_occasion_v4_xml(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV4Xml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_occasion_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve occasion data in XML format from the SOAP service.

        This method calls the GetOccasionXml SOAP operation with optional sorting and filtering parameters.
        The sorting and filtering specifications are converted to XML format before being passed to the service.

        Args:
            *args: Variable length argument list to pass to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing occasion data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def return_occasion(self, *args: Any, occasion_ids: Optional[IntListSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Return occasion information from the LEGA system.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            occasion_ids: Optional specification of occasion IDs to return. If provided,
                will be converted to XML format for the SOAP request. If None, all occasions
                may be returned (depending on service implementation).
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response from the ReturnOccasion SOAP service containing
                the requested occasion information.
        """
        occasion_ids_xml = occasion_ids.to_xml() if occasion_ids else ""
        return self._call("ReturnOccasion", occasion_ids=occasion_ids_xml, *args, **kwargs)

    def set_occasion_answer(self, *args: Any, occasion_answers: Optional[XmlArray[OccasionAnswerSpec]] = None, **kwargs: Any) -> SoapResponse:
        """
        Set answers for one or more occasions.

        This method calls the SetOccasionAnswer SOAP operation to submit answers for occasions.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            occasion_answers: An optional XmlArray of OccasionAnswerSpec objects containing
                the answers to set for occasions. If None, an empty string is passed.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service after setting the occasion answers.

        Example:
            >>> service.set_occasion_answer(occasion_answers=occasion_answers_array)
        """
        occasion_answers_xml = occasion_answers.to_xml() if occasion_answers else ""
        return self._call("SetOccasionAnswer", occasion_answers=occasion_answers_xml, *args, **kwargs)

    def set_occasion_location(self, *args: Any, occasion_location: Optional[XmlArray[OccasionLocationSpec]] = None, **kwargs: Any) -> SoapResponse:
        """
        Set the location for an occasion.

        This method calls the SOAP service's SetOccasionLocation operation to configure
        or update the location information for a given occasion.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            occasion_location: Optional XML array of OccasionLocationSpec objects containing
                the location details to set. If None, an empty string is passed.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the
                operation.

        Example:
            >>> service.set_occasion_location(occasion_location=location_specs)
        """
        occasion_location_xml = occasion_location.to_xml() if occasion_location else ""
        return self._call("SetOccasionLocation", occasion_location=occasion_location_xml, *args, **kwargs)

    def set_occasion_object_answer(self, *args: Any, occasion_object_answer: Optional[XmlArray[OccasionObjectAnswerSpec]] = None, **kwargs: Any) -> SoapResponse:
        """
        Set occasion object answer via SOAP service.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            occasion_object_answer: Optional array of OccasionObjectAnswerSpec objects to be set.
                If provided, will be converted to XML format before sending.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service call.

        Note:
            This method calls the "SetOccasionObjectAnswer" SOAP operation with the
            serialized occasion object answer data.
        """
        occasion_object_answer_xml = occasion_object_answer.to_xml() if occasion_object_answer else ""
        return self._call("SetOccasionObjectAnswer", occasionObjectAnswer=occasion_object_answer_xml, *args, **kwargs)

    def set_occasion_participant_number(self, *args: Any, participant_numbers: Optional[XmlArray[OccasionParticipantNumberSpec]] = None, **kwargs: Any) -> SoapResponse:
        """
        Set participant numbers for an occasion.

        This method calls the SOAP service's SetOccasionParticipantNumber operation to assign
        or update participant numbers for an occasion.

        Args:
            *args (Any): Variable length argument list to be passed to the underlying _call method.
            participant_numbers (Optional[XmlArray[OccasionParticipantNumberSpec]], optional):
                An array of participant number specifications to be set for the occasion.
                If None, an empty string will be sent. Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments to be passed to the underlying _call method.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        participant_numbers_xml = participant_numbers.to_xml() if participant_numbers else ""
        return self._call("SetOccasionParticipantNumber", participantNumbers=participant_numbers_xml, *args, **kwargs)

    def set_occasion_quantity(self, *args: Any, occasion_quantity: Optional[XmlArray[OccasionQuantitySpec]] = None, **kwargs: Any) -> SoapResponse:
        """
        Set the quantity for one or more occasions.

        This method calls the SetOccasionQuantity SOAP operation to update quantity information
        for specified occasions.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            occasion_quantity (Optional[XmlArray[OccasionQuantitySpec]], optional):
                An array of occasion quantity specifications to set. Each specification
                contains details about the occasion and the quantity to set. Defaults to None.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the
                quantity update operation.

        Note:
            If occasion_quantity is None, an empty string will be passed to the SOAP service.
        """
        occasion_quantity_xml = occasion_quantity.to_xml() if occasion_quantity else ""
        return self._call("SetOccasionQuantity", occasionQuantity=occasion_quantity_xml, *args, **kwargs)

    def set_occasion_seating(self, *args: Any, seating_info: Optional[XmlArray[OccasionSeatingInfoSpec]] = None, **kwargs: Any) -> SoapResponse:
        """
        Set seating information for an occasion.

        Args:
            *args: Variable length argument list to pass to the SOAP service.
            seating_info: Optional array of OccasionSeatingInfoSpec objects containing
                seating information to be set for the occasion. If None, an empty string
                is sent.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP service.

        Returns:
            SoapResponse: The response from the SetOccasionSeating SOAP service call.
        """
        seating_info_xml = seating_info.to_xml() if seating_info else ""
        return self._call("SetOccasionSeating", seatingInfo=seating_info_xml, *args, **kwargs)

    def update_occasion_dates(self, *args: Any, reservation_id: Optional[int] = None, occasion_id: Optional[int] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, **kwargs: Any) -> SoapResponse:
        """
        Update the start and end dates for an occasion.

        Args:
            reservation_id (Optional[int]): The ID of the reservation associated with the occasion.
            occasion_id (Optional[int]): The ID of the occasion to update.
            start_date (Optional[dt.date]): The new start date for the occasion.
            end_date (Optional[dt.date]): The new end date for the occasion.
            *args (Any): Additional positional arguments to pass to the SOAP call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service call.
        """
        return self._call("UpdateOccasionDates", reservationID=reservation_id, occasionID=occasion_id, startDate=start_date, endDate=end_date, *args, **kwargs)

    def update_occasion_status(self, *args: Any, reservation_id: Optional[int] = None, occasion_id: Optional[int] = None, status_id: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Update the status of an occasion in the Lega system.

        This method calls the UpdateOccasionStatus SOAP operation to modify the status
        of a specific occasion associated with a reservation.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int], optional): The unique identifier of the reservation.
                Defaults to None.
            occasion_id (Optional[int], optional): The unique identifier of the occasion to update.
                Defaults to None.
            status_id (Optional[str], optional): The new status identifier to set for the occasion.
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                of the status update operation.

        Raises:
            Any exceptions raised by the underlying _call method.
        """
        return self._call("UpdateOccasionStatus", reservationID=reservation_id, occasionID=occasion_id, statusID=status_id, *args, **kwargs)