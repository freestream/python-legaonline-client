from __future__ import annotations

from typing import Optional

from ..query import FilterSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService

class AccountService(BaseService):
    """
    Service class for managing account-related operations via SOAP.

    This class provides methods to interact with account data through a SOAP service,
    including retrieving, updating, and managing external account users. It supports
    various formats (standard and XML) for data exchange and provides flexible
    filtering and sorting capabilities.

    The service handles operations such as:
    - Retrieving account information by various search criteria
    - Fetching account data in XML format with optional sorting and filtering
    - Managing external account users and their credentials
    - Updating user information through both standard and XML-based methods

    All methods inherit authentication and timezone handling from BaseService.

    Attributes:
        Inherits all attributes from BaseService through initialization.

        >>> account_service = AccountService(zeep_service, auth_manager, timezone_info)
        >>> users = account_service.get_external_account_user(
        ...     filtering=FilterSpec(field="status", value="active")
        ... )
    """
    __slots__ = ()

    def get_account(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve account information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the account results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the account results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing account information.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetAccount", sort=sort_xml, filter=filter_xml)

    def get_account_info(self) -> SoapResponse:
        """
        Retrieve account information from the SOAP service.

        Returns:
            SoapResponse: Response object containing account information.
        """
        return self._call("GetAccountInfo")

    def get_account_info_xml(self) -> SoapResponse:
        """
        Retrieve account information in XML format.

        Returns:
            SoapResponse: The SOAP response containing account information in XML format.
        """
        return self._call("GetAccountInfoXml")

    def get_account_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve account data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the account results.
                If provided, it will be converted to XML format and included in the request.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the account results.
                If provided, it will be converted to XML format and included in the request.
                Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing account data in XML format.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetAccountXml", sort=sort_xml, filter=filter_xml)

    def get_external_account_user(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve external account user information from the SOAP service.

        This method calls the GetExternalAccountUser SOAP operation with optional
        sorting and filtering parameters.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                external account user information.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = service.get_external_account_user(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetExternalAccountUser", sort=sort_xml, filter=filter_xml)

    def get_external_account_user_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve external account user data in XML format.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If None, no sorting is applied. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If None, no filtering is applied. Defaults to None.

        Returns:
            SoapResponse: The SOAP response containing external account user data in XML format.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetExternalAccountUserXml", sort=sort_xml, filter=filter_xml)

    def set_external_account_user_password(self, user_id: Optional[int] = None, old_password: Optional[str] = None, new_password: Optional[str] = None) -> SoapResponse:
        """
        Set the password for an external account user.

        Args:
            user_id (Optional[int], optional): The ID of the user whose password should be changed. Defaults to None.
            old_password (Optional[str], optional): The current password of the user. Defaults to None.
            new_password (Optional[str], optional): The new password to set for the user. Defaults to None.

        Returns:
            SoapResponse: The SOAP response object containing the result of the password change operation.
        """
        return self._call("SetExternalAccountUserPassword", userID=user_id, oldPassword=old_password, newPassword=new_password)

    def set_external_account_user_password_xml(self, user_id: Optional[int] = None, old_password: Optional[str] = None, new_password: Optional[str] = None) -> SoapResponse:
        """
        Sets a new password for an external account user.

        Args:
            user_id (Optional[int], optional): The unique identifier of the external account user. Defaults to None.
            old_password (Optional[str], optional): The current password of the user. Defaults to None.
            new_password (Optional[str], optional): The new password to set for the user. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the password change operation.
        """
        return self._call("SetExternalAccountUserPasswordXml", userID=user_id, oldPassword=old_password, newPassword=new_password)

    def update_external_account_user(self, users: Optional[str] = None) -> SoapResponse:
        """
        Update an external account user's information.

        Args:
            users (Optional[str], optional): XML string containing user information to be updated. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service call containing the result of the update operation.
        """
        return self._call("UpdateExternalAccountUser", users=users)

    def update_external_account_user_xml(self, users: Optional[str] = None) -> SoapResponse:
        """
        Update external account user information using XML format.

        This method calls the SOAP service's UpdateExternalAccountUserXml operation to update
        external account user data.

        Args:
            users (Optional[str], optional): XML string containing user information to be updated.
                If None, the operation may use default behavior as defined by the service. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                of the update operation.
        """
        return self._call("UpdateExternalAccountUserXml", users=users)
