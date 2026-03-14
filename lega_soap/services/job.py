from __future__ import annotations

from typing import Any, Optional

from ..query import FilterSpec, SortSpec, JobSpec
from ..types import SoapResponse
from .base import BaseService


class JobService(BaseService):
    """
    Service class for managing job-related operations in the LegaOnline SOAP API.

    This service provides methods to retrieve, create, update job information and manage
    job-reservation relationships through SOAP operations.

    Inherits from:
        BaseService: Base class providing core SOAP service functionality.

    Attributes:
        __slots__ (tuple): Empty tuple to prevent dynamic attribute creation for memory optimization.

    Methods:
        get_job: Retrieves job information with optional sorting and filtering.
        set_job: Creates or updates job specifications in the system.
        add_reservation_to_job: Associates a reservation with a specific job.

        >>> job_service = JobService(client)
        >>> response = job_service.get_job(job_id=123)
        >>> job_service.set_job(jobs=job_spec)
        >>> job_service.add_reservation_to_job(reservation_id=456, job_id=123)
    """
    __slots__ = ()

    def get_job(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve job information from the SOAP service.

        This method calls the 'GetJob' SOAP operation with optional sorting and filtering parameters.

        Args:
            *args (Any): Variable positional arguments to be passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            **kwargs (Any): Variable keyword arguments to be passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing job information.

        Example:
            >>> job_service.get_job(job_id=123, sorting=my_sort_spec, filtering=my_filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetJob", *args, sort=sort_xml, filter=filter_xml, **kwargs)

    def set_job(self, *args: Any, jobs: Optional[JobSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Set job specifications in the LegaOnline system.

        This method calls the 'SetJob' SOAP operation to create or update job specifications.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            jobs: Optional job specification object containing the job details to set.
                Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: Response object from the SOAP service containing the result
                of the SetJob operation.

        Raises:
            May raise exceptions from the underlying SOAP call depending on the
            implementation of _call method.
        """
        return self._call("SetJob", *args, jobs=jobs, **kwargs)

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
