from __future__ import annotations

from typing import Any, Optional

from ..types import SoapResponse
from .base import BaseService

class GeoService(BaseService):
    """
    Service for handling geographic data operations via SOAP.

    This service provides methods to retrieve country information in various formats
    from the underlying SOAP service. All methods inherit from BaseService and utilize
    its _call method for making SOAP requests.

    The service supports optional language parameters for localized content and allows
    passing additional arguments to customize SOAP calls.

    Attributes:
        Inherits all attributes from BaseService. Uses __slots__ = () to prevent
        dynamic attribute creation.

        >>> geo_service = GeoService(client)
        >>> countries = geo_service.get_countries(language="en")
        >>> countries_xml = geo_service.get_countries_xml(language="sv")
    """
    __slots__ = ()

    def get_countries(self, *args: Any, language: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve a list of countries from the SOAP service.

        Args:
            language (Optional[str], optional): The language code for localized country names.
                If None, the default language will be used. Defaults to None.
            *args (Any): Additional positional arguments to pass to the SOAP call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: A response object containing the list of countries returned by
                the SOAP service.

        Raises:
            May raise exceptions from the underlying SOAP service call depending on
            the implementation of the _call method.
        """
        return self._call("GetCountries", *args, language=language, **kwargs)

    def get_countries_xml(self, *args: Any, language: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve a list of countries in XML format.

        Args:
            language (Optional[str], optional): The language code for the country names.
                If None, the default language will be used. Defaults to None.
            *args (Any): Additional positional arguments to pass to the underlying SOAP call.
            **kwargs (Any): Additional keyword arguments to pass to the underlying SOAP call.

        Returns:
            SoapResponse: A response object containing the XML data with country information.

        Example:
            >>> response = service.get_countries_xml(language="en")
            >>> response = service.get_countries_xml()
        """
        return self._call("GetCountriesXml", *args, language=language, **kwargs)
