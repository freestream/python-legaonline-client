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
    """
    Client for interacting with the LegaOnline SOAP API.
    This class manages authentication and provides access to various service endpoints
    (e.g., customers, reservations, orders) via the LegaOnline API. It wraps a Zeep SOAP client
    and injects authentication tokens as needed for each service.
    Attributes:
        zeep_client (Any): The underlying Zeep SOAP client instance.
        auth (AuthManager): Manages authentication and token lifecycle.
        tzinfo (datetime.tzinfo): Timezone information used for date/time fields.
        auth_service (AuthService): Service for authentication-related operations (no auth token required).
        accounts (AccountService): Service for account-related operations.
        availability (AvailabilityService): Service for checking availability.
        calendar (CalendarService): Service for calendar-related operations.
        catalog (CatalogService): Service for catalog-related operations.
        communication (CommunicationService): Service for communication-related operations.
        customers (CustomerService): Service for customer-related operations.
        geo (GeoService): Service for geographical data operations.
        integration (IntegrationService): Service for integration-related operations.
        jobs (JobService): Service for job/task-related operations.
        objects (ObjectService): Service for object/resource-related operations.
        occasions (OccasionService): Service for occasion/event-related operations.
        orders (OrderService): Service for order-related operations.
        reports (ReportService): Service for reporting operations.
        reservations (ReservationService): Service for reservation-related operations.
        shipping (ShippingService): Service for shipping-related operations.
        misc (MiscService): Service for miscellaneous operations.
    Args:
        creds (Credentials): Credentials for authenticating with the API.
        wsdl_url (str, optional): URL to the WSDL for the SOAP API. Defaults to LegaOnline production endpoint.
        zeep_client (Optional[ZeepClient], optional): Custom Zeep client instance. If None, a new one is created.
        authenticate_on_init (bool, optional): Whether to authenticate immediately upon initialization. Defaults to True.
        tzinfo (Optional[datetime.tzinfo], optional): Timezone info to use. If None, uses default timezone.
    Raises:
        AuthenticationError: If authentication fails during initialization (when authenticate_on_init is True).
    """


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
            from zeep.transports import Transport as ZeepTransport  # local import

            class _PatchedTransport(ZeepTransport):
                """Patches LegaOnline WSDL to declare xmlns:s which the server omits."""
                def load(self, url):
                    content = super().load(url)
                    if b'xmlns:s=' not in content and b's:string' in content:
                        content = content.replace(
                            b'<wsdl:definitions ',
                            b'<wsdl:definitions xmlns:s="http://www.w3.org/2001/XMLSchema" ',
                            1,
                        )
                    return content

            settings = ZeepSettings(strict=False, xml_huge_tree=True)
            zeep_client = ZeepClient(wsdl=wsdl_url, settings=settings, transport=_PatchedTransport())

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
