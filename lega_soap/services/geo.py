from __future__ import annotations

from typing import Optional

from ..types import SoapResponse
from .base import BaseService

class GeoService(BaseService):
    """
    Service for handling geographic data operations via SOAP.

    This service provides methods to retrieve country information in various formats
    from the underlying SOAP service. All methods inherit from BaseService and utilize
    its _call method for making SOAP requests.

    The service supports optional language parameters for localized content.

    Attributes:
        Inherits all attributes from BaseService. Uses __slots__ = () to prevent
        dynamic attribute creation.

        >>> geo_service = GeoService(client)
        >>> countries = geo_service.get_countries(language="en")
        >>> countries_xml = geo_service.get_countries_xml(language="sv")
    """
    __slots__ = ()

    def get_countries(self, language: Optional[str] = None) -> SoapResponse:
        """
        Retrieve a list of countries from the SOAP service.

        Args:
            language (Optional[str], optional): The language code for localized country names.
                If None, the default language will be used. Defaults to None.

        Returns:
            SoapResponse: A response object containing the list of countries returned by
                the SOAP service.
        """
        return self._call("GetCountries", language=language)

    def get_countries_xml(self, language: Optional[str] = None) -> SoapResponse:
        """
        Retrieve a list of countries in XML format.

        Args:
            language (Optional[str], optional): The language code for the country names.
                If None, the default language will be used. Defaults to None.

        Returns:
            SoapResponse: A response object containing the XML data with country information.

        Example:
            >>> response = service.get_countries_xml(language="en")
            >>> response = service.get_countries_xml()
        """
        return self._call("GetCountriesXml", language=language)
