from __future__ import annotations

from typing import Literal, Optional

from ..types import SoapResponse
from .base import BaseService

AccountSetting = Literal[
    "BookingDayStart",
    "BookingDayEnd",
    "PriceIncVat",
    "PersonnelParticipantListReportId",
    "PersonnelDiplomaReportId",
    "PersonnelEvaluationStatisticsReportId",
    "VismaAdminSettings",
    "FinancialAPIInvoiceDateRows",
]


class FinancialAccountSettingService(BaseService):
    """
    Service class for account setting operations in the Financial API.

    Provides methods for reading and writing account-level configuration settings
    via the LegaOnline Financial SOAP API.

    Attributes:
        __slots__: Empty tuple indicating no additional instance attributes.

    Note:
        This class inherits from BaseService which provides the underlying _call method
        for executing authenticated SOAP operations.
    """

    __slots__ = ()

    def get_account_setting(self, setting: str) -> SoapResponse:
        """
        Retrieve the current value of an account setting.

        Args:
            setting (str): The name of the account setting to retrieve. Valid values are
                defined by the AccountSetting type alias: ``BookingDayStart``,
                ``BookingDayEnd``, ``PriceIncVat``, ``PersonnelParticipantListReportId``,
                ``PersonnelDiplomaReportId``, ``PersonnelEvaluationStatisticsReportId``,
                ``VismaAdminSettings``, ``FinancialAPIInvoiceDateRows``.

        Returns:
            SoapResponse: The response from the SOAP service containing the setting value
                as a string.
        """
        return self._call("GetAccountSetting", setting=setting)

    def set_empty_account_setting(self, setting: str, new_value: str) -> SoapResponse:
        """
        Set an account setting to a new value.

        Args:
            setting (str): The name of the account setting to update. Valid values are
                defined by the AccountSetting type alias: ``BookingDayStart``,
                ``BookingDayEnd``, ``PriceIncVat``, ``PersonnelParticipantListReportId``,
                ``PersonnelDiplomaReportId``, ``PersonnelEvaluationStatisticsReportId``,
                ``VismaAdminSettings``, ``FinancialAPIInvoiceDateRows``.
            new_value (str): The new value to assign to the setting.

        Returns:
            SoapResponse: The response from the SOAP service containing the updated
                setting value as a string.
        """
        return self._call("SetEmptyAccountSetting", setting=setting, newValue=new_value)
