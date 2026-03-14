from __future__ import annotations

import datetime as dt
from typing import Optional

from ..query import FilterSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService


class JobService(BaseService):
    """
    Service class for managing job-related operations in the LegaOnline SOAP API.

    This service provides methods to retrieve, create, update job information and manage
    job-reservation relationships through SOAP operations.

    Attributes:
        __slots__ (tuple): Empty tuple to prevent dynamic attribute creation for memory optimization.

    Methods:
        get_job: Retrieves job information with optional sorting and filtering.
        set_job: Creates or updates job specifications in the system.
        add_reservation_to_job: Associates a reservation with a specific job.

        >>> job_service = JobService(client)
        >>> job_service.set_job(job_id=1, customer_id=2, status=1)
        >>> job_service.add_reservation_to_job(reservation_id=456, job_id=123)
    """
    __slots__ = ()

    def get_job(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve job information from the SOAP service.

        This method calls the 'GetJob' SOAP operation with optional sorting and filtering parameters.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing job information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetJob", sort=sort_xml, filter=filter_xml)

    def set_job(
        self,
        job_id: Optional[int] = None,
        customer_id: Optional[int] = None,
        description: Optional[str] = None,
        job_nr_description: Optional[str] = None,
        status: Optional[int] = None,
        start_date: Optional[dt.datetime] = None,
        end_date: Optional[dt.datetime] = None,
        notes: Optional[str] = None,
        job_nr: Optional[str] = None,
        customer_reference: Optional[str] = None,
        po_number: Optional[str] = None,
        price_code_group_id: Optional[int] = None,
    ) -> SoapResponse:
        """
        Set job specifications in the LegaOnline system.

        This method calls the 'SetJob' SOAP operation to create or update job specifications.

        Args:
            job_id (Optional[int]): Job ID. Required in WSDL.
            customer_id (Optional[int]): Customer ID. Required in WSDL.
            description (Optional[str]): Job description.
            job_nr_description (Optional[str]): Job number description.
            status (Optional[int]): Job status. Required in WSDL.
            start_date (Optional[dt.datetime]): Start date. Required in WSDL.
            end_date (Optional[dt.datetime]): End date. Required in WSDL.
            notes (Optional[str]): Notes.
            job_nr (Optional[str]): Job number.
            customer_reference (Optional[str]): Customer reference.
            po_number (Optional[str]): PO number.
            price_code_group_id (Optional[int]): Price code group ID. Required in WSDL.

        Returns:
            SoapResponse: Response object from the SOAP service containing the result
                of the SetJob operation.
        """
        record = {k: v for k, v in {
            "JobID": job_id,
            "CustomerID": customer_id,
            "Description": description,
            "JobNr_Description": job_nr_description,
            "Status": status,
            "StartDate": start_date,
            "EndDate": end_date,
            "Notes": notes,
            "JobNr": job_nr,
            "CustomerReference": customer_reference,
            "PO_Number": po_number,
            "PriceCodeGroupID": price_code_group_id,
        }.items() if v is not None}
        return self._call("SetJob", jobs=[record])

    def add_reservation_to_job(self, reservation_id: Optional[int] = None, job_id: Optional[int] = None) -> SoapResponse:
        """
        Add a reservation to a job in the LegaOnline system.

        Args:
            reservation_id (Optional[int], optional): The ID of the reservation to add. Defaults to None.
            job_id (Optional[int], optional): The ID of the job to add the reservation to. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the result of the operation.
        """
        return self._call("AddReservationToJob", reservationID=reservation_id, jobID=job_id)
