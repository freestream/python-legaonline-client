from __future__ import annotations

from typing import Any

from ..types import SoapResponse
from .base import BaseService

class MiscService(BaseService):
    """
    Service class for handling miscellaneous SOAP operations.
    This class provides methods for various utility operations such as retrieving
    company information and assets through SOAP service calls.
    Inherits from:
        BaseService: Base class that provides core SOAP service functionality.
    Attributes:
        __slots__: Empty tuple to prevent dynamic attribute creation and reduce memory overhead.
    Example:
        >>> misc_service = MiscService()
        >>> response = misc_service.get_company_logo_url()
    """
    
    __slots__ = ()

    def get_company_logo_url(self, *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Get the URL of the company logo.

        Args:
            *args: Variable length argument list to be passed to the SOAP service.
            **kwargs: Arbitrary keyword arguments to be passed to the SOAP service.

        Returns:
            SoapResponse: A response object containing the company logo URL from the SOAP service.

        Raises:
            May raise exceptions from the underlying SOAP service call.
        """
        return self._call("GetCompanyLogoUrl", *args, **kwargs)
