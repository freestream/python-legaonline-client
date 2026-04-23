from __future__ import annotations

import datetime as dt
from typing import Optional, TYPE_CHECKING, Any

from .auth import AuthManager, Credentials
from .timezone import get_default_tzinfo
from .services.auth import AuthService
from .services.financial_account_setting import FinancialAccountSettingService
from .services.financial_customer import FinancialCustomerService
from .services.financial_invoice import FinancialInvoiceService
from .services.financial_payment import FinancialPaymentService

if TYPE_CHECKING:  # pragma: no cover
    from zeep.client import Client as ZeepClient


class FinancialClient:
    """
    Client for the LegaOnline Financial SOAP API (financialapi.asmx).

    Provides access to invoice, payment, customer, and account setting operations
    via the Financial API endpoint. Authentication is managed automatically.

    Attributes:
        zeep_client: The underlying Zeep SOAP client instance.
        auth: Manages authentication and token lifecycle.
        tzinfo: Timezone information used for date/time fields.
        auth_service: Service for authentication operations (no auth token required).
        account_settings: Service for account setting operations.
        customers: Service for customer operations (Financial API subset + transaction data).
        invoices: Service for invoice operations (V1–V8, payments, invalidation).
        payments: Service for payment and balance operations.

    Args:
        creds: Credentials for authenticating with the API.
        wsdl_url: URL to the Financial API WSDL. Defaults to the LegaOnline production endpoint.
        zeep_client: Custom Zeep client instance. If None, a new one is created.
        authenticate_on_init: Whether to authenticate immediately upon initialization.
        tzinfo: Timezone info to use. If None, uses the system default.
    """

    __slots__ = (
        "zeep_client",
        "auth",
        "tzinfo",
        "auth_service",
        "account_settings",
        "customers",
        "invoices",
        "payments",
    )

    def __init__(
        self,
        *,
        creds: Credentials,
        wsdl_url: str = "https://api.legaonline.se/financialapi.asmx?wsdl",
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

        self.auth: AuthManager = AuthManager(self.zeep_client.service, creds)
        if authenticate_on_init:
            self.auth.authenticate()

        self.account_settings: FinancialAccountSettingService = FinancialAccountSettingService(
            self.zeep_client.service, self.auth, self.tzinfo
        )
        self.customers: FinancialCustomerService = FinancialCustomerService(
            self.zeep_client.service, self.auth, self.tzinfo
        )
        self.invoices: FinancialInvoiceService = FinancialInvoiceService(
            self.zeep_client.service, self.auth, self.tzinfo
        )
        self.payments: FinancialPaymentService = FinancialPaymentService(
            self.zeep_client.service, self.auth, self.tzinfo
        )

        self.auth_service: AuthService = AuthService(self.zeep_client.service, self.tzinfo)
