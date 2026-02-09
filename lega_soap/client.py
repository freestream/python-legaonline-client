from __future__ import annotations

import datetime as dt
from typing import Optional, TYPE_CHECKING, Any

from .auth import AuthManager, Credentials
from .timezone import get_default_tzinfo
from .services import (
    AuthService,
    AccountService,
    AvailabilityService,
    CalendarService,
    CatalogService,
    CommunicationService,
    CustomerService,
    GeoService,
    IntegrationService,
    JobService,
    ObjectService,
    OccasionService,
    OrderService,
    ReportService,
    ReservationService,
    ShippingService,
    MiscService,
)

if TYPE_CHECKING:  # pragma: no cover
    from zeep.client import Client as ZeepClient


class Client:
    """High-level client for the Lega Online Rental API."""

    __slots__ = (
        "zeep_client",
        "auth",
        "tzinfo",
        "auth_service",
        "accounts",
        "availability",
        "calendar",
        "catalog",
        "communication",
        "customers",
        "geo",
        "integration",
        "jobs",
        "objects",
        "occasions",
        "orders",
        "reports",
        "reservations",
        "shipping",
        "misc",
    )

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
            from zeep.client import Client as ZeepClient  # local import
            from zeep.settings import Settings as ZeepSettings  # local import

            settings = ZeepSettings(strict=False, xml_huge_tree=True)
            zeep_client = ZeepClient(wsdl=wsdl_url, settings=settings)

        self.zeep_client: Any = zeep_client
        self.tzinfo: dt.tzinfo = tzinfo or get_default_tzinfo()

        # Auth manager (token lifecycle)
        self.auth: AuthManager = AuthManager(self.zeep_client.service, creds)
        if authenticate_on_init:
            self.auth.authenticate()

        # Services that use authToken injected by BaseService
        self.customers: CustomerService = CustomerService(self.zeep_client.service, self.auth, self.tzinfo)
        self.reservations: ReservationService = ReservationService(self.zeep_client.service, self.auth, self.tzinfo)
        self.occasions: OccasionService = OccasionService(self.zeep_client.service, self.auth, self.tzinfo)
        self.accounts: AccountService = AccountService(self.zeep_client.service, self.auth, self.tzinfo)
        self.availability: AvailabilityService = AvailabilityService(self.zeep_client.service, self.auth, self.tzinfo)
        self.catalog: CatalogService = CatalogService(self.zeep_client.service, self.auth, self.tzinfo)
        self.objects: ObjectService = ObjectService(self.zeep_client.service, self.auth, self.tzinfo)
        self.orders: OrderService = OrderService(self.zeep_client.service, self.auth, self.tzinfo)
        self.communication: CommunicationService = CommunicationService(self.zeep_client.service, self.auth, self.tzinfo)
        self.jobs: JobService = JobService(self.zeep_client.service, self.auth, self.tzinfo)
        self.geo: GeoService = GeoService(self.zeep_client.service, self.auth, self.tzinfo)
        self.calendar: CalendarService = CalendarService(self.zeep_client.service, self.auth, self.tzinfo)
        self.integration: IntegrationService = IntegrationService(self.zeep_client.service, self.auth, self.tzinfo)
        self.reports: ReportService = ReportService(self.zeep_client.service, self.auth, self.tzinfo)
        self.shipping: ShippingService = ShippingService(self.zeep_client.service, self.auth, self.tzinfo)
        self.misc: MiscService = MiscService(self.zeep_client.service, self.auth, self.tzinfo)

        # Methods without authToken parameter (direct Zeep call)
        self.auth_service: AuthService = AuthService(self.zeep_client.service, self.tzinfo)
