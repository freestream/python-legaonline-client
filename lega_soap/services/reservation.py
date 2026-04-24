from __future__ import annotations

import datetime as dt
from decimal import Decimal
from typing import Optional

from ..query import FilterSpec, SortSpec, IntListSpec
from ..types import SoapResponse
from .base import BaseService

class ReservationService(BaseService):
    """
    ReservationService provides a set of methods to interact with reservation-related operations via a SOAP API.

    This service class enables the creation, retrieval, updating, and deletion of reservations and their associated data,
    such as answers, addresses, shipping methods, and discounts. It supports multiple versions of reservation operations
    and allows for optional sorting and filtering of results.
    """
    __slots__ = ()

    def add_reservation_to_job(self, reservation_id: Optional[int] = None, job_id: Optional[int] = None) -> SoapResponse:
        """
        Add a reservation to a specific job.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation. Defaults to None.
            job_id (Optional[int], optional): The ID of the job. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service.
        """
        return self._call("AddReservationToJob", reservationID=reservation_id, jobID=job_id)

    def cancel_reservation(self, reservation_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Cancel one or more reservations.

        Args:
            reservation_ids (Optional[IntListSpec], optional): A list of reservation IDs to cancel.
                If None, the behavior depends on the SOAP service implementation. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the cancellation operation.
        """
        return self._call("CancelReservation", reservationIDs=reservation_ids.to_zeep() if reservation_ids else None)

    def create_reservation(self, customer_id: Optional[int] = None, customer_contact_id: Optional[int] = None) -> SoapResponse:
        """
        Create a new reservation for a customer.

        Args:
            customer_id (Optional[int], optional): The unique identifier of the customer. Defaults to None.
            customer_contact_id (Optional[int], optional): The unique identifier of the customer contact. Defaults to None.

        Returns:
            SoapResponse: The SOAP response object containing the result of the reservation creation operation.
        """
        return self._call("CreateReservation", customerID=customer_id, customerContactID=customer_contact_id)

    def create_reservation_inc_payment_method(self, customer_id: Optional[int] = None, customer_contact_id: Optional[int] = None, payment_method_id: Optional[int] = None) -> SoapResponse:
        """
        Create a reservation including payment method information.

        Args:
            customer_id (Optional[int], optional): The unique identifier of the customer. Defaults to None.
            customer_contact_id (Optional[int], optional): The unique identifier of the customer contact. Defaults to None.
            payment_method_id (Optional[int], optional): The unique identifier of the payment method. Defaults to None.
                Note: Maps to WSDL parameter 'paymentMetodID' (typo preserved from WSDL).

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation details.
        """
        return self._call("CreateReservationIncPaymentMethod", customerID=customer_id, customerContactID=customer_contact_id, paymentMetodID=payment_method_id)

    def get_reservation(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve reservation data with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP 'GetReservation' call.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservation", sort=sort_xml, filter=filter_xml)

    def get_reservation_answer(self, reservation_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Retrieves reservation answers for the specified reservation IDs.

        Args:
            reservation_ids (Optional[IntListSpec], optional): An optional list of reservation IDs to query.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the reservation answers.
        """
        return self._call("GetReservationAnswer", reservationIDs=reservation_ids.to_zeep() if reservation_ids else None)

    def get_reservation_answer_v2(self, reservation_ids: Optional[IntListSpec] = None) -> SoapResponse:
        """
        Retrieves reservation answers for the specified reservation IDs using the GetReservationAnswerV2 SOAP method.

        Args:
            reservation_ids (Optional[IntListSpec], optional): An optional list of reservation IDs to query.
                If provided, it will be serialized to XML. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing reservation answer details.
        """
        return self._call("GetReservationAnswerV2", reservationIDs=reservation_ids.to_zeep() if reservation_ids else None)

    def get_reservation_answer_list(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves a list of reservation answers from the SOAP service, with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification to order the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification to filter the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation answer list.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationAnswerList", sort=sort_xml, filter=filter_xml)

    def get_reservation_answer_list_v2(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves a list of reservation answers using the V2 API method, with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation answer list.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationAnswerListV2", sort=sort_xml, filter=filter_xml)

    def get_reservation_answer_list_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves a list of reservation answers in XML format, with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing the reservation answer list in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationAnswerListXml", sort=sort_xml, filter=filter_xml)

    def get_reservation_answer_list_xml_v2(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves a list of reservation answers in XML format (version 2), with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing the reservation answer list in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationAnswerListXmlV2", sort=sort_xml, filter=filter_xml)

    def get_reservation_pickup_address(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves the pickup address for a reservation, with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification to order the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification to filter the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation pickup address information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationPickupAddress", sort=sort_xml, filter=filter_xml)

    def get_reservation_pickup_address_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves the reservation pickup address information in XML format.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification to order the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification to filter the results. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing the reservation pickup address XML.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationPickupAddressXml", sort=sort_xml, filter=filter_xml)

    def get_reservation_questions(self) -> SoapResponse:
        """
        Retrieve reservation-related questions via the SOAP API.

        Returns:
            SoapResponse: The response object containing the reservation questions data.
        """
        return self._call("GetReservationQuestions")

    def get_reservation_shipping_address(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves the shipping address for a reservation.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification to order the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification to filter the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation shipping address information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationShippingAddress", sort=sort_xml, filter=filter_xml)

    def get_reservation_shipping_address_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves the shipping address information for reservations in XML format.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification to order the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification to filter the results. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing the reservation shipping address XML.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationShippingAddressXml", sort=sort_xml, filter=filter_xml)

    def get_reservation_v2(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves reservation data using the GetReservationV2 SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing reservation data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV2", sort=sort_xml, filter=filter_xml)

    def get_reservation_v2_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves reservation data in XML format using the GetReservationV2Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing the reservation data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV2Xml", sort=sort_xml, filter=filter_xml)

    def get_reservation_v3(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves reservation data using version 3 of the reservation API.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The response object containing the reservation data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV3", sort=sort_xml, filter=filter_xml)

    def get_reservation_v3_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves reservation data in XML format using the GetReservationV3Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the reservation data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV3Xml", sort=sort_xml, filter=filter_xml)

    def get_reservation_v4(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve reservation data using version 4 of the API.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The response object containing the reservation data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV4", sort=sort_xml, filter=filter_xml)

    def get_reservation_v5(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve reservation data using version 5 of the API.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification. Defaults to None.

        Returns:
            SoapResponse: The response object containing the reservation data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationV5", sort=sort_xml, filter=filter_xml)

    def get_reservation_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves reservation data in XML format, optionally applying sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): An optional sorting specification to order the reservations. Defaults to None.
            filtering (Optional[FilterSpec], optional): An optional filtering specification to filter the reservations. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing the reservation data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReservationXml", sort=sort_xml, filter=filter_xml)

    def remove_reservation_pickup_address(self, reservation_id: Optional[int] = None) -> SoapResponse:
        """
        Removes the pickup address associated with a reservation.

        Args:
            reservation_id (Optional[int], optional): The unique identifier of the reservation
                whose pickup address should be removed. Defaults to None.

        Returns:
            SoapResponse: The response object returned by the SOAP service.
        """
        return self._call("RemoveReservationPickupAddress", reservationID=reservation_id)

    def remove_reservation_shipping_address(self, reservation_id: Optional[int] = None) -> SoapResponse:
        """
        Removes the shipping address associated with a reservation.

        Args:
            reservation_id (Optional[int], optional): The unique identifier of the reservation
                whose shipping address should be removed. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service.
        """
        return self._call("RemoveReservationShippingAddress", reservationID=reservation_id)

    def set_reservation(
        self,
        customer_id: int,
        customer_contact_id: int,
        reservation_id: Optional[int] = None,
        tmp_order_id: int = 0,
        object_count: int = 1,
        description: Optional[str] = None,
        period_start: Optional[dt.datetime] = None,
        period_end: Optional[dt.datetime] = None,
        from_web: bool = False,
        activated: bool = False,
        returned: bool = False,
        customer_reference: Optional[str] = None,
        customer_notes: Optional[str] = None,
        purchase_order_number: Optional[str] = None,
        customer_shipping_address_lnk_id: int = 0,
        shipping_customer_contact_id: int = 0,
        payment_method_id: Optional[int] = None,
        order_sum: Decimal = Decimal(0),
        paid: bool = False,
        job_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Create or update a reservation.

        Args:
            reservation_id (Optional[int]): Reservation ID. Required in WSDL.
            tmp_order_id (int): Temporary order ID. Required in WSDL. Defaults to 0.
            customer_id (int): Customer ID. Required.
            customer_contact_id (int): Customer contact ID. Required.
            object_count (int): Object count. Required in WSDL. Defaults to 1.
            description (Optional[str]): Description.
            period_start (Optional[dt.datetime]): Period start datetime. Required in WSDL.
            period_end (Optional[dt.datetime]): Period end datetime. Required in WSDL.
            from_web (bool): Whether from web. Required in WSDL. Defaults to False.
            activated (bool): Whether activated. Required in WSDL. Defaults to False.
            returned (bool): Whether returned. Required in WSDL. Defaults to False.
            customer_reference (Optional[str]): Customer reference.
            customer_notes (Optional[str]): Customer notes.
            purchase_order_number (Optional[str]): Purchase order number.
            customer_shipping_address_lnk_id (int): Customer shipping address link ID. Required in WSDL. Defaults to 0.
            shipping_customer_contact_id (int): Shipping customer contact ID. Required in WSDL. Defaults to 0.
            payment_method_id (Optional[int]): Payment method ID. Nillable in WSDL.
            order_sum (Decimal): Order sum. Required in WSDL. Defaults to Decimal(0).
            paid (bool): Whether paid. Required in WSDL. Defaults to False.
            job_id (Optional[int]): Job ID. Nillable in WSDL.

        Returns:
            SoapResponse: The response from the SOAP service after attempting to set the reservation.
        """
        record = {k: v for k, v in {
            "ReservationID": reservation_id,
            "TmpOrderID": tmp_order_id,
            "CustomerID": customer_id,
            "ObjectCount": object_count,
            "CustomerContactID": customer_contact_id,
            "Description": description,
            "PeriodStart": period_start,
            "PeriodEnd": period_end,
            "FromWeb": from_web,
            "Activated": activated,
            "Returned": returned,
            "CustomerReference": customer_reference,
            "CustomerNotes": customer_notes,
            "PurchaseOrderNumber": purchase_order_number,
            "CustomerShippingAddressLnkID": customer_shipping_address_lnk_id,
            "ShippingCustomerContactID": shipping_customer_contact_id,
            "PaymentMethodID": payment_method_id,
            "OrderSum": order_sum,
            "Paid": paid,
            "JobID": job_id,
        }.items() if v is not None}
        return self._call("SetReservation", reservation=record)

    def set_reservation_v2(
        self,
        customer_id: int,
        customer_contact_id: int,
        external_reservation_id: Optional[int] = None,
        reservation_id: Optional[int] = None,
        tmp_order_id: int = 0,
        object_count: int = 1,
        description: Optional[str] = None,
        period_start: Optional[dt.datetime] = None,
        period_end: Optional[dt.datetime] = None,
        from_web: bool = False,
        activated: bool = False,
        returned: bool = False,
        customer_reference: Optional[str] = None,
        customer_notes: Optional[str] = None,
        purchase_order_number: Optional[str] = None,
        customer_shipping_address_lnk_id: int = 0,
        shipping_customer_contact_id: int = 0,
        payment_method_id: Optional[int] = None,
        order_sum: Decimal = Decimal(0),
        paid: bool = False,
        job_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Create or update a reservation using the SetReservationV2 SOAP method.

        Args:
            external_reservation_id (Optional[int]): External reservation ID. Nillable in WSDL.
            reservation_id (Optional[int]): Reservation ID. Required in WSDL.
            tmp_order_id (int): Temporary order ID. Required in WSDL. Defaults to 0.
            customer_id (int): Customer ID. Required.
            customer_contact_id (int): Customer contact ID. Required.
            object_count (int): Object count. Required in WSDL. Defaults to 1.
            description (Optional[str]): Description.
            period_start (Optional[dt.datetime]): Period start datetime. Required in WSDL.
            period_end (Optional[dt.datetime]): Period end datetime. Required in WSDL.
            from_web (bool): Whether from web. Required in WSDL. Defaults to False.
            activated (bool): Whether activated. Required in WSDL. Defaults to False.
            returned (bool): Whether returned. Required in WSDL. Defaults to False.
            customer_reference (Optional[str]): Customer reference.
            customer_notes (Optional[str]): Customer notes.
            purchase_order_number (Optional[str]): Purchase order number.
            customer_shipping_address_lnk_id (int): Customer shipping address link ID. Required in WSDL. Defaults to 0.
            shipping_customer_contact_id (int): Shipping customer contact ID. Required in WSDL. Defaults to 0.
            payment_method_id (Optional[int]): Payment method ID. Nillable in WSDL.
            order_sum (Decimal): Order sum. Required in WSDL. Defaults to Decimal(0).
            paid (bool): Whether paid. Required in WSDL. Defaults to False.
            job_id (Optional[int]): Job ID. Nillable in WSDL.

        Returns:
            SoapResponse: The response object from the SOAP call.
        """
        record = {k: v for k, v in {
            "ExternalReservationID": external_reservation_id,
            "ReservationID": reservation_id,
            "TmpOrderID": tmp_order_id,
            "CustomerID": customer_id,
            "ObjectCount": object_count,
            "CustomerContactID": customer_contact_id,
            "Description": description,
            "PeriodStart": period_start,
            "PeriodEnd": period_end,
            "FromWeb": from_web,
            "Activated": activated,
            "Returned": returned,
            "CustomerReference": customer_reference,
            "CustomerNotes": customer_notes,
            "PurchaseOrderNumber": purchase_order_number,
            "CustomerShippingAddressLnkID": customer_shipping_address_lnk_id,
            "ShippingCustomerContactID": shipping_customer_contact_id,
            "PaymentMethodID": payment_method_id,
            "OrderSum": order_sum,
            "Paid": paid,
            "JobID": job_id,
        }.items() if v is not None}
        return self._call("SetReservationV2", reservation=record)

    def set_reservation_v3(
        self,
        customer_id: int,
        customer_contact_id: int,
        reservation_number: Optional[str] = None,
        created: Optional[dt.datetime] = None,
        external_reservation_id: Optional[int] = None,
        reservation_id: Optional[int] = None,
        tmp_order_id: int = 0,
        object_count: int = 1,
        description: Optional[str] = None,
        period_start: Optional[dt.datetime] = None,
        period_end: Optional[dt.datetime] = None,
        from_web: bool = False,
        activated: bool = False,
        returned: bool = False,
        customer_reference: Optional[str] = None,
        customer_notes: Optional[str] = None,
        purchase_order_number: Optional[str] = None,
        customer_shipping_address_lnk_id: int = 0,
        shipping_customer_contact_id: int = 0,
        payment_method_id: Optional[int] = None,
        order_sum: Decimal = Decimal(0),
        paid: bool = False,
        job_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Create or update a reservation using the SetReservationV3 SOAP method.

        Args:
            reservation_number (Optional[str]): Reservation number.
            created (Optional[dt.datetime]): Creation datetime. Required in WSDL. Defaults to now.
            external_reservation_id (Optional[int]): External reservation ID. Nillable in WSDL.
            reservation_id (Optional[int]): Reservation ID. Required in WSDL.
            tmp_order_id (int): Temporary order ID. Required in WSDL. Defaults to 0.
            customer_id (int): Customer ID. Required.
            customer_contact_id (int): Customer contact ID. Required.
            object_count (int): Object count. Required in WSDL. Defaults to 1.
            description (Optional[str]): Description.
            period_start (Optional[dt.datetime]): Period start datetime. Required in WSDL.
            period_end (Optional[dt.datetime]): Period end datetime. Required in WSDL.
            from_web (bool): Whether from web. Required in WSDL. Defaults to False.
            activated (bool): Whether activated. Required in WSDL. Defaults to False.
            returned (bool): Whether returned. Required in WSDL. Defaults to False.
            customer_reference (Optional[str]): Customer reference.
            customer_notes (Optional[str]): Customer notes.
            purchase_order_number (Optional[str]): Purchase order number.
            customer_shipping_address_lnk_id (int): Customer shipping address link ID. Required in WSDL. Defaults to 0.
            shipping_customer_contact_id (int): Shipping customer contact ID. Required in WSDL. Defaults to 0.
            payment_method_id (Optional[int]): Payment method ID. Nillable in WSDL.
            order_sum (Decimal): Order sum. Required in WSDL. Defaults to Decimal(0).
            paid (bool): Whether paid. Required in WSDL. Defaults to False.
            job_id (Optional[int]): Job ID. Nillable in WSDL.

        Returns:
            SoapResponse: The response from the SOAP service after setting the reservation.
        """
        record = {k: v for k, v in {
            "ReservationNumber": reservation_number,
            "Created": created or dt.datetime.now(),
            "ExternalReservationID": external_reservation_id,
            "ReservationID": reservation_id,
            "TmpOrderID": tmp_order_id,
            "CustomerID": customer_id,
            "ObjectCount": object_count,
            "CustomerContactID": customer_contact_id,
            "Description": description,
            "PeriodStart": period_start,
            "PeriodEnd": period_end,
            "FromWeb": from_web,
            "Activated": activated,
            "Returned": returned,
            "CustomerReference": customer_reference,
            "CustomerNotes": customer_notes,
            "PurchaseOrderNumber": purchase_order_number,
            "CustomerShippingAddressLnkID": customer_shipping_address_lnk_id,
            "ShippingCustomerContactID": shipping_customer_contact_id,
            "PaymentMethodID": payment_method_id,
            "OrderSum": order_sum,
            "Paid": paid,
            "JobID": job_id,
        }.items() if v is not None}
        return self._call("SetReservationV3", reservationV3=record)

    def set_reservation_v4(
        self,
        customer_id: int,
        customer_contact_id: int,
        invoice_notes: Optional[str] = None,
        reservation_number: Optional[str] = None,
        created: Optional[dt.datetime] = None,
        external_reservation_id: Optional[int] = None,
        reservation_id: Optional[int] = None,
        tmp_order_id: int = 0,
        object_count: int = 1,
        description: Optional[str] = None,
        period_start: Optional[dt.datetime] = None,
        period_end: Optional[dt.datetime] = None,
        from_web: bool = False,
        activated: bool = False,
        returned: bool = False,
        customer_reference: Optional[str] = None,
        customer_notes: Optional[str] = None,
        purchase_order_number: Optional[str] = None,
        customer_shipping_address_lnk_id: int = 0,
        shipping_customer_contact_id: int = 0,
        payment_method_id: Optional[int] = None,
        order_sum: Decimal = Decimal(0),
        paid: bool = False,
        job_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Create or update a reservation using the SetReservationV4 SOAP method.

        Args:
            invoice_notes (Optional[str]): Invoice notes.
            reservation_number (Optional[str]): Reservation number.
            created (Optional[dt.datetime]): Creation datetime. Required in WSDL. Defaults to now.
            external_reservation_id (Optional[int]): External reservation ID. Nillable in WSDL.
            reservation_id (Optional[int]): Reservation ID. Required in WSDL.
            tmp_order_id (int): Temporary order ID. Required in WSDL. Defaults to 0.
            customer_id (int): Customer ID. Required.
            customer_contact_id (int): Customer contact ID. Required.
            object_count (int): Object count. Required in WSDL. Defaults to 1.
            description (Optional[str]): Description.
            period_start (Optional[dt.datetime]): Period start datetime. Required in WSDL.
            period_end (Optional[dt.datetime]): Period end datetime. Required in WSDL.
            from_web (bool): Whether from web. Required in WSDL. Defaults to False.
            activated (bool): Whether activated. Required in WSDL. Defaults to False.
            returned (bool): Whether returned. Required in WSDL. Defaults to False.
            customer_reference (Optional[str]): Customer reference.
            customer_notes (Optional[str]): Customer notes.
            purchase_order_number (Optional[str]): Purchase order number.
            customer_shipping_address_lnk_id (int): Customer shipping address link ID. Required in WSDL. Defaults to 0.
            shipping_customer_contact_id (int): Shipping customer contact ID. Required in WSDL. Defaults to 0.
            payment_method_id (Optional[int]): Payment method ID. Nillable in WSDL.
            order_sum (Decimal): Order sum. Required in WSDL. Defaults to Decimal(0).
            paid (bool): Whether paid. Required in WSDL. Defaults to False.
            job_id (Optional[int]): Job ID. Nillable in WSDL.

        Returns:
            SoapResponse: The response object from the SOAP call.
        """
        record = {k: v for k, v in {
            "Created": created or dt.datetime.now(),
            "InvoiceNotes": invoice_notes,
            "ReservationNumber": reservation_number,
            "ExternalReservationID": external_reservation_id,
            "ReservationID": reservation_id,
            "TmpOrderID": tmp_order_id,
            "CustomerID": customer_id,
            "ObjectCount": object_count,
            "CustomerContactID": customer_contact_id,
            "Description": description,
            "PeriodStart": period_start,
            "PeriodEnd": period_end,
            "FromWeb": from_web,
            "Activated": activated,
            "Returned": returned,
            "CustomerReference": customer_reference,
            "CustomerNotes": customer_notes,
            "PurchaseOrderNumber": purchase_order_number,
            "CustomerShippingAddressLnkID": customer_shipping_address_lnk_id,
            "ShippingCustomerContactID": shipping_customer_contact_id,
            "PaymentMethodID": payment_method_id,
            "OrderSum": order_sum,
            "Paid": paid,
            "JobID": job_id,
        }.items() if v is not None}

        return self._call("SetReservationV4", reservation=record)

    def set_reservation_account_number(self, reservation_id: Optional[int] = None, account_number: Optional[str] = None) -> SoapResponse:
        """
        Sets the account number for a specific reservation.

        Args:
            reservation_id (Optional[int], optional): The unique identifier of the reservation to update. Defaults to None.
            account_number (Optional[str], optional): The account number to associate with the reservation. Defaults to None.

        Returns:
            SoapResponse: The response object returned by the SOAP service.
        """
        return self._call("SetReservationAccountNumber", reservationID=reservation_id, accountNumber=account_number)

    def set_reservation_answer(
        self,
        reservation_answer_id: Optional[int] = None,
        question_id: Optional[int] = None,
        answer_id: Optional[int] = None,
        answer_text: Optional[str] = None,
        reservation_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set answers for a reservation.

        Args:
            reservation_answer_id (Optional[int]): Reservation answer ID. Required in WSDL.
            question_id (Optional[int]): Question ID. Required in WSDL.
            answer_id (Optional[int]): Answer ID. Required in WSDL.
            answer_text (Optional[str]): Answer text.
            reservation_id (Optional[int]): Reservation ID. Required in WSDL.

        Returns:
            SoapResponse: The response from the SOAP service after setting the reservation answer.
        """
        record = {k: v for k, v in {
            "ReservationAnswerID": reservation_answer_id,
            "QuestionID": question_id,
            "AnswerID": answer_id,
            "AnswerText": answer_text,
            "ReservationID": reservation_id,
        }.items() if v is not None}
        return self._call("SetReservationAnswer", reservationAnswerList={"ReservationAnswer": [record]})

    def set_reservation_answer_v2(
        self,
        answer_number: Optional[int] = None,
        answer_time: Optional[str] = None,
        reservation_answer_id: Optional[int] = None,
        question_id: Optional[int] = None,
        answer_id: Optional[int] = None,
        answer_text: Optional[str] = None,
        reservation_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set or update answers for a reservation using the V2 API.

        Args:
            answer_number (Optional[int]): Answer number. Required in WSDL.
            answer_time (Optional[str]): Answer time.
            reservation_answer_id (Optional[int]): Reservation answer ID. Required in WSDL.
            question_id (Optional[int]): Question ID. Required in WSDL.
            answer_id (Optional[int]): Answer ID. Required in WSDL.
            answer_text (Optional[str]): Answer text.
            reservation_id (Optional[int]): Reservation ID. Required in WSDL.

        Returns:
            SoapResponse: The response object returned by the SOAP service.
        """
        record = {k: v for k, v in {
            "AnswerNumber": answer_number,
            "AnswerTime": answer_time,
            "ReservationAnswerID": reservation_answer_id,
            "QuestionID": question_id,
            "AnswerID": answer_id,
            "AnswerText": answer_text,
            "ReservationID": reservation_id,
        }.items() if v is not None}
        return self._call("SetReservationAnswerV2", reservationAnswerList={"ReservationAnswerV2": [record]})

    def set_reservation_pickup_address(self, reservation_id: Optional[int] = None, customer_shipping_address_lnk_id: Optional[int] = None) -> SoapResponse:
        """
        Sets the pickup address for a reservation.

        Args:
            reservation_id (Optional[int], optional): The unique identifier of the reservation. Defaults to None.
            customer_shipping_address_lnk_id (Optional[int], optional): The link ID of the customer's shipping address. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service.
        """
        return self._call("SetReservationPickupAddress", reservationID=reservation_id, customerShippingAddressLnkID=customer_shipping_address_lnk_id)

    def set_reservation_shipping_address(self, reservation_id: Optional[int] = None, customer_shipping_address_lnk_id: Optional[int] = None) -> SoapResponse:
        """
        Sets the shipping address for a reservation.

        Args:
            reservation_id (Optional[int], optional): The unique identifier of the reservation to update. Defaults to None.
            customer_shipping_address_lnk_id (Optional[int], optional): The unique identifier linking the customer to the shipping address. Defaults to None.

        Returns:
            SoapResponse: The response object returned by the SOAP service.
        """
        return self._call("SetReservationShippingAddress", reservationID=reservation_id, customerShippingAddressLnkID=customer_shipping_address_lnk_id)

    def set_reservation_shipping_method(self, reservation_id: Optional[int] = None, shipping_method_id: Optional[int] = None) -> SoapResponse:
        """
        Sets the shipping method for a specific reservation.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation to update. Defaults to None.
            shipping_method_id (Optional[int], optional): The ID of the shipping method to set. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service after setting the shipping method.
        """
        return self._call("SetReservationShippingMethod", reservationID=reservation_id, shippingMethodID=shipping_method_id)

    def update_reservation_discount(self, reservation_id: Optional[int] = None, discount_percent: Optional[float] = None) -> SoapResponse:
        """
        Updates the discount percentage for a specific reservation.

        Args:
            reservation_id (Optional[int], optional): The unique identifier of the reservation to update. Defaults to None.
            discount_percent (Optional[float], optional): The new discount percentage to apply to the reservation. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service after updating the reservation discount.
        """
        return self._call("UpdateReservationDiscount", reservationID=reservation_id, discountPercent=discount_percent)
