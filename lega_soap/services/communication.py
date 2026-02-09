from __future__ import annotations

from typing import Any, Optional

from ..query import FilterSpec, SortSpec, StrListSpec
from ..types import SoapResponse
from .base import BaseService


class CommunicationService(BaseService):
    """
    Service class for handling communication-related SOAP operations.

    This class provides methods for managing document communications and email operations
    within the LegaOnline system. It extends BaseService to provide SOAP-based communication
    functionality including document retrieval, confirmation emails, and password emails.

    The service supports operations such as:
    - Retrieving lists of sent documents with optional sorting and filtering
    - Sending confirmation emails for reservations with various recipient configurations
    - Sending user passwords via email

    All methods return SoapResponse objects containing the results of the SOAP operations.

    Attributes:
        Inherits all attributes from BaseService. Uses __slots__ = () to prevent
        additional attribute assignment.

        >>> from lega_soap.services import CommunicationService
        >>> service = CommunicationService(client)
        >>> response = service.get_document_sent_list()
        >>> # Send confirmation email
        >>> to_list = StrListSpec(['user@example.com'])
        >>> service.send_confirmation_email(
        ...     reservation_id=123,
        ...     from_address='noreply@example.com',
        ...     to_addresses=to_list
        ... )
    """
    __slots__ = ()

    def get_document_sent_list(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve a list of sent documents from the SOAP service.

        This method calls the GetDocumentSentList SOAP operation with optional sorting
        and filtering parameters.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the results. If provided,
                it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results. If provided,
                it will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the underlying SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the list of sent documents.

        Example:
            >>> sort_spec = SortSpec(field="date", order="desc")
            >>> filter_spec = FilterSpec(field="status", value="completed")
            >>> response = service.get_document_sent_list(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetDocumentSentList", sort=sort_xml, filter=filter_xml, **kwargs)

    def get_document_sent_list_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve a list of sent documents in XML format with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec]): Specification for sorting the document list.
                If provided, will be converted to XML format for the SOAP request.
            filtering (Optional[FilterSpec]): Specification for filtering the document list.
                If provided, will be converted to XML format for the SOAP request.
            **kwargs (Any): Additional keyword arguments to pass to the underlying SOAP call.

        Returns:
            SoapResponse: The response from the GetDocumentSentListXml SOAP operation,
                containing the list of sent documents in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetDocumentSentListXml", sort=sort_xml, filter=filter_xml, **kwargs)

    def send_confirmation_email(self, reservation_id: Optional[int] = None, from_address: Optional[str] = None, to_addresses: Optional[StrListSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Send a confirmation email for a reservation.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation to send confirmation for. Defaults to None.
            from_address (Optional[str], optional): The sender's email address. Defaults to None.
            to_addresses (Optional[StrListSpec], optional): List of recipient email addresses. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response object containing the result of the email sending operation.
        """
        to_addresses_xml = to_addresses.to_xml() if to_addresses else ""
        return self._call("SendConfirmationEmail", reservationID=reservation_id, toAddresses=to_addresses_xml, **{"from": from_address, **kwargs})

    def send_confirmation_email_and_copy(self, reservation_id: Optional[int] = None, from_address: Optional[str] = None, to_addresses: Optional[StrListSpec] = None, cc_address: Optional[str] = None, bcc_address: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Send a confirmation email with optional CC and BCC recipients.

        This method sends a confirmation email for a reservation and allows specifying
        multiple recipients along with CC and BCC addresses.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation for which
                to send the confirmation email. Defaults to None.
            from_address (Optional[str], optional): The sender's email address. Defaults to None.
            to_addresses (Optional[StrListSpec], optional): A StrListSpec object containing
                the list of recipient email addresses. Defaults to None.
            cc_address (Optional[str], optional): The CC (carbon copy) email address. Defaults to None.
            bcc_address (Optional[str], optional): The BCC (blind carbon copy) email address.
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP service call.

        Returns:
            SoapResponse: The response from the SOAP service call containing the result
                of the email send operation.
        """
        to_addresses_xml = to_addresses.to_xml() if to_addresses else ""
        return self._call("SendConfirmationEmailAndCopy", reservationID=reservation_id, toAddresses=to_addresses_xml, cc=cc_address, bcc=bcc_address, **{"from": from_address, **kwargs})

    def send_confirmation_email_doc(self, reservation_id: Optional[int] = None, from_address: Optional[str] = None, to_addresses: Optional[StrListSpec] = None, confirmation_email_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Send a confirmation email document for a reservation.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation to send confirmation for. Defaults to None.
            from_address (Optional[str], optional): The email address to send from. Defaults to None.
            to_addresses (Optional[StrListSpec], optional): The recipient email addresses. Defaults to None.
            confirmation_email_id (Optional[int], optional): The ID of the confirmation email template. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The SOAP response object containing the result of the email send operation.
        """
        to_addresses_xml = to_addresses.to_xml() if to_addresses else ""
        return self._call("SendConfirmationEmailDoc", reservationID=reservation_id, toAddresses=to_addresses_xml, confirmationEmailID=confirmation_email_id, **{"from": from_address, **kwargs})

    def send_confirmation_email_doc_v2(self, reservation_id: Optional[int] = None, from_address: Optional[str] = None, to_addresses: Optional[StrListSpec] = None, document_id: Optional[int] = None, **kwargs: Any) -> SoapResponse:
        """
        Send a confirmation email with a document attachment.

        This method sends a confirmation email for a reservation with an attached document
        using the SendConfirmationEmailDocV2 SOAP operation.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation to send
                confirmation for. Defaults to None.
            from_address (Optional[str], optional): The sender's email address. Defaults to None.
            to_addresses (Optional[StrListSpec], optional): The recipient email addresses.
                Must be a StrListSpec object that can be converted to XML. Defaults to None.
            document_id (Optional[int], optional): The ID of the document to attach to the email.
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the
                email send operation.

        Note:
            The 'from_address' parameter is mapped to the 'from' keyword in the SOAP call
            to avoid conflicts with Python's reserved 'from' keyword.
        """
        to_addresses_xml = to_addresses.to_xml() if to_addresses else ""
        return self._call("SendConfirmationEmailDocV2", reservationID=reservation_id, toAddresses=to_addresses_xml, documentID=document_id, **{"from": from_address, **kwargs})

    def send_user_password(self, username: Optional[str] = None, from_email: Optional[str] = None, mail_subject: Optional[str] = None, mail_text: Optional[str] = None, password_text: Optional[str] = None, **kwargs: Any) -> SoapResponse:
        """
        Send a user password via email through the SOAP service.

        This method sends a password to a user via email using the SendUserPassword SOAP operation.
        All email content parameters are optional and can be customized.

        Args:
            username (Optional[str], optional): The username of the user to send the password to.
                Defaults to None.
            from_email (Optional[str], optional): The sender's email address for the password email.
                Defaults to None.
            mail_subject (Optional[str], optional): The subject line of the password email.
                Defaults to None.
            mail_text (Optional[str], optional): The body text of the password email.
                Defaults to None.
            password_text (Optional[str], optional): Additional text to include with the password.
                Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("SendUserPassword", username=username, fromEmail=from_email, mailSubject=mail_subject, mailText=mail_text, passwordText=password_text, **kwargs)
