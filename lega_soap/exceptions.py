class LegaError(RuntimeError):
    """
    Base exception class for LegaOnline SOAP API errors.

    This exception serves as the parent class for all LegaOnline-related exceptions,
    inheriting from RuntimeError to indicate errors that occur during the
    execution of LegaOnline SOAP operations.

    Raises:
        LegaError: Base exception for LegaOnline SOAP API operations.
    """
    pass


class AuthError(LegaError):
    """Exception raised when authentication with the LegaOnline SOAP API fails.

    This exception is raised when there are authentication-related errors,
    such as invalid credentials, expired tokens, or unauthorized access attempts.

    Inherits from:
        LegaError: Base exception class for LegaOnline-related errors.

    Example:
        >>> raise AuthError("Invalid API credentials provided")
    """
    pass


class ServiceError(LegaError):
    """
    Exception raised when a service-level error occurs in the LegaOnline SOAP API.

    This exception is raised when there are issues with the SOAP service itself,
    such as service unavailability, invalid service responses, or other
    service-related failures that prevent successful communication with the API.

    Inherits from:
        LegaError: Base exception class for LegaOnline-related errors.
    """
    pass