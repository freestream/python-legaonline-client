from __future__ import annotations

from typing import Optional

from ..query import FilterSpec, SortSpec, ReportParameterSpec, XmlArray
from ..types import SoapResponse
from .base import BaseService


class ReportService(BaseService):
    """
    Service class for managing reports via SOAP API.

    This class provides methods for report-related operations including retrieval of printer profiles,
    report documents, and report URLs with sorting and filtering capabilities.
    It inherits from BaseService and implements SOAP service calls for report management functionality.

    The ReportService handles:
    - Retrieval of printer profiles and report documents with sorting and filtering capabilities
    - Retrieval of report URLs with parameterization options

    All methods return SoapResponse objects containing the results from the SOAP service calls.
    """
    __slots__ = ()

    def get_printer_profile(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve printer profile information from the SOAP service.

        This method calls the GetPrinterProfile SOAP operation with optional sorting
        and filtering parameters.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing printer profile data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetPrinterProfile", sort=sort_xml, filter=filter_xml)

    def get_printer_profile_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve printer profile information in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing printer profile data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetPrinterProfileXml", sort=sort_xml, filter=filter_xml)

    def get_report_doc(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve report document information from the SOAP service.

        This method calls the GetReportDoc SOAP operation with optional sorting
        and filtering parameters.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing report document data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReportDoc", sort=sort_xml, filter=filter_xml)

    def get_report_doc_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve report document information in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing report document data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetReportDocXml", sort=sort_xml, filter=filter_xml)

    def get_report_url(self, report_id: Optional[int] = None, report_name: Optional[str] = None, show_as_html: Optional[bool] = None, parameters: Optional[XmlArray[ReportParameterSpec]] = None) -> SoapResponse:
        """
        Retrieve report URL information from the SOAP service.

        Args:
            report_id (Optional[int], optional): The ID of the report. Defaults to None.
            report_name (Optional[str], optional): The name of the report. Defaults to None.
            show_as_html (Optional[bool], optional): Whether to show the report as HTML. Defaults to None.
            parameters (Optional[XmlArray[ReportParameterSpec]], optional): Parameters for the report. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing report URL data.
        """
        show_as_html_str = "true" if show_as_html else "false" if show_as_html is not None else None
        parameters_xml = parameters.to_xml() if parameters else ""
        return self._call("GetReportUrl", reportID=report_id, reportName=report_name, showAsHtml=show_as_html_str, parameters=parameters_xml)

    def get_report_url_xml(self, report_id: Optional[int] = None, report_name: Optional[str] = None, show_as_html: Optional[bool] = None, parameters: Optional[XmlArray[ReportParameterSpec]] = None) -> SoapResponse:
        """
        Retrieve report URL information in XML format from the SOAP service.

        Args:
            report_id (Optional[int], optional): The ID of the report. Defaults to None.
            report_name (Optional[str], optional): The name of the report. Defaults to None.
            show_as_html (Optional[bool], optional): Whether to show the report as HTML. Defaults to None.
            parameters (Optional[XmlArray[ReportParameterSpec]], optional): Parameters for the report. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing report URL data in XML format.
        """
        show_as_html_str = "true" if show_as_html else "false" if show_as_html is not None else None
        parameters_xml = parameters.to_xml() if parameters else ""
        return self._call("GetReportUrlXml", reportID=report_id, reportName=report_name, showAsHtml=show_as_html_str, parameters=parameters_xml)
