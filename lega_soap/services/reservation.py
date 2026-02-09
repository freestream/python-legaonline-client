from __future__ import annotations

import datetime as dt
from typing import Any, Optional

from ..query import FilterSpec, SortSpec, IntListSpec
from ..types import SoapResponse
from .base import BaseService

class ReservationService(BaseService):
    """
    ReservationService provides a set of methods to interact with reservation-related operations via a SOAP API.

    This service class enables the creation, retrieval, updating, and deletion of reservations and their associated data, such as answers, addresses, shipping methods, and discounts. It supports multiple versions of reservation operations and allows for optional sorting and filtering of results.

    Methods:
        add_reservation_to_job(*args, reservation_id=None, job_id=None, **kwargs)
            Add a reservation to a specific job.

        cancel_reservation(reservation_ids=None)

        create_reservation(customer_id, customer_contact_id)

        create_reservation_inc_payment_method(customer_id, customer_contact_id, payment_method_id)

        get_reservation(*args, sorting=None, filtering=None, **kwargs)

        get_reservation_answer(*args, reservation_ids=None, **kwargs)
            Retrieve reservation answers for specified reservation IDs.

        get_reservation_answer_list(*args, sorting=None, filtering=None, **kwargs)
            Retrieve a list of reservation answers with optional sorting and filtering.

        get_reservation_answer_list_v2(*args, sorting=None, filtering=None, **kwargs)
            Retrieve a list of reservation answers using the V2 API method.

        get_reservation_answer_list_xml(*args, sorting=None, filtering=None, **kwargs)
            Retrieve a list of reservation answers in XML format.

        get_reservation_answer_list_xml_v2(*args, sorting=None, filtering=None, **kwargs)
            Retrieve a list of reservation answers in XML format (version 2).

        get_reservation_answer_v2(*args, reservation_ids=None, **kwargs)
            Retrieve reservation answers using the GetReservationAnswerV2 SOAP method.

        get_reservation_pickup_address(*args, sorting=None, filtering=None, **kwargs)
            Retrieve the pickup address for a reservation.

        get_reservation_pickup_address_xml(*args, sorting=None, filtering=None, **kwargs)
            Retrieve the reservation pickup address information in XML format.

        get_reservation_questions(*args, **kwargs)
            Retrieve reservation-related questions.

        get_reservation_shipping_address(*args, sorting=None, filtering=None, **kwargs)
            Retrieve the shipping address for a reservation.

        get_reservation_shipping_address_xml(*args, sorting=None, filtering=None, **kwargs)
            Retrieve the shipping address information for reservations in XML format.

        get_reservation_v2(*args, sorting=None, filtering=None, **kwargs)
            Retrieve reservation data using the GetReservationV2 SOAP method.

        get_reservation_v2_xml(*args, sorting=None, filtering=None, **kwargs)
            Retrieve reservation data in XML format using the GetReservationV2Xml SOAP method.

        get_reservation_v3(*args, sorting=None, filtering=None, **kwargs)
            Retrieve reservation data using version 3 of the reservation API.

        get_reservation_v3_xml(*args, sorting=None, filtering=None, **kwargs)
            Retrieve reservation data in XML format using the GetReservationV3Xml SOAP method.

        get_reservation_v4(*args, sorting=None, filtering=None, **kwargs)
            Retrieve reservation data using version 4 of the API.

        get_reservation_xml(*args, sorting=None, filtering=None, **kwargs)
            Retrieve reservation data in XML format.

        remove_reservation_pickup_address(*args, reservation_id=None, **kwargs)
            Remove the pickup address associated with a reservation.

        remove_reservation_shipping_address(*args, reservation_id=None, **kwargs)
            Remove the shipping address associated with a reservation.

        set_reservation(*args, reservation_id=None, tmp_order_id=None, customer_id=None, object_count=None, customer_contact_id=None, description=None, period_start=None, period_end=None, from_web=None, activated=None, returned=None, customer_reference=None, customer_notes=None, purchase_order_number=None, customer_shipping_address_lnk_id=None, shipping_customer_contact_id=None, payment_method_id=None, order_sum=None, paid=None, job_id=None, **kwargs)
            Create or update a reservation with the provided details.

        set_reservation_account_number(*args, reservation_id=None, account_number=None, **kwargs)
            Set the account number for a specific reservation.

        set_reservation_answer(*args, reservation_answer_id=None, question_id=None, answer_id=None, answer_text=None, reservation_id=None, **kwargs)
            Set an answer for a reservation question.

        set_reservation_answer_v2(*args, reservation_answer_id=None, question_id=None, answer_id=None, answer_text=None, reservation_id=None, **kwargs)
            Set or update an answer for a reservation question using the V2 API.

        set_reservation_pickup_address(*args, reservation_id=None, customer_shipping_address_lnk_id=None, **kwargs)
            Set the pickup address for a reservation.

        set_reservation_shipping_address(*args, reservation_id=None, customer_shipping_address_lnk_id=None, **kwargs)
            Set the shipping address for a reservation.

        set_reservation_shipping_method(*args, reservation_id=None, shipping_method_id=None, **kwargs)
            Set the shipping method for a specific reservation.

        set_reservation_v2(*args, reservation_id=None, tmp_order_id=None, customer_id=None, object_count=None, customer_contact_id=None, description=None, period_start=None, period_end=None, from_web=None, activated=None, returned=None, customer_reference=None, customer_notes=None, purchase_order_number=None, customer_shipping_address_lnk_id=None, shipping_customer_contact_id=None, payment_method_id=None, order_sum=None, paid=None, job_id=None, **kwargs)
            Create or update a reservation using the SetReservationV2 SOAP method.

        set_reservation_v3(*args, reservation_id=None, tmp_order_id=None, customer_id=None, object_count=None, customer_contact_id=None, description=None, period_start=None, period_end=None, from_web=None, activated=None, returned=None, customer_reference=None, customer_notes=None, purchase_order_number=None, customer_shipping_address_lnk_id=None, shipping_customer_contact_id=None, payment_method_id=None, order_sum=None, paid=None, job_id=None, **kwargs)
            Create or update a reservation using the SetReservationV3 SOAP method.

        set_reservation_v4(*args, reservation_id=None, tmp_order_id=None, customer_id=None, object_count=None, customer_contact_id=None, description=None, period_start=None, period_end=None, from_web=None, activated=None, returned=None, customer_reference=None, customer_notes=None, purchase_order_number=None, customer_shipping_address_lnk_id=None, shipping_customer_contact_id=None, payment_method_id=None, order_sum=None, paid=None, job_id=None, **kwargs)
            Create or update a reservation using the SetReservationV4 SOAP method.

        update_reservation_discount(*args, reservation_id=None, discount_percent=None, **kwargs)
            Update the discount percentage for a specific reservation.
    """
    __slots__ = ()

    def add_reservation_to_job(self, *args: Any, reservation_id: Optional[int] = None, job_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        return self._call("AddReservationToJob", *args, reservationID=reservation_id, jobID=job_id, **kwargs)

    def cancel_reservation(self, reservation_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Cancel one or more reservations.

        Args:
            reservation_ids (Optional[IntListSpec], optional): A list of reservation IDs to cancel.
                If None, the behavior depends on the SOAP service implementation. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the cancellation operation.
        """
        reservation_ids_xml = reservation_ids.to_xml() if reservation_ids else ""
        return self._call("CancelReservation", reservationIDs=reservation_ids_xml)

    def create_reservation(self, customer_id: Optional[int], customer_contact_id: Optional[int]) -> SoapResponse:
        """
        Create a new reservation for a customer.

        Args:
            customer_id (Optional[int]): The unique identifier of the customer. Can be None if not available.
            customer_contact_id (Optional[int]): The unique identifier of the customer contact. Can be None if not available.

        Returns:
            SoapResponse: The SOAP response object containing the result of the reservation creation operation.
        """
        return self._call("CreateReservation", customerID=customer_id, customerContactID=customer_contact_id)

    def create_reservation_inc_payment_method(self, customer_id: Optional[int], customer_contact_id: Optional[int], payment_method_id: Optional[int]) -> SoapResponse:
        """
        Create a reservation including payment method information.

        Args:
            customer_id: The unique identifier of the customer. Can be None.
            customer_contact_id: The unique identifier of the customer contact. Can be None.
            payment_method_id: The unique identifier of the payment method. Can be None.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation details.
        """
        return self._call("CreateReservationIncPaymentMethod", customerID=customer_id, customerContactID=customer_contact_id, paymentMethodID=payment_method_id)

    def get_reservation(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve reservation data with optional sorting and filtering.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification. If provided, it will be converted to XML and included in the request.
            filtering (Optional[FilterSpec]): An optional filtering specification. If provided, it will be converted to XML and included in the request.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP 'GetReservation' call.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservation", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_answer(self, *args: Any, reservation_ids: Optional[IntListSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves reservation answers for the specified reservation IDs.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            reservation_ids (Optional[IntListSpec]): An optional list of reservation IDs to query. If provided, it will be converted to XML format.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the reservation answers.

        """
        reservation_ids_xml = reservation_ids.to_xml() if reservation_ids else ""
        return self._call("GetReservationAnswer", reservationIDs=reservation_ids_xml, *args, **kwargs)

    def get_reservation_answer_list(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves a list of reservation answers from the SOAP service, with optional sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification to order the results.
            filtering (Optional[FilterSpec]): An optional filtering specification to filter the results.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation answer list.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationAnswerList", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_answer_list_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves a list of reservation answers using the V2 API method, with optional sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification. If provided, it will be converted to XML and included in the request.
            filtering (Optional[FilterSpec]): An optional filtering specification. If provided, it will be converted to XML and included in the request.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation answer list.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationAnswerListV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_answer_list_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves a list of reservation answers in XML format, with optional sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification. If provided, the results will be sorted accordingly.
            filtering (Optional[FilterSpec]): An optional filtering specification. If provided, the results will be filtered accordingly.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing the reservation answer list in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationAnswerListXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_answer_list_xml_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves a list of reservation answers in XML format (version 2), with optional sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification. If provided, the results will be sorted accordingly.
            filtering (Optional[FilterSpec]): An optional filtering specification. If provided, the results will be filtered accordingly.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing the reservation answer list in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationAnswerListXmlV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_answer_v2(self, *args: Any, reservation_ids: Optional[IntListSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves reservation answers for the specified reservation IDs using the GetReservationAnswerV2 SOAP method.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            reservation_ids (Optional[IntListSpec]): An optional list of reservation IDs to query. If provided, it will be serialized to XML.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing reservation answer details.
        """
        reservation_ids_xml = reservation_ids.to_xml() if reservation_ids else ""
        return self._call("GetReservationAnswerV2", reservationIDs=reservation_ids_xml, *args, **kwargs)

    def get_reservation_pickup_address(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves the pickup address for a reservation, with optional sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification to order the results.
            filtering (Optional[FilterSpec]): An optional filtering specification to filter the results.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation pickup address information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationPickupAddress", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_pickup_address_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves the reservation pickup address information in XML format.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification to order the results.
            filtering (Optional[FilterSpec]): An optional filtering specification to filter the results.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing the reservation pickup address XML.

        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationPickupAddressXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_questions(self, *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Retrieve reservation-related questions via the SOAP API.

        This method calls the "GetReservationQuestions" operation on the SOAP service,
        passing any provided positional and keyword arguments to the underlying call.

        Args:
            *args: Variable length argument list to be forwarded to the SOAP call.
            **kwargs: Arbitrary keyword arguments to be forwarded to the SOAP call.

        Returns:
            SoapResponse: The response object containing the reservation questions data.

        Raises:
            Any exceptions raised by the underlying SOAP call.
        """
        return self._call("GetReservationQuestions", *args, **kwargs)

    def get_reservation_shipping_address(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves the shipping address for a reservation.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification to order the results.
            filtering (Optional[FilterSpec]): An optional filtering specification to filter the results.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation shipping address information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationShippingAddress", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_shipping_address_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves the shipping address information for reservations in XML format.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification to order the results.
            filtering (Optional[FilterSpec]): An optional filtering specification to filter the results.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing the reservation shipping address XML.

        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationShippingAddressXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves reservation data using the GetReservationV2 SOAP method, with optional sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification. If provided, it will be converted to XML and included in the request.
            filtering (Optional[FilterSpec]): An optional filtering specification. If provided, it will be converted to XML and included in the request.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing reservation data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_v2_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves reservation data in XML format using the GetReservationV2Xml SOAP method.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification. If provided, it will be converted to XML and included in the request.
            filtering (Optional[FilterSpec]): An optional filtering specification. If provided, it will be converted to XML and included in the request.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing the reservation data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV2Xml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_v3(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves reservation data using version 3 of the reservation API.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification to determine the order of the returned reservations.
            filtering (Optional[FilterSpec]): An optional filtering specification to limit the reservations returned.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the reservation data.

        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV3", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_v3_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves reservation data in XML format using the GetReservationV3Xml SOAP method.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification. If provided, it will be converted to XML and included in the request.
            filtering (Optional[FilterSpec]): An optional filtering specification. If provided, it will be converted to XML and included in the request.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV3Xml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_v4(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve reservation data using version 4 of the API, with optional sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification. If provided, it will be converted to XML and included in the request.
            filtering (Optional[FilterSpec]): An optional filtering specification. If provided, it will be converted to XML and included in the request.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the reservation data.

        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV4", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_reservation_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves reservation data in XML format, optionally applying sorting and filtering.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec]): An optional sorting specification to order the reservations.
            filtering (Optional[FilterSpec]): An optional filtering specification to filter the reservations.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing the reservation data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def remove_reservation_pickup_address(self, *args: Any, reservation_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Removes the pickup address associated with a reservation.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int]): The unique identifier of the reservation whose pickup address should be removed.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object returned by the SOAP service after attempting to remove the pickup address.
        """
        return self._call("RemoveReservationPickupAddress", *args, reservationID=reservation_id, **kwargs)

    def remove_reservation_shipping_address(self, *args: Any, reservation_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Removes the shipping address associated with a reservation.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int]): The unique identifier of the reservation whose shipping address should be removed.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service after attempting to remove the shipping address.
        """
        return self._call("RemoveReservationShippingAddress", *args, reservationID=reservation_id, **kwargs)

    def set_reservation(self, *args: Any, reservation_id: Optional[int] = None, tmp_order_id: Optional[int] = None, customer_id: Optional[int] = None, object_count: Optional[int] = None, customer_contact_id: Optional[int] = None, description: Optional[str] = None, period_start: Optional[dt.date] = None, period_end: Optional[dt.date] = None, from_web: Optional[bool] = None, activated: Optional[bool] = None, returned: Optional[bool] = None, customer_reference: Optional[str] = None, customer_notes: Optional[str] = None, purchase_order_number: Optional[str] = None, customer_shipping_address_lnk_id: Optional[int] = None, shipping_customer_contact_id: Optional[int] = None, payment_method_id: Optional[int] = None, order_sum: Optional[float] = None, paid: Optional[bool] = None, job_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Creates or updates a reservation with the provided details.

        Parameters:
            *args: Any
                Additional positional arguments passed to the underlying SOAP call.
            reservation_id: Optional[int]
                The unique identifier of the reservation to update. If None, a new reservation may be created.
            tmp_order_id: Optional[int]
                Temporary order identifier associated with the reservation.
            customer_id: Optional[int]
                The ID of the customer making the reservation.
            object_count: Optional[int]
                The number of objects/items reserved.
            customer_contact_id: Optional[int]
                The contact ID for the customer.
            description: Optional[str]
                Description or notes about the reservation.
            period_start: Optional[dt.date]
                Start date of the reservation period.
            period_end: Optional[dt.date]
                End date of the reservation period.
            from_web: Optional[bool]
                Indicates if the reservation was made from the web.
            activated: Optional[bool]
                Indicates if the reservation is activated.
            returned: Optional[bool]
                Indicates if the reserved items have been returned.
            customer_reference: Optional[str]
                Reference information provided by the customer.
            customer_notes: Optional[str]
                Additional notes from the customer.
            purchase_order_number: Optional[str]
                Purchase order number associated with the reservation.
            customer_shipping_address_lnk_id: Optional[int]
                Link ID for the customer's shipping address.
            shipping_customer_contact_id: Optional[int]
                Contact ID for the shipping customer.
            payment_method_id: Optional[int]
                ID of the payment method used.
            order_sum: Optional[float]
                Total sum of the order.
            paid: Optional[bool]
                Indicates if the reservation/order has been paid.
            job_id: Optional[int]
                Associated job ID, if applicable.
            **kwargs: Any
                Additional keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse
                The response from the SOAP service after attempting to set the reservation.
        """
        return self._call("SetReservation", *args, reservationID=reservation_id, TmpOrderID=tmp_order_id, CustomerID=customer_id, ObjectCount=object_count, CustomerContactID=customer_contact_id, Description=description, PeriodStart=period_start, PeriodEnd=period_end, FromWeb=from_web, Activated=activated, Returned=returned, CustomerReference=customer_reference, CustomerNotes=customer_notes, PurchaseOrderNumber=purchase_order_number, CustomerShippingAddressLnkID=customer_shipping_address_lnk_id, ShippingCustomerContactID=shipping_customer_contact_id, PaymentMethodID=payment_method_id, OrderSum=order_sum, Paid=paid, JobID=job_id, **kwargs)

    def set_reservation_account_number(self, *args: Any, reservation_id: Optional[int] = None, account_number: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Sets the account number for a specific reservation.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int]): The unique identifier of the reservation to update.
            account_number (Optional[str]): The account number to associate with the reservation.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object returned by the SOAP service after attempting to set the account number.
        """
        return self._call("SetReservationAccountNumber", *args, reservationID=reservation_id, accountNumber=account_number, **kwargs)

    def set_reservation_answer(self, *args: Any, reservation_answer_id: Optional[int] = None, question_id: Optional[int] = None, answer_id: Optional[int] = None, answer_text: Optional[str] = None, reservation_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Sets an answer for a reservation question.

        Args:
            *args (Any): Additional positional arguments.
            reservation_answer_id (Optional[int], optional): The ID of the reservation answer. Defaults to None.
            question_id (Optional[int], optional): The ID of the question being answered. Defaults to None.
            answer_id (Optional[int], optional): The ID of the selected answer. Defaults to None.
            answer_text (Optional[str], optional): The text of the answer, if applicable. Defaults to None.
            reservation_id (Optional[int], optional): The ID of the reservation. Defaults to None.
            **kwargs (Any): Additional keyword arguments.

        Returns:
            SoapResponse: The response from the SOAP service after setting the reservation answer.
        """
        return self._call("SetReservationAnswer", *args, ReservationAnswerID=reservation_answer_id, QuestionID=question_id, AnswerID=answer_id, AnswerText=answer_text, ReservationID=reservation_id, **kwargs)

    def set_reservation_answer_v2(self, *args: Any, reservation_answer_id: Optional[int] = None, question_id: Optional[int] = None, answer_id: Optional[int] = None, answer_text: Optional[str] = None, reservation_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Sets or updates an answer for a reservation question using the V2 API.

        This method sends the provided answer details to the SOAP service, associating them with a specific reservation and question.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            reservation_answer_id (Optional[int]): The unique identifier of the reservation answer to update. If None, a new answer may be created.
            question_id (Optional[int]): The unique identifier of the question being answered.
            answer_id (Optional[int]): The unique identifier of the selected answer option, if applicable.
            answer_text (Optional[str]): The text of the answer, if a free-text response is required.
            reservation_id (Optional[int]): The unique identifier of the reservation to which the answer belongs.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object returned by the SOAP service after setting the reservation answer.
        """
        return self._call("SetReservationAnswerV2", *args, ReservationAnswerID=reservation_answer_id, QuestionID=question_id, AnswerID=answer_id, AnswerText=answer_text, ReservationID=reservation_id, **kwargs)

    def set_reservation_pickup_address(self, *args: Any, reservation_id: Optional[int] = None, customer_shipping_address_lnk_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Sets the pickup address for a reservation.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int]): The unique identifier of the reservation.
            customer_shipping_address_lnk_id (Optional[int]): The link ID of the customer's shipping address to be set as the pickup address.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service after attempting to set the pickup address.
        """
        return self._call("SetReservationPickupAddress", *args, reservationID=reservation_id, CustomerShippingAddressLnkID=customer_shipping_address_lnk_id, **kwargs)

    def set_reservation_shipping_address(self, *args: Any, reservation_id: Optional[int] = None, customer_shipping_address_lnk_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Sets the shipping address for a reservation.

        This method calls the "SetReservationShippingAddress" SOAP operation to update the shipping address associated with a specific reservation.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int]): The unique identifier of the reservation to update.
            customer_shipping_address_lnk_id (Optional[int]): The unique identifier linking the customer to the shipping address.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object returned by the SOAP service after attempting to set the reservation's shipping address.
        """
        return self._call("SetReservationShippingAddress", *args, reservationID=reservation_id, CustomerShippingAddressLnkID=customer_shipping_address_lnk_id, **kwargs)

    def set_reservation_shipping_method(self, *args: Any, reservation_id: Optional[int] = None, shipping_method_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Sets the shipping method for a specific reservation.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int]): The ID of the reservation to update.
            shipping_method_id (Optional[int]): The ID of the shipping method to set for the reservation.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service after setting the shipping method.
        """
        return self._call("SetReservationShippingMethod", *args, reservationID=reservation_id, ShippingMethodID=shipping_method_id, **kwargs)

    def set_reservation_v2(self, *args: Any, reservation_id: Optional[int] = None, tmp_order_id: Optional[int] = None, customer_id: Optional[int] = None, object_count: Optional[int] = None, customer_contact_id: Optional[int] = None, description: Optional[str] = None, period_start: Optional[dt.date] = None, period_end: Optional[dt.date] = None, from_web: Optional[bool] = None, activated: Optional[bool] = None, returned: Optional[bool] = None, customer_reference: Optional[str] = None, customer_notes: Optional[str] = None, purchase_order_number: Optional[str] = None, customer_shipping_address_lnk_id: Optional[int] = None, shipping_customer_contact_id: Optional[int] = None, payment_method_id: Optional[int] = None, order_sum: Optional[float] = None, paid: Optional[bool] = None, job_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Creates or updates a reservation using the SetReservationV2 SOAP method.

        Parameters:
            *args: Any
                Additional positional arguments passed to the SOAP call.
            reservation_id: Optional[int]
                The unique identifier of the reservation to update. If None, a new reservation may be created.
            tmp_order_id: Optional[int]
                Temporary order identifier associated with the reservation.
            customer_id: Optional[int]
                The unique identifier of the customer making the reservation.
            object_count: Optional[int]
                The number of objects/items included in the reservation.
            customer_contact_id: Optional[int]
                The contact ID for the customer.
            description: Optional[str]
                Description or notes about the reservation.
            period_start: Optional[dt.date]
                The start date of the reservation period.
            period_end: Optional[dt.date]
                The end date of the reservation period.
            from_web: Optional[bool]
                Indicates if the reservation was made from the web.
            activated: Optional[bool]
                Indicates if the reservation is activated.
            returned: Optional[bool]
                Indicates if the reserved items have been returned.
            customer_reference: Optional[str]
                Reference string provided by the customer.
            customer_notes: Optional[str]
                Additional notes from the customer.
            purchase_order_number: Optional[str]
                Purchase order number associated with the reservation.
            customer_shipping_address_lnk_id: Optional[int]
                Link ID for the customer's shipping address.
            shipping_customer_contact_id: Optional[int]
                Contact ID for the shipping customer.
            payment_method_id: Optional[int]
                Identifier for the payment method used.
            order_sum: Optional[float]
                Total sum of the order.
            paid: Optional[bool]
                Indicates if the reservation/order has been paid.
            job_id: Optional[int]
                Identifier for the related job.
            **kwargs: Any
                Additional keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse
                The response object from the SOAP call containing the result of the reservation operation.
        """
        return self._call("SetReservationV2", *args, reservationID=reservation_id, TmpOrderID=tmp_order_id, CustomerID=customer_id, ObjectCount=object_count, CustomerContactID=customer_contact_id, Description=description, PeriodStart=period_start, PeriodEnd=period_end, FromWeb=from_web, Activated=activated, Returned=returned, CustomerReference=customer_reference, CustomerNotes=customer_notes, PurchaseOrderNumber=purchase_order_number, CustomerShippingAddressLnkID=customer_shipping_address_lnk_id, ShippingCustomerContactID=shipping_customer_contact_id, PaymentMethodID=payment_method_id, OrderSum=order_sum, Paid=paid, JobID=job_id, **kwargs)

    def set_reservation_v3(self, *args: Any, reservation_id: Optional[int] = None, tmp_order_id: Optional[int] = None, customer_id: Optional[int] = None, object_count: Optional[int] = None, customer_contact_id: Optional[int] = None, description: Optional[str] = None, period_start: Optional[dt.date] = None, period_end: Optional[dt.date] = None, from_web: Optional[bool] = None, activated: Optional[bool] = None, returned: Optional[bool] = None, customer_reference: Optional[str] = None, customer_notes: Optional[str] = None, purchase_order_number: Optional[str] = None, customer_shipping_address_lnk_id: Optional[int] = None, shipping_customer_contact_id: Optional[int] = None, payment_method_id: Optional[int] = None, order_sum: Optional[float] = None, paid: Optional[bool] = None, job_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Creates or updates a reservation using the SetReservationV3 SOAP method.

        Parameters:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int]): The unique identifier for the reservation.
            tmp_order_id (Optional[int]): Temporary order ID associated with the reservation.
            customer_id (Optional[int]): The ID of the customer making the reservation.
            object_count (Optional[int]): Number of objects/items in the reservation.
            customer_contact_id (Optional[int]): ID of the customer's contact person.
            description (Optional[str]): Description of the reservation.
            period_start (Optional[dt.date]): Start date of the reservation period.
            period_end (Optional[dt.date]): End date of the reservation period.
            from_web (Optional[bool]): Indicates if the reservation was made from the web.
            activated (Optional[bool]): Whether the reservation is activated.
            returned (Optional[bool]): Whether the reserved items have been returned.
            customer_reference (Optional[str]): Reference provided by the customer.
            customer_notes (Optional[str]): Notes from the customer.
            purchase_order_number (Optional[str]): Purchase order number associated with the reservation.
            customer_shipping_address_lnk_id (Optional[int]): Link ID for the customer's shipping address.
            shipping_customer_contact_id (Optional[int]): Contact ID for shipping.
            payment_method_id (Optional[int]): ID of the payment method used.
            order_sum (Optional[float]): Total sum of the order.
            paid (Optional[bool]): Indicates if the reservation/order has been paid.
            job_id (Optional[int]): Associated job ID.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service after setting the reservation.
        """
        return self._call("SetReservationV3", *args, reservationID=reservation_id, TmpOrderID=tmp_order_id, CustomerID=customer_id, ObjectCount=object_count, CustomerContactID=customer_contact_id, Description=description, PeriodStart=period_start, PeriodEnd=period_end, FromWeb=from_web, Activated=activated, Returned=returned, CustomerReference=customer_reference, CustomerNotes=customer_notes, PurchaseOrderNumber=purchase_order_number, CustomerShippingAddressLnkID=customer_shipping_address_lnk_id, ShippingCustomerContactID=shipping_customer_contact_id, PaymentMethodID=payment_method_id, OrderSum=order_sum, Paid=paid, JobID=job_id, **kwargs)

    def set_reservation_v4(self, *args: Any, reservation_id: Optional[int] = None, tmp_order_id: Optional[int] = None, customer_id: Optional[int] = None, object_count: Optional[int] = None, customer_contact_id: Optional[int] = None, description: Optional[str] = None, period_start: Optional[dt.date] = None, period_end: Optional[dt.date] = None, from_web: Optional[bool] = None, activated: Optional[bool] = None, returned: Optional[bool] = None, customer_reference: Optional[str] = None, customer_notes: Optional[str] = None, purchase_order_number: Optional[str] = None, customer_shipping_address_lnk_id: Optional[int] = None, shipping_customer_contact_id: Optional[int] = None, payment_method_id: Optional[int] = None, order_sum: Optional[float] = None, paid: Optional[bool] = None, job_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Creates or updates a reservation using the SetReservationV4 SOAP method.

        Parameters:
            *args (Any): Additional positional arguments passed to the SOAP call.
            reservation_id (Optional[int]): The unique identifier for the reservation.
            tmp_order_id (Optional[int]): Temporary order ID associated with the reservation.
            customer_id (Optional[int]): The ID of the customer making the reservation.
            object_count (Optional[int]): Number of objects/items in the reservation.
            customer_contact_id (Optional[int]): Contact ID for the customer.
            description (Optional[str]): Description of the reservation.
            period_start (Optional[datetime.date]): Start date of the reservation period.
            period_end (Optional[datetime.date]): End date of the reservation period.
            from_web (Optional[bool]): Indicates if the reservation was made from the web.
            activated (Optional[bool]): Indicates if the reservation is activated.
            returned (Optional[bool]): Indicates if the reserved items have been returned.
            customer_reference (Optional[str]): Reference provided by the customer.
            customer_notes (Optional[str]): Additional notes from the customer.
            purchase_order_number (Optional[str]): Purchase order number associated with the reservation.
            customer_shipping_address_lnk_id (Optional[int]): Link ID for the customer's shipping address.
            shipping_customer_contact_id (Optional[int]): Contact ID for the shipping customer.
            payment_method_id (Optional[int]): ID of the payment method used.
            order_sum (Optional[float]): Total sum of the order.
            paid (Optional[bool]): Indicates if the reservation has been paid.
            job_id (Optional[int]): Associated job ID.
            **kwargs (Any): Additional keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP call.
        """
        return self._call("SetReservationV4", *args, reservationID=reservation_id, TmpOrderID=tmp_order_id, CustomerID=customer_id, ObjectCount=object_count, CustomerContactID=customer_contact_id, Description=description, PeriodStart=period_start, PeriodEnd=period_end, FromWeb=from_web, Activated=activated, Returned=returned, CustomerReference=customer_reference, CustomerNotes=customer_notes, PurchaseOrderNumber=purchase_order_number, CustomerShippingAddressLnkID=customer_shipping_address_lnk_id, ShippingCustomerContactID=shipping_customer_contact_id, PaymentMethodID=payment_method_id, OrderSum=order_sum, Paid=paid, JobID=job_id, **kwargs)

    def update_reservation_discount(self, *args: Any, reservation_id: Optional[int] = None, discount_percent: Optional[float] = None, **kwargs: Any) -> SoapResponse:
        """
        Updates the discount percentage for a specific reservation.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            reservation_id (Optional[int]): The unique identifier of the reservation to update.
            discount_percent (Optional[float]): The new discount percentage to apply to the reservation.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service after updating the reservation discount.
        """
        return self._call("UpdateReservationDiscount", *args, reservationID=reservation_id, discountPercent=discount_percent, **kwargs)