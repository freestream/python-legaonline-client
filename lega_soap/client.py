from __future__ import annotations

import datetime as dt
from typing import Optional, TYPE_CHECKING, Any

from .auth import AuthManager, Credentials
from .timezone import get_default_tzinfo
from .services import (
    CustomerService, 
    ReservationService
)

if TYPE_CHECKING:
    from zeep.client import Client as ZeepClient


class Client:
    """
    A client for interacting with the Lega Online SOAP API.

    This client provides a high-level interface for making requests to the Lega Online
    rental management system. It handles authentication, timezone management, and provides
    access to various service endpoints.

    Args:
        creds (Credentials): Authentication credentials for the API.
        wsdl_url (str, optional): URL to the WSDL definition. Defaults to the production
            Lega Online API endpoint.
        zeep_client (Optional[ZeepClient], optional): Pre-configured Zeep client instance.
            If not provided, a new client will be created with appropriate settings.
        authenticate_on_init (bool, optional): Whether to authenticate immediately upon
            initialization. Defaults to True.
        tzinfo (Optional[dt.tzinfo], optional): Timezone information for datetime operations.
            If not provided, the default timezone will be used.

    Attributes:
        zeep_client (ZeepClient): The underlying Zeep SOAP client.
        auth (AuthManager): Manager for handling authentication with the API.
        tzinfo (dt.tzinfo): Timezone information used for datetime operations.
        customers (CustomerService): Service interface for customer-related operations.

    Example:
        >>> from lega_soap import Client, Credentials
        >>> creds = Credentials(username="user", password="pass")
        >>> client = Client(creds=creds)
        >>> # Use client.customers to access customer operations
    """
    __slots__ = ("zeep_client", "auth", "tzinfo", "customers", "reservations")

    def __init__(
        self,
        *,
        creds: Credentials,
        wsdl_url: str = "https://api.legaonline.se/rentalapi.asmx?wsdl",
        zeep_client: Optional["ZeepClient"] = None,
        authenticate_on_init: bool = True,
        tzinfo: Optional[dt.tzinfo] = None,
    ) -> None:
        if zeep_client is None:
            from zeep.client import Client as ZeepClient
            from zeep.settings import Settings as ZeepSettings

            settings = ZeepSettings(strict=False, xml_huge_tree=True)
            zeep_client = ZeepClient(wsdl=wsdl_url, settings=settings)

        self.zeep_client = zeep_client
        self.auth = AuthManager(self.zeep_client.service, creds)

        if authenticate_on_init:
            self.auth.authenticate()

        self.tzinfo = tzinfo or get_default_tzinfo()
        self.customers = CustomerService(self.zeep_client.service, self.auth, self.tzinfo)
        self.reservations = ReservationService(self.zeep_client.service, self.auth, self.tzinfo)
