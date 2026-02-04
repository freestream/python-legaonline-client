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
