from __future__ import annotations

from typing import Any, Optional

from ..types import SoapResponse
from .base import BaseServiceNoAuth


class AuthService(BaseServiceNoAuth):
    """
    SOAP authentication service for handling user authentication and token management.

    This service provides methods for authenticating users and managing authentication tokens
    through SOAP API calls. It inherits from BaseServiceNoAuth, indicating that these methods
    can be called without prior authentication (they are the authentication entry points).

    The service supports multiple authentication methods:
    - Token-based authentication using user ID and hash
    - Username/password authentication
    - XML-based username/password authentication
    - Token validation

    All methods return SoapResponse objects containing the results of the authentication
    operations, which typically include session tokens or authentication credentials for
    subsequent API calls.

    Attributes:
        __slots__ (tuple): Empty tuple to prevent dynamic attribute creation for memory efficiency.

    Example:
        >>> auth_service = AuthService(zeep_client, timezone_info)
        >>> response = auth_service.login_user(username="user@example.com", password="secret")
        >>> token_response = auth_service.get_auth_token(user_id=123, hash_str="hash_value")
        >>> validation = auth_service.validate_auth_token()
    """
    __slots__ = ()

    def get_auth_token(self, *args: Any, user_id: Optional[int] = None, hash_str: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Get an authentication token from the SOAP service.

        This method calls the GetAuthToken SOAP operation without prior authentication
        to obtain an auth token for subsequent authenticated requests.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            user_id (Optional[int], optional): The user ID for authentication. Defaults to None.
            hash_str (Optional[str], optional): The hash string for authentication. Defaults to None.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the authentication token.
        """
        return self._call_noauth("GetAuthToken", userID=user_id, hash=hash_str, *args, **kwargs)

    def login_user(self, *args: Any, username: Optional[str] = None, password: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Authenticate a user with the SOAP service using username and password.

        This method calls the 'LoginUser' SOAP endpoint without requiring prior authentication.
        It is typically used to obtain authentication credentials for subsequent API calls.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            username (Optional[str], optional): The username for authentication. Defaults to None.
            password (Optional[str], optional): The password for authentication. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing authentication result,
                          typically including a session token or authentication credentials.

        Raises:
            May raise exceptions from the underlying _call_noauth method, such as:
            - SOAPError: If the SOAP request fails
            - AuthenticationError: If the credentials are invalid
            - NetworkError: If there are connection issues
        """
        return self._call_noauth("LoginUser", username=username, password=password, *args, **kwargs)

    def login_user_xml(self, *args: Any, username: Optional[str] = None, password: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Authenticate a user using XML-based SOAP login.

        This method calls the LoginUserXml SOAP service without authentication to log in a user
        with the provided credentials.

        Args:
            *args: Variable length argument list to pass to the underlying SOAP call.
            username (Optional[str], optional): The username for authentication. Defaults to None.
            password (Optional[str], optional): The password for authentication. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the underlying SOAP call.

        Returns:
            SoapResponse: The SOAP response object containing the authentication result.

        Raises:
            SoapError: If the SOAP call fails or authentication is unsuccessful.
        """
        return self._call_noauth("LoginUserXml", username=username, password=password, *args, **kwargs)

    def validate_auth_token(self, *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Validates an authentication token.

        Args:
            *args: Variable length argument list to be passed to the SOAP service.
            **kwargs: Arbitrary keyword arguments to be passed to the SOAP service.

        Returns:
            SoapResponse: The response from the SOAP service containing validation results.

        Note:
            This method calls the 'ValidateAuthToken' SOAP operation without authentication.
        """
        return self._call_noauth("ValidateAuthToken", *args, **kwargs)
