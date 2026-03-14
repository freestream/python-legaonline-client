from __future__ import annotations

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

    def get_company_logo_url(self) -> SoapResponse:
        """
        Get the URL of the company logo.

        Returns:
            SoapResponse: A response object containing the company logo URL from the SOAP service.
        """
        return self._call("GetCompanyLogoUrl")
