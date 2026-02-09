from __future__ import annotations

from typing import Any, Callable, Dict
import datetime as dt

from zeep.helpers import serialize_object

from ..exceptions import ServiceError
from ..sanitize import sanitize_object
from ..types import SoapResponse


_EMPTY = (None, "", [], {}, ())


class BaseService:
    """
    Base service class for SOAP API interactions.

    This class provides a foundation for making SOAP service calls with authentication,
    error handling, and response serialization/sanitization.

    Attributes:
        _service: The underlying Zeep SOAP service instance.
        _auth: Authentication manager for handling tokens.
        _tzinfo: Timezone information for date/time serialization.

    Args:
        zeep_service: A Zeep service instance for making SOAP calls.
        auth_manager: An authentication manager that provides valid tokens.
        tzinfo: Timezone information to be used for datetime objects.

    Methods:
        _call: Execute a SOAP service method with authentication and error handling.

    Raises:
        ServiceError: When a SOAP method is not found or when execution fails.
    """
    __slots__ = ("_service", "_auth", "_tzinfo")
    
    def __init__(
        self,
        zeep_service: Any,
        auth_manager: Any,
        tzinfo: dt.tzinfo,
    ) -> None:
        """
        Initialize the base service with required dependencies.

        Args:
            zeep_service (Any): The Zeep SOAP service client instance used for making SOAP requests.
            auth_manager (Any): The authentication manager handling credentials and authorization.
            tzinfo (dt.tzinfo): Timezone information object for handling datetime conversions.

        Returns:
            None
        """
        self._service: Any = zeep_service
        self._auth: Any = auth_manager
        self._tzinfo: dt.tzinfo = tzinfo

    def _call(self, method_name: str, *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Execute a SOAP service method with authentication and error handling.

        This method ensures a valid authentication token, calls the specified SOAP method
        with provided arguments, and processes the response through serialization and sanitization.

        Args:
            method_name (str): The name of the SOAP method to call on the service.
            *args (Any): Positional arguments to pass to the SOAP method.
            **kwargs (Any): Keyword arguments to pass to the SOAP method. Arguments with
                values in _EMPTY will be filtered out.

        Returns:
            SoapResponse: The sanitized and serialized response from the SOAP method call,
                with timezone information applied.

        Raises:
            ServiceError: If the SOAP method is not found on the service, or if the method
                call fails for any reason. The original exception is chained for context.

        Example:
            >>> response = self._call('GetCustomer', customer_id=123)
            >>> response = self._call('UpdateOrder', order_data, status='completed')
        """
        token = self._auth.ensure_valid_token()

        try:
            method: Callable[..., Any] = getattr(self._service, method_name)
        except AttributeError as e:
            raise ServiceError(f"SOAP method not found: {method_name}") from e

        filtered_kwargs: Dict[str, Any] = {k: v for k, v in kwargs.items() if v not in _EMPTY}

        try:
            result = method(token, *args, **filtered_kwargs)
        except Exception as e:
            raise ServiceError(f"{method_name} failed: {e}") from e

        serialized = serialize_object(result)
        return sanitize_object(serialized, self._tzinfo)

class BaseServiceNoAuth:
    """
    Base service class for SOAP operations that do not require authentication.
    This class provides a foundation for making unauthenticated SOAP service calls
    with automatic serialization, sanitization, and timezone handling.
    Attributes:
        _service (Any): The underlying Zeep SOAP service instance.
        _tzinfo (dt.tzinfo): Timezone information used for datetime sanitization.
    Args:
        zeep_service (Any): A Zeep service object used to make SOAP calls.
        tzinfo (dt.tzinfo): Timezone information for datetime conversion.
    Raises:
        ServiceError: If the SOAP method is not found or if the method call fails.
    Example:
        >>> from datetime import timezone
        >>> service = BaseServiceNoAuth(zeep_service, timezone.utc)
        >>> response = service._call_noauth('GetData', param1='value1')
    """
    

    __slots__ = ("_service", "_tzinfo")

    def __init__(self, zeep_service: Any, tzinfo: dt.tzinfo) -> None:
        """
        Initialize the base service with a Zeep service instance and timezone information.

        Args:
            zeep_service (Any): The Zeep SOAP service instance used for making SOAP requests.
            tzinfo (dt.tzinfo): Timezone information object for handling datetime conversions.

        Returns:
            None
        """
        self._service: Any = zeep_service
        self._tzinfo: dt.tzinfo = tzinfo

    def _call_noauth(self, method_name: str, *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Call a SOAP service method without authentication.

        This method invokes a SOAP service method by name, filters out empty parameters,
        and processes the response by serializing and sanitizing the result.

        Args:
            method_name (str): The name of the SOAP method to call.
            *args (Any): Positional arguments to pass to the SOAP method.
            **kwargs (Any): Keyword arguments to pass to the SOAP method. Arguments with
                empty values (as defined in _EMPTY) will be filtered out.

        Returns:
            SoapResponse: The sanitized and serialized response from the SOAP method call.

        Raises:
            ServiceError: If the SOAP method is not found or if the method call fails.

        Note:
            The response is automatically serialized and sanitized using the service's
            timezone information before being returned.
        """
        try:
            method: Callable[..., Any] = getattr(self._service, method_name)
        except AttributeError as e:
            raise ServiceError(f"SOAP method not found: {method_name}") from e

        filtered_kwargs: Dict[str, Any] = {k: v for k, v in kwargs.items() if v not in _EMPTY}

        try:
            result = method(*args, **filtered_kwargs)
        except Exception as e:
            raise ServiceError(f"{method_name} failed: {e}") from e

        serialized = serialize_object(result)
        return sanitize_object(serialized, self._tzinfo)
