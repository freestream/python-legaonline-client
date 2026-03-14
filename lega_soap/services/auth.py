from __future__ import annotations

from typing import Optional

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

    def get_auth_token(self, user_id: Optional[int] = None, hash_str: Optional[str] = None) -> SoapResponse:
        """
        Get an authentication token from the SOAP service.

        This method calls the GetAuthToken SOAP operation without prior authentication
        to obtain an auth token for subsequent authenticated requests.

        Args:
            user_id (Optional[int], optional): The user ID for authentication. Defaults to None.
            hash_str (Optional[str], optional): The hash string for authentication. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the authentication token.
        """
        return self._call_noauth("GetAuthToken", userID=user_id, hash=hash_str)

    def login_user(self, username: Optional[str] = None, password: Optional[str] = None) -> SoapResponse:
        """
        Authenticate a user with the SOAP service using username and password.

        This method calls the 'LoginUser' SOAP endpoint without requiring prior authentication.
        It is typically used to obtain authentication credentials for subsequent API calls.

        Args:
            username (Optional[str], optional): The username for authentication. Defaults to None.
            password (Optional[str], optional): The password for authentication. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing authentication result,
                          typically including a session token or authentication credentials.
        """
        return self._call_noauth("LoginUser", username=username, password=password)

    def login_user_xml(self, username: Optional[str] = None, password: Optional[str] = None) -> SoapResponse:
        """
        Authenticate a user using XML-based SOAP login.

        This method calls the LoginUserXml SOAP service without authentication to log in a user
        with the provided credentials.

        Args:
            username (Optional[str], optional): The username for authentication. Defaults to None.
            password (Optional[str], optional): The password for authentication. Defaults to None.

        Returns:
            SoapResponse: The SOAP response object containing the authentication result.
        """
        return self._call_noauth("LoginUserXml", username=username, password=password)

    def validate_auth_token(self) -> SoapResponse:
        """
        Validates an authentication token.

        Returns:
            SoapResponse: The response from the SOAP service containing validation results.

        Note:
            This method calls the 'ValidateAuthToken' SOAP operation without authentication.
        """
        return self._call_noauth("ValidateAuthToken")
