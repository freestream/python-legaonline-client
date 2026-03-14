from __future__ import annotations

import datetime as dt
from typing import Any, Optional

from ..query import FilterSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService

class OrderService(BaseService):
    """
    Service class for managing rental orders via SOAP API.

    This class provides methods for order-related operations including price calculations,
    order retrieval, and payment validation. It inherits from BaseService and implements
    SOAP service calls for order management functionality.

    The OrderService handles:
    - Price calculations for single and multiple objects
    - Order retrieval with sorting and filtering capabilities
    - Payment validation for reservations
    - XML-formatted order data retrieval

    All methods return SoapResponse objects containing the results from the SOAP service calls.

        >>> # Calculate price for a rental
        >>> response = service.calculate_price(
        ...     object_id=123,
        ...     customer_id=456,
        ...     start_date=date(2024, 1, 1),
        ...     end_date=date(2024, 1, 7)
        ... )
        >>> # Retrieve orders with filtering
        >>> orders = service.get_orders(filtering=my_filter_spec)
    """
    __slots__ = ()

    def calculate_price(self, object_id: Optional[int] = None, customer_id: Optional[int] = None, start_date: Optional[dt.date] = None, end_date: Optional[dt.date] = None) -> SoapResponse:
        """
        Calculate the price for a rental order.

        Args:
            object_id (Optional[int], optional): The ID of the object to calculate price for. Defaults to None.
            customer_id (Optional[int], optional): The ID of the customer. Defaults to None.
            start_date (Optional[dt.date], optional): The start date of the rental period. Defaults to None.
            end_date (Optional[dt.date], optional): The end date of the rental period. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing the calculated price information.
        """
        return self._call("CalculatePrice", objectID=object_id, customerID=customer_id, startDate=start_date, endDate=end_date)

    def calculate_prices(
        self,
        customer_id: Optional[int] = None,
        customer_contact_id: Optional[int] = None,
        price_info: Optional[str] = None,
    ) -> SoapResponse:
        """
        Calculate prices for a customer and contact.

        Args:
            customer_id: The ID of the customer.
            customer_contact_id: The ID of the customer contact.
            price_info: XML string with price information.

        Returns:
            SoapResponse: The SOAP response containing the calculated prices.
        """
        return self._call("CalculatePrices", customerID=customer_id, customerContactID=customer_contact_id, priceInfo=price_info)

    def get_orders(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve orders from the SOAP service with optional sorting and filtering.

        This method calls the GetOrders SOAP operation to fetch orders. It supports
        optional sorting and filtering specifications that are converted to XML format
        before being passed to the SOAP service.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            sorting: Optional sorting specification that defines how orders should be sorted.
                     If provided, it will be converted to XML format using its to_xml() method.
            filtering: Optional filtering specification that defines which orders to retrieve.
                       If provided, it will be converted to XML format using its to_xml() method.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object containing the retrieved orders and metadata
                          from the SOAP service.

        Example:
            >>> service = OrderService()
            >>> response = service.get_orders(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOrders", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_orders_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve orders in XML format from the SOAP service.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting: Optional sorting specification to apply to the orders query.
                If provided, will be converted to XML format.
            filtering: Optional filtering specification to apply to the orders query.
                If provided, will be converted to XML format.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing orders in XML format.

        Example:
            >>> service = OrderService()
            >>> response = service.get_orders_xml(sorting=my_sort_spec, filtering=my_filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetOrdersXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def set_valid_payment(self, *args: Any, reservation_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Set a payment as valid for a reservation.

        This method calls the SOAP service's SetValidPayment operation to mark
        a payment as valid for the specified reservation.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            reservation_id: The ID of the reservation to set valid payment for.
                If None, the reservation_id must be provided in kwargs.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.
                Can include reservationID as an alternative to reservation_id parameter.

        Returns:
            SoapResponse: The response object from the SOAP service call containing
                the result of the SetValidPayment operation.

        Raises:
            Any exceptions raised by the underlying SOAP service call.
        """
        return self._call("SetValidPayment", *args, reservationID=reservation_id, **kwargs)
