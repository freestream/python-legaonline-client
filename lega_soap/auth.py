from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Any

from .exceptions import AuthError


@dataclass(frozen=True, slots=True)
class Credentials:
    """
    A class representing user authentication credentials for the Lega SOAP API.

    Attributes:
        user_id (int): The unique identifier for the user.
        hash (str): The authentication hash/token for the user.
    """
    user_id: int
    hash: str


class AuthManager:
    """
    Manages authentication tokens for SOAP service communication.

    This class handles authentication token lifecycle including acquisition,
    validation, and automatic renewal. It interacts with a SOAP service to
    obtain and validate authentication tokens using provided credentials.

    Attributes:
        _service (Any): The Zeep SOAP service instance used for authentication operations.
        _creds (Credentials): User credentials containing user_id and hash for authentication.
        _token (Optional[str]): The current authentication token, None if not yet authenticated.

    Properties:
        token (str): Returns the current authentication token.
            Raises AuthError if token hasn't been initialized.

    Methods:
        authenticate() -> str:
            Obtains a new authentication token from the SOAP service.
            Raises AuthError if token acquisition fails or returns empty.
            
        validate() -> bool:
            Validates the current authentication token with the SOAP service.
            Returns False if no token exists or validation fails.
            
        ensure_valid_token() -> str:
            Ensures a valid token exists, validating current token or
            obtaining a new one if necessary. Returns a valid token.

    Raises:
        AuthError: When token initialization fails, token is accessed before
            authentication, or when GetAuthToken operation fails.

    Example:
        >>> auth_manager = AuthManager(zeep_service, credentials)
        >>> token = auth_manager.authenticate()
        >>> if auth_manager.validate():
        ...     # Use token for authenticated requests
        ...     pass
    """
    __slots__ = ("_service", "_creds", "_token")
    
    def __init__(
        self,
        zeep_service: Any,
        creds: Credentials,
    ) -> None:
        self._service: Any = zeep_service
        self._creds: Credentials = creds
        self._token: Optional[str] = None

    @property
    def token(self) -> str:
        """
        Get the authentication token.

        Returns:
            str: The authentication token.

        Raises:
            AuthError: If the authentication token has not been initialized.
                Call authenticate() first to obtain a token.
        """
        if not self._token:
            raise AuthError("Auth token not initialized. Call authenticate() first.")
        return self._token

    def authenticate(self) -> str:
        """
        Authenticate with the SOAP service and retrieve an authentication token.

        This method calls the SOAP service's GetAuthToken method using the stored
        credentials (user_id and hash). If successful, it stores the token internally
        and returns it.

        Returns:
            str: The authentication token retrieved from the service.

        Raises:
            AuthError: If the GetAuthToken call fails or returns an empty token.
                The exception message will contain details about the failure.

        Example:
            >>> auth = SomeAuthClass(service, credentials)
            >>> token = auth.authenticate()
            >>> print(token)
            'abc123xyz...'
        """
        try:
            token = self._service.GetAuthToken(self._creds.user_id, self._creds.hash)
        except Exception as e:
            raise AuthError(f"GetAuthToken failed: {e}") from e

        if not token:
            raise AuthError("GetAuthToken returned empty token.")

        self._token = token
        return token

    def validate(self) -> bool:
        """
        Validate the current authentication token.

        This method checks if the authentication token is valid by first verifying
        that a token exists, then calling the service's ValidateAuthToken method.

        Returns:
            bool: True if the token exists and is valid according to the service,
                  False if no token exists, validation fails, or an exception occurs
                  during validation.

        Raises:
            None: All exceptions are caught and result in a False return value.
        """
        if not self._token:
            return False
        try:
            return bool(self._service.ValidateAuthToken(self._token))
        except Exception:
            return False

    def ensure_valid_token(self) -> str:
        """
        Ensures a valid authentication token is available.

        If a token exists and is still valid, returns the existing token.
        Otherwise, authenticates and returns a new token.

        Returns:
            str: A valid authentication token.
        """
        if self._token and self.validate():
            return self._token
        return self.authenticate()
