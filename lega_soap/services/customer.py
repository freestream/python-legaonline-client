from __future__ import annotations

import datetime as dt
from typing import Optional

from .base import BaseService
from ..query import FilterSpec, SortSpec


class CustomerService(BaseService):
    """
    Service class for managing customer-related operations.

    This class provides methods to interact with customer data through a ZEEP SOAP service.
    It extends BaseService and handles customer retrieval with optional sorting, filtering,
    and attribute inclusion.

    Args:
        zeep_service: The ZEEP service client for making SOAP requests.
        auth_manager: Manager for handling authentication and authorization.
        tzinfo (dt.tzinfo): Timezone information for datetime operations.

    Methods:
        get_customer: Retrieves customer data with optional sorting, filtering, and attributes.
    """
    def __init__(self, zeep_service, auth_manager, tzinfo: dt.tzinfo):
        super().__init__(zeep_service, auth_manager, tzinfo)

    def get_customer(
        self,
        sorting: Optional[SortSpec] = None,
        filtering: Optional[FilterSpec] = None,
        include_attributes: bool = False,
    ):
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""

        return self._call("GetCustomer", sort_xml, filter_xml, include_attributes)
