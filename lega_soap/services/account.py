from __future__ import annotations

from typing import Any, Optional

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
        >>> response = account_service.get_account(account_id=12345)
        >>> users = account_service.get_external_account_user(
        ...     filtering=FilterSpec(field="status", value="active")
        ... )
    """
    __slots__ = ()

    def get_account(self, *args: Any, account_id: Optional[int] = None, account_name: Optional[str] = None, legal_name: Optional[str] = None, email: Optional[str] = None, address: Optional[str] = None, zip_str: Optional[str] = None, city: Optional[str] = None, phone: Optional[str] = None, fax: Optional[str] = None, org_nr: Optional[str] = None, homepage: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve account information from the SOAP service.

        Args:
            account_id (Optional[int], optional): The unique identifier for the account. Defaults to None.
            account_name (Optional[str], optional): The name of the account. Defaults to None.
            legal_name (Optional[str], optional): The legal name of the account. Defaults to None.
            email (Optional[str], optional): The email address associated with the account. Defaults to None.
            address (Optional[str], optional): The street address of the account. Defaults to None.
            zip_str (Optional[str], optional): The postal/zip code of the account. Defaults to None.
            city (Optional[str], optional): The city of the account. Defaults to None.
            phone (Optional[str], optional): The phone number of the account. Defaults to None.
            fax (Optional[str], optional): The fax number of the account. Defaults to None.
            org_nr (Optional[str], optional): The organization number of the account. Defaults to None.
            homepage (Optional[str], optional): The homepage URL of the account. Defaults to None.
            *args (Any): Additional positional arguments to pass to the SOAP service call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response from the SOAP service containing account information.
        """
        return self._call("GetAccount", *args, **kwargs, AccountID=account_id, AccountName=account_name, LegalName=legal_name, Email=email, Address=address, Zip=zip_str, City=city, Phone=phone, Fax=fax, OrgNr=org_nr, Homepage=homepage)

    def get_account_info(self, *args: Any, name: Optional[str] = None, email: Optional[str] = None, address_1: Optional[str] = None, zip_str: Optional[str] = None, city: Optional[str] = None, phone: Optional[str] = None, fax: Optional[str] = None, org_nr: Optional[str] = None, homepage: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve account information based on the provided search criteria.

        Args:
            name (Optional[str], optional): Account name to search for. Defaults to None.
            email (Optional[str], optional): Email address to search for. Defaults to None.
            address_1 (Optional[str], optional): Primary address to search for. Defaults to None.
            zip_str (Optional[str], optional): Zip/postal code to search for. Defaults to None.
            city (Optional[str], optional): City to search for. Defaults to None.
            phone (Optional[str], optional): Phone number to search for. Defaults to None.
            fax (Optional[str], optional): Fax number to search for. Defaults to None.
            org_nr (Optional[str], optional): Organization number to search for. Defaults to None.
            homepage (Optional[str], optional): Homepage URL to search for. Defaults to None.
            *args (Any): Additional positional arguments to pass to the SOAP service call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: Response object containing account information matching the search criteria.
        """
        return self._call("GetAccountInfo", *args, **kwargs, Name=name, Email=email, Address1=address_1, Zip=zip_str, City=city, Phone=phone, Fax=fax, OrgNR=org_nr, Homepage=homepage)

    def get_account_info_xml(self, *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Retrieve account information in XML format.

        This method calls the SOAP service's GetAccountInfoXml operation to fetch
        account details and returns the response in XML format.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response containing account information in XML format.

        Raises:
            Any exceptions raised by the underlying SOAP service call.
        """
        return self._call("GetAccountInfoXml", *args, **kwargs)

    def get_account_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve account data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the account results.
                If provided, it will be converted to XML format and included in the request.
                Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the account results.
                If provided, it will be converted to XML format and included in the request.
                Defaults to None.
            *args (Any): Additional positional arguments to pass to the SOAP service call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The SOAP response containing account data in XML format.

        Raises:
            Any exceptions raised by the underlying _call method or the to_xml() conversions.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetAccountXml", *args, **kwargs, sort=sort_xml, filter=filter_xml)

    def get_external_account_user(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve external account user information from the SOAP service.

        This method calls the GetExternalAccountUser SOAP operation with optional
        sorting and filtering parameters.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP service call.
            sorting (Optional[SortSpec]): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

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
        return self._call("GetExternalAccountUser", *args, **kwargs, sort=sort_xml, filter=filter_xml)

    def get_external_account_user_xml(self, *, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve external account user data in XML format.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the results.
                If None, no sorting is applied.
            filtering (Optional[FilterSpec]): Specification for filtering the results.
                If None, no filtering is applied.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The SOAP response containing external account user data in XML format.
        """
        sort_xml: str = sorting.to_xml() if sorting else ""
        filter_xml: str = filtering.to_xml() if filtering else ""
        return self._call("GetExternalAccountUserXml", sort=sort_xml, filter=filter_xml, **kwargs)

    def set_external_account_user_password(self, user_id: Optional[int], new_password: Optional[str], *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Set the password for an external account user.

        Args:
            user_id (Optional[int]): The ID of the user whose password should be changed.
            new_password (Optional[str]): The new password to set for the user.
            *args (Any): Additional positional arguments to pass to the SOAP service call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The SOAP response object containing the result of the password change operation.
        """
        return self._call("SetExternalAccountUserPassword", *args, **kwargs, userID=user_id, newPassword=new_password)

    def set_external_account_user_password_xml(self, user_id: Optional[int], new_password: Optional[str], *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Sets a new password for an external account user.

        Args:
            user_id (Optional[int]): The unique identifier of the external account user.
            new_password (Optional[str]): The new password to set for the user.
            *args (Any): Additional positional arguments to pass to the SOAP service call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the password change operation.
        """
        return self._call("SetExternalAccountUserPasswordXml", *args, **kwargs, userID=user_id, newPassword=new_password)

    def update_external_account_user(self, user_id: Optional[int], full_name: Optional[str], user_name: Optional[str], email: Optional[str], address: Optional[str], zip_str: Optional[str], city: Optional[str], phone: Optional[str], mobile: Optional[str], *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Update an external account user's information.

        Args:
            user_id (Optional[int]): The unique identifier of the user to update.
            full_name (Optional[str]): The full name of the user.
            user_name (Optional[str]): The username for the account.
            email (Optional[str]): The email address of the user.
            address (Optional[str]): The street address of the user.
            zip_str (Optional[str]): The postal/ZIP code.
            city (Optional[str]): The city of residence.
            phone (Optional[str]): The phone number of the user.
            mobile (Optional[str]): The mobile phone number of the user.
            *args (Any): Additional positional arguments to pass to the SOAP service call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response from the SOAP service call containing the result of the update operation.
        """
        return self._call("UpdateExternalAccountUser", *args, **kwargs, user_id=user_id, FullName=full_name, UserName=user_name, Email=email, Address=address, Zip=zip_str, City=city, Phone=phone, Mobile=mobile)

    def update_external_account_user_xml(self, users: Optional[str], *args: Any, **kwargs: Any) -> SoapResponse:
        """
        Update external account user information using XML format.

        This method calls the SOAP service's UpdateExternalAccountUserXml operation to update
        external account user data.

        Args:
            users (Optional[str]): XML string containing user information to be updated.
                If None, the operation may use default behavior as defined by the service.
            *args (Any): Additional positional arguments to pass to the SOAP service call.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the result
                of the update operation.

        Raises:
            May raise exceptions from the underlying SOAP service call, such as
            connection errors or service-specific exceptions.
        """
        return self._call("UpdateExternalAccountUserXml", *args, **kwargs, users=users)
