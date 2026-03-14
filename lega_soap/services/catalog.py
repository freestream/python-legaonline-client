from __future__ import annotations

from typing import Optional

from ..query import FilterSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService

class CatalogService(BaseService):
    """
    Service class for handling catalog-related SOAP operations.

    This class provides methods to interact with catalog entities such as attributes,
    categories, questions, and their XML representations. It supports operations for
    different object types including jobs, companies, and general objects.

    Methods:
        get_attribute: Retrieve attribute information.
        get_attribute_xml: Retrieve attribute information in XML format.
        get_category: Retrieve category information.
        get_category_v2: Retrieve category information (version 2).
        get_category_v2_xml: Retrieve category information in XML format (version 2).
        get_category_v3: Retrieve category information (version 3).
        get_category_xml: Retrieve category information in XML format.
        get_company_attribute: Retrieve company-specific attribute information.
        get_company_attribute_xml: Retrieve company-specific attribute in XML format.
        get_job_attribute: Retrieve job-specific attribute information.
        get_job_attribute_xml: Retrieve job-specific attribute in XML format.
        get_object_attribute: Retrieve object-specific attribute information.
        get_object_attribute_xml: Retrieve object-specific attribute in XML format.
        get_object_category_question: Retrieve questions for object categories.
        get_object_category_question_xml: Retrieve questions for object categories in XML format.
        get_question: Retrieve question information.
        get_question_xml: Retrieve question information in XML format.
        set_job_attributes: Set attributes for a job.
        set_job_attributes_xml: Set attributes for a job using XML format.

    All methods return SoapResponse objects containing the result of the SOAP operation.
    """
    __slots__ = ()

    def get_attribute(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve attribute information from the catalog service.

        This method calls the SOAP 'GetAttribute' operation with optional sorting and filtering parameters.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing attribute data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetAttribute", sort=sort_xml, filter=filter_xml)

    def get_attribute_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves attribute data in XML format from the catalog service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing the attribute XML data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetAttributeXml", sort=sort_xml, filter=filter_xml)

    def get_category(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve category information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification object that defines
                how results should be sorted. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that
                defines which results should be included. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing category data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategory", sort=sort_xml, filter=filter_xml)

    def get_category_v2(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve category information using the V2 API endpoint with optional sorting and filtering.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the category data from the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategoryV2", sort=sort_xml, filter=filter_xml)

    def get_category_v2_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve category information in XML format using the GetCategoryV2Xml SOAP method.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification object that defines
                how the category results should be sorted. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that
                defines criteria for filtering category results. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing category
                information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategoryV2Xml", sort=sort_xml, filter=filter_xml)

    def get_category_v3(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve category information using the GetCategoryV3 SOAP operation.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the category
                information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategoryV3", sort=sort_xml, filter=filter_xml)

    def get_category_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve category data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification object that defines how to sort
                the category results. Will be converted to XML if provided. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that defines how to
                filter the category results. Will be converted to XML if provided. Defaults to None.

        Returns:
            SoapResponse: The response object containing the category XML data returned by the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategoryXml", sort=sort_xml, filter=filter_xml)

    def get_company_attribute(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves company attribute information from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML and included in the SOAP request.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML and included in the SOAP request.
                Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the
                company attribute data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCompanyAttribute", sort=sort_xml, filter=filter_xml)

    def get_company_attribute_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve company attributes in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing company attributes
                in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCompanyAttributeXml", sort=sort_xml, filter=filter_xml)

    def get_job_attribute(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve job attributes from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                     If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                       If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                          the requested job attributes.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetJobAttribute", sort=sort_xml, filter=filter_xml)

    def get_job_attribute_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve job attribute data in XML format from the catalog service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                     If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                       If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object containing the job attribute data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetJobAttributeXml", sort=sort_xml, filter=filter_xml)

    def get_object_attribute(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve object attributes from the catalog service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the
                requested object attributes.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectAttribute", sort=sort_xml, filter=filter_xml)

    def get_object_attribute_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve object attributes in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing object attributes
                in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectAttributeXml", sort=sort_xml, filter=filter_xml)

    def get_object_category_question(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve object category questions from the catalog service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service containing the object
                category questions data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectCategoryQuestion", sort=sort_xml, filter=filter_xml)

    def get_object_category_question_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieves object category question data in XML format from the SOAP service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing object category
                          question data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectCategoryQuestionXml", sort=sort_xml, filter=filter_xml)

    def get_question(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve questions from the catalog service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response from the GetQuestion SOAP service call.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetQuestion", sort=sort_xml, filter=filter_xml)

    def get_question_xml(self, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None) -> SoapResponse:
        """
        Retrieve question data in XML format from the catalog service.

        Args:
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.

        Returns:
            SoapResponse: The response from the SOAP service containing question data in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetQuestionXml", sort=sort_xml, filter=filter_xml)

    def set_job_attributes(self, job_attribute: Optional[str] = None) -> SoapResponse:
        """
        Set job attributes.

        Args:
            job_attribute (Optional[str], optional): XML string containing the job attribute to set. Defaults to None.

        Returns:
            SoapResponse: The response object from the SOAP service call.
        """
        return self._call("SetJobAttributes", jobAttribute=job_attribute)

    def set_job_attributes_xml(self, job_attribute: Optional[str] = None) -> SoapResponse:
        """
        Set job attributes, returning XML response.

        Args:
            job_attribute (Optional[str], optional): XML string containing the job attribute to set. Defaults to None.

        Returns:
            SoapResponse: The response from the SetJobAttributesXml SOAP operation.
        """
        return self._call("SetJobAttributesXml", jobAttribute=job_attribute)
