from __future__ import annotations

import datetime as dt
from typing import Optional

from zeep.client import Client as ZeepClient
from zeep.settings import Settings as ZeepSettings

from .auth import AuthManager, Credentials
from .timezone import get_default_tzinfo
from .services import CustomerService


class Client:
    """
    A SOAP client for interacting with the Lega Online Rental API.
    This client provides a high-level interface to the Lega Online API services,
    handling authentication, timezone management, and service access.
    Args:
        creds (Credentials): Authentication credentials for the API.
        wsdl_url (str, optional): URL to the WSDL definition. 
            Defaults to "https://api.legaonline.se/rentalapi.asmx?wsdl".
        zeep_client (Optional[ZeepClient], optional): Pre-configured Zeep client instance.
            If not provided, a new client will be created. Defaults to None.
        authenticate_on_init (bool, optional): Whether to authenticate immediately upon
            initialization. Defaults to True.
        tzinfo (Optional[dt.tzinfo], optional): Timezone information to use for datetime
            operations. If not provided, uses the default timezone. Defaults to None.
    Attributes:
        zeep_client (ZeepClient): The underlying Zeep SOAP client.
        auth (AuthManager): Manager for handling API authentication.
        tzinfo (dt.tzinfo): Timezone information for datetime operations.
        customers (CustomerService): Service interface for customer-related operations.
    """
    __slots__ = ("zeep_client", "auth", "tzinfo", "customers")
    
    def __init__(
        self,
        *,
        creds: Credentials,
        wsdl_url: str = "https://api.legaonline.se/rentalapi.asmx?wsdl",
        zeep_client: Optional[ZeepClient] = None,
        authenticate_on_init: bool = True,
        tzinfo: Optional[dt.tzinfo] = None,
    ) -> None:
        if not zeep_client:
            settings = ZeepSettings(strict=False, xml_huge_tree=True)
            zeep_client = ZeepClient(wsdl=wsdl_url, settings=settings)

        self.zeep_client: ZeepClient = zeep_client
        self.auth: AuthManager = AuthManager(self.zeep_client.service, creds)

        if authenticate_on_init:
            self.auth.authenticate()

        self.tzinfo: dt.tzinfo = tzinfo or get_default_tzinfo()

        self.customers: CustomerService = CustomerService(self.zeep_client.service, self.auth, self.tzinfo)