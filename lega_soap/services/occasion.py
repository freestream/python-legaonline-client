from __future__ import annotations

import datetime as dt
from typing import Any, Optional

from ..query import (
    IntListSpec,
    SortSpec,
    FilterSpec,
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

    def activate_occasion(self, occasion_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Activate one or more occasions.

        Args:
            occasion_ids (Optional[IntListSpec], optional): Specification of occasion IDs to activate.
                If None, no ID list is included in the SOAP request. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the result
                of the activation operation.
        """
        return self._call("ActivateOccasion", occasionIDs=occasion_ids.to_zeep() if occasion_ids else None)

    def add_occasion_accessory(
        self,
        occasion_id: Optional[int] = None,
        start_date: Optional[dt.datetime] = None,
        end_date: Optional[dt.datetime] = None,
        status_id: Optional[int] = None,
        object_id: Optional[int] = None,
        quantity: Optional[int] = None,
    ) -> SoapResponse:
        """
        Add an accessory to an occasion.

        Args:
            occasion_id (Optional[int]): Occasion ID. Required in WSDL.
            start_date (Optional[dt.datetime]): Start date. Required in WSDL.
            end_date (Optional[dt.datetime]): End date. Required in WSDL.
            status_id (Optional[int]): Status ID. Required in WSDL.
                See :class:`lega_soap.OccasionStatus` for values
                (1=Booked, 2=Preliminary, 3=Canceled, 4=Locked).
            object_id (Optional[int]): Object ID. Required in WSDL.
            quantity (Optional[int]): Quantity. Required in WSDL.

        Returns:
            SoapResponse: The response from the SOAP service call.
        """
        record = {k: v for k, v in {
            "OccasionID": occasion_id,
            "StartDate": start_date,
            "EndDate": end_date,
            "StatusID": status_id,
            "ObjectID": object_id,
            "Quantity": quantity,
        }.items() if v is not None}
        return self._call("AddOccasionAccessory", occasionAccessory={"OccasionAccessory": [record]})

    def cancel_occasion(self, occasion_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Cancel one or more occasions.

        Args:
            occasion_ids (Optional[IntListSpec], optional): A specification containing a list of
                occasion IDs to cancel. If None, no occasions will be cancelled. Defaults to None.

        Returns:
            SoapResponse: The SOAP response from the CancelOccasion operation.
        """
        return self._call("CancelOccasion", occasionIDs=occasion_ids.to_zeep() if occasion_ids else None)

    def create_occasion(self, reservation_id: int, object_id: int, customer_id: int, customer_contact_id: int, start_date: dt.date, end_date: dt.date, quantity: int) -> SoapResponse:
        """
        Creates a new occasion.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation to associate with the occasion. Defaults to None.
            object_id (Optional[int], optional): The ID of the object for the occasion. Defaults to None.
            customer_id (Optional[int], optional): The ID of the customer associated with the occasion. Defaults to None.
            customer_contact_id (Optional[int], optional): The ID of the customer contact associated with the occasion. Defaults to None.
            start_date (Optional[dt.date], optional): The start date of the occasion. Defaults to None.
            end_date (Optional[dt.date], optional): The end date of the occasion. Defaults to None.
            quantity (Optional[int], optional): The quantity for the occasion. Defaults to None.

        Returns:
            SoapResponse: The SOAP response object containing the result of the CreateOccasion operation.
        """
        return self._call("CreateOccasion", reservationID=reservation_id, objectID=object_id, customerID=customer_id, customerContactID=customer_contact_id, startDate=start_date, endDate=end_date, quantity=quantity)

    def create_preliminary_occasion(self, reservation_id: int, object_id: int, customer_id: int, customer_contact_id: int, start_date: dt.date, end_date: dt.date, quantity: int) -> SoapResponse:
        """
        Create a preliminary occasion.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation. Defaults to None.
            object_id (Optional[int], optional): The ID of the object for the occasion. Defaults to None.
            customer_id (Optional[int], optional): The ID of the customer. Defaults to None.
            customer_contact_id (Optional[int], optional): The ID of the customer contact. Defaults to None.
            start_date (Optional[dt.date], optional): The start date of the occasion. Defaults to None.
            end_date (Optional[dt.date], optional): The end date of the occasion. Defaults to None.
            quantity (Optional[int], optional): The quantity for the occasion. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service call.
        """
        return self._call("CreatePreliminaryOccasion", reservationID=reservation_id, objectID=object_id, customerID=customer_id, customerContactID=customer_contact_id, startDate=start_date, endDate=end_date, quantity=quantity)

    def get_availability_exclude_occasion(self, object_ids: Optional[IntListSpec] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, exclude_occasion_id: Optional[int] = None) -> SoapResponse:
        """
        Get availability for objects excluding a specific occasion.

        Args:
            object_ids (Optional[IntListSpec], optional): List specification of object IDs to check
                availability for. Defaults to None.
            start_date (Optional[dt.date], optional): Start date for the availability query. Defaults to None.
            end_date (Optional[dt.date], optional): End date for the availability query. Defaults to None.
            exclude_occasion_id (Optional[int], optional): The occasion ID to exclude from the results.
                Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing availability information for the requested
                objects, excluding the specified occasion.
        """
        return self._call("GetAvailabilityExcludeOccasion", objectIDs=object_ids.to_zeep() if object_ids else None, startDate=start_date, endDate=end_date, excludeOccasionID=exclude_occasion_id)

    def get_availability_exclude_occasion_xml(self, object_ids: Optional[IntListSpec] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None, exclude_occasion_id: Optional[int] = None) -> SoapResponse:
        """
        Get availability for objects excluding a specific occasion, returned as XML.

        Args:
            object_ids (Optional[IntListSpec], optional): List specification of object IDs to check availability for. Defaults to None.
            start_date (Optional[dt.date], optional): Start date for the availability period. Defaults to None.
            end_date (Optional[dt.date], optional): End date for the availability period. Defaults to None.
            exclude_occasion_id (Optional[int], optional): ID of the occasion to exclude from availability check. Defaults to None.

        Returns:
            SoapResponse: SOAP response containing availability information in XML format.
        """
        return self._call("GetAvailabilityExcludeOccasionXml", objectIDs=object_ids.to_zeep() if object_ids else None, startDate=start_date, endDate=end_date, excludeOccasionID=exclude_occasion_id)

    def get_occasion(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion data from the SOAP service with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasion", sort=sort_xml, filter=filter_xml)

    def get_occasion_answer(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion answers from the SOAP service with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification to apply to the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to apply to the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the occasion answer data from the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionAnswer", sort=sort_xml, filter=filter_xml)

    def get_occasion_answer_v2(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves occasion answers using the GetOccasionAnswerV2 SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion
                answer data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionAnswerV2", sort=sort_xml, filter=filter_xml)

    def get_occasion_answer_v2_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion answers in XML format using version 2 of the API.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification to order the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to filter the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the
                occasion answers in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionAnswerV2Xml", sort=sort_xml, filter=filter_xml)

    def get_occasion_answer_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves occasion answer data in XML format via SOAP service call.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification that defines how results should be ordered.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification that defines which results to include.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion
                          answer data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionAnswerXml", sort=sort_xml, filter=filter_xml)

    def get_occasion_location(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion location information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                occasion location data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionLocation", sort=sort_xml, filter=filter_xml)

    def get_occasion_location_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves occasion location data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion
                location data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionLocationXml", sort=sort_xml, filter=filter_xml)

    def get_occasion_participant_number(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion participant numbers from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification to order the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to filter the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion
                participant number data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionParticipantNumber", sort=sort_xml, filter=filter_xml)

    def get_occasion_participant_number_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion participant numbers in XML format.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification to apply to the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification to apply to the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion
                          participant numbers in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionParticipantNumberXml", sort=sort_xml, filter=filter_xml)

    def get_occasion_questions(self, object_id: Optional[int] = None) -> SoapResponse:
        """
        Retrieve occasion questions for a given object.

        Args:
            object_id (Optional[int], optional): The ID of the object to retrieve questions for. Defaults to None.

        Returns:
            SoapResponse: The response object containing the occasion questions data.
        """
        return self._call("GetOccasionQuestions", objectID=object_id)

    def get_occasion_questions_v2(self, object_id: Optional[int] = None) -> SoapResponse:
        """
        Retrieves occasion questions using version 2 of the API.

        Args:
            object_id (Optional[int], optional): The ID of the object to retrieve questions for. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing the occasion questions data.
        """
        return self._call("GetOccasionQuestionsV2", objectID=object_id)

    def get_occasion_questions_xml(self, object_id: Optional[int] = None) -> SoapResponse:
        """
        Retrieve occasion questions in XML format.

        Args:
            object_id (Optional[int], optional): The ID of the object to retrieve questions for. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion questions data.
        """
        return self._call("GetOccasionQuestionsXml", objectID=object_id)

    def get_occasion_seating(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve seating information for an occasion.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion seating data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionSeating", sort=sort_xml, filter=filter_xml)

    def get_occasion_seating_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve seating information for an occasion in XML format.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the seating data.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the seating data.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing occasion seating
                information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionSeatingXml", sort=sort_xml, filter=filter_xml)

    def get_occasion_v2(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion data using the GetOccasionV2 SOAP operation.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification object. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV2", sort=sort_xml, filter=filter_xml)

    def get_occasion_v2_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion data in XML format using the V2 API endpoint.

        Args:
            sorting (Optional[SortSpec], optional): Sorting criteria for the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering criteria for the results. Defaults to None.

        Returns:
            SoapResponse: The SOAP response object containing the occasion data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV2Xml", sort=sort_xml, filter=filter_xml)

    def get_occasion_v3(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion data using the GetOccasionV3 SOAP operation.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing occasion data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV3", sort=sort_xml, filter=filter_xml)

    def get_occasion_v3_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion data in XML format using the GetOccasionV3Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification object. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the occasion data
                in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV3Xml", sort=sort_xml, filter=filter_xml)

    def get_occasion_v4(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion data using version 4 of the GetOccasion SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the result from the GetOccasionV4 SOAP call.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV4", sort=sort_xml, filter=filter_xml)

    def get_occasion_v4_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion data in XML format using the V4 API endpoint.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the XML data for occasions
                matching the specified criteria.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionV4Xml", sort=sort_xml, filter=filter_xml)

    def get_occasion_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve occasion data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing occasion data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOccasionXml", sort=sort_xml, filter=filter_xml)

    def return_occasion(self, occasion_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Return occasion information from the LEGA system.

        Args:
            occasion_ids (Optional[IntListSpec], optional): Specification of occasion IDs to return.
                If provided, will be converted to XML format for the SOAP request. Defaults to None.

        Returns:
            SoapResponse: The response from the ReturnOccasion SOAP service containing
                the requested occasion information.
        """
        return self._call("ReturnOccasion", occasionIDs=occasion_ids.to_zeep() if occasion_ids else None)

    def set_occasion_answer(
        self,
        answer_id: Optional[int] = None,
        occasion_id: Optional[int] = None,
        answer_text: Optional[str] = None,
        answer_time: Optional[str] = None,
        answer_number: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set answers for one or more occasions.

        Args:
            answer_id (Optional[int]): Answer ID. Required in WSDL.
            occasion_id (Optional[int]): Occasion ID. Required in WSDL.
            answer_text (Optional[str]): Answer text.
            answer_time (Optional[str]): Answer time.
            answer_number (Optional[int]): Answer number. Required in WSDL.

        Returns:
            SoapResponse: The response from the SOAP service after setting the occasion answers.
        """
        record = {k: v for k, v in {
            "AnswerID": answer_id,
            "OccasionID": occasion_id,
            "AnswerText": answer_text,
            "AnswerTime": answer_time,
            "AnswerNumber": answer_number,
        }.items() if v is not None}
        return self._call("SetOccasionAnswer", occasionAnswer={"OccAnswer": [record]})

    def set_occasion_location(
        self,
        occasion_id: Optional[int] = None,
        location_id: Optional[int] = None,
        location_address_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set the location for an occasion.

        Args:
            occasion_id (Optional[int]): Occasion ID. Required in WSDL.
            location_id (Optional[int]): Location ID. Required in WSDL.
            location_address_id (Optional[int]): Location address ID. Required in WSDL.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the
                operation.
        """
        record = {k: v for k, v in {
            "OccasionID": occasion_id,
            "LocationID": location_id,
            "LocationAddressID": location_address_id,
        }.items() if v is not None}
        return self._call("SetOccasionLocation", occasionLocation={"OccasionLocation": [record]})

    def set_occasion_object_answer(
        self,
        answer_id: Optional[int] = None,
        occasion_id: Optional[int] = None,
        object_id: Optional[int] = None,
        answer_text: Optional[str] = None,
        answer_time: Optional[str] = None,
        answer_number: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set occasion object answer via SOAP service.

        Args:
            answer_id (Optional[int]): Answer ID. Required in WSDL.
            occasion_id (Optional[int]): Occasion ID. Required in WSDL.
            object_id (Optional[int]): Object ID. Required in WSDL.
            answer_text (Optional[str]): Answer text.
            answer_time (Optional[str]): Answer time.
            answer_number (Optional[int]): Answer number. Required in WSDL.

        Returns:
            SoapResponse: The response object from the SOAP service call.
        """
        record = {k: v for k, v in {
            "AnswerID": answer_id,
            "OccasionID": occasion_id,
            "ObjectID": object_id,
            "AnswerText": answer_text,
            "AnswerTime": answer_time,
            "AnswerNumber": answer_number,
        }.items() if v is not None}
        return self._call("SetOccasionObjectAnswer", occasionObjectAnswer={"OccObjectAnswer": [record]})

    def set_occasion_participant_number(
        self,
        participant_number: Optional[int] = None,
        occasion_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set participant numbers for an occasion.

        Args:
            participant_number (Optional[int]): Participant number. Required in WSDL.
            occasion_id (Optional[int]): Occasion ID. Required in WSDL.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        record = {k: v for k, v in {
            "ParticipantNumber": participant_number,
            "OccasionID": occasion_id,
        }.items() if v is not None}
        return self._call("SetOccasionParticipantNumber", participantNumbers={"OccasionParticipantNumber": [record]})

    def set_occasion_quantity(
        self,
        occasion_id: Optional[int] = None,
        quantity: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set the quantity for one or more occasions.

        Args:
            occasion_id (Optional[int]): Occasion ID. Required in WSDL.
            quantity (Optional[int]): Quantity. Required in WSDL.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the
                quantity update operation.
        """
        record = {k: v for k, v in {
            "OccasionID": occasion_id,
            "Quantity": quantity,
        }.items() if v is not None}
        return self._call("SetOccasionQuantity", occasionQuantity={"OccasionQuantity": [record]})

    def set_occasion_seating(
        self,
        occasion_id: Optional[int] = None,
        seating_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set seating information for an occasion.

        Args:
            occasion_id (Optional[int]): Occasion ID. Required in WSDL.
            seating_id (Optional[int]): Seating ID. Required in WSDL.

        Returns:
            SoapResponse: The response from the SetOccasionSeating SOAP service call.
        """
        record = {k: v for k, v in {
            "OccasionID": occasion_id,
            "SeatingID": seating_id,
        }.items() if v is not None}
        return self._call("SetOccasionSeating", seatingInfo={"OccasionSeatingInfo": [record]})

    def update_occasion_dates(self, reservation_id: Optional[int] = None, occasion_id: Optional[int] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None) -> SoapResponse:
        """
        Update the start and end dates for an occasion.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation associated with the occasion. Defaults to None.
            occasion_id (Optional[int], optional): The ID of the occasion to update. Defaults to None.
            start_date (Optional[dt.date], optional): The new start date for the occasion. Defaults to None.
            end_date (Optional[dt.date], optional): The new end date for the occasion. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service call.
        """
        return self._call("UpdateOccasionDates", reservationID=reservation_id, occasionID=occasion_id, startDate=start_date, endDate=end_date)

    def update_occasion_status(self, reservation_id: Optional[int] = None, occasion_id: Optional[int] = None, status_id: Optional[int] = None) -> SoapResponse:
        """
        Update the status of an occasion in the Lega system.

        Args:
            reservation_id (Optional[int], optional): The unique identifier of the reservation. Defaults to None.
            occasion_id (Optional[int], optional): The unique identifier of the occasion to update. Defaults to None.
            status_id (Optional[int], optional): The new status identifier to set for the occasion.
                See :class:`lega_soap.OccasionStatus` for values
                (1=Booked, 2=Preliminary, 3=Canceled, 4=Locked). Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                of the status update operation.
        """
        return self._call("UpdateOccasionStatus", reservationID=reservation_id, occasionID=occasion_id, statusID=status_id)
