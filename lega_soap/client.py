from __future__ import annotations

import datetime as dt
from typing import Optional

from zeep.client import Client as ZeepClient
from zeep.settings import Settings as ZeepSettings

from .auth import AuthManager, Credentials
from .timezone import get_default_tzinfo
from .services import CustomerService


class Client:
    def __init__(
        self,
        creds: Credentials,
        wsdl_url: str = "https://api.legaonline.se/rentalapi.asmx?wsdl",
        zeep_client: Optional[ZeepClient] = None,
        authenticate_on_init: bool = True,
        tzinfo: Optional[dt.tzinfo] = None,
    ):
        if not zeep_client:
            settings = ZeepSettings(strict=False, xml_huge_tree=True)
            zeep_client = ZeepClient(wsdl=wsdl_url, settings=settings)

        self.zeep_client = zeep_client
        self.auth = AuthManager(self.zeep_client.service, creds)

        if authenticate_on_init:
            self.auth.authenticate()

        self.tzinfo: dt.tzinfo = tzinfo or get_default_tzinfo()

        self.customers = CustomerService(self.zeep_client.service, self.auth, self.tzinfo)