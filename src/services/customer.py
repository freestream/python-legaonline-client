from __future__ import annotations

import datetime as dt
from typing import Optional

from .base import BaseService
from ..query import FilterSpec, SortSpec


class CustomerService(BaseService):
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
