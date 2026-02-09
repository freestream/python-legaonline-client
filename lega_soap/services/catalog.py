from __future__ import annotations

from typing import Any, Optional

from ..query import FilterSpec, SortSpec
from ..types import SoapResponse
from .base import BaseService

class CatalogService(BaseService):
    """
    Service class for handling catalog-related SOAP operations.

    This class provides methods to interact with catalog entities such as attributes,
    categories, questions, and their XML representations. It supports operations for
    different object types including jobs, companies, and general objects.

    Attributes:
        Inherits all attributes from BaseService.

    Args:
        zeep_service (Any): The Zeep SOAP service client instance.
        auth_manager (Any): Authentication manager for handling service credentials.
        tzinfo (dt.tzinfo): Timezone information for datetime operations.

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

    def get_attribute(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve attribute information from the catalog service.

        This method calls the SOAP 'GetAttribute' operation with optional sorting and filtering parameters.

        Args:
            *args (Any): Variable length argument list passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing attribute data.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="active", value=True)
            >>> response = catalog.get_attribute(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetAttribute", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_attribute_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves attribute data in XML format from the catalog service.

        This method calls the GetAttributeXml SOAP operation with optional sorting and filtering specifications.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing the attribute XML data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetAttributeXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_category(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve category information from the SOAP service.

        This method calls the 'GetCategory' SOAP operation with optional sorting and filtering
        parameters. It converts SortSpec and FilterSpec objects to their XML representations
        before making the SOAP call.

        Args:
            *args (Any): Variable length argument list passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification object that defines
                how results should be sorted. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that
                defines which results should be included. Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing category data.

        Example:
            >>> service = CatalogService()
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="active", value=True)
            >>> response = service.get_category(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategory", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_category_v2(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve category information using the V2 API endpoint with optional sorting and filtering.

        Args:
            *args (Any): Variable length argument list to be passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, will be converted to XML format. Defaults to None.
            **kwargs (Any): Arbitrary keyword arguments to be passed to the SOAP call.

        Returns:
            SoapResponse: The response object containing the category data from the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategoryV2", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_category_v2_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve category information in XML format using the GetCategoryV2Xml SOAP method.

        This method calls the GetCategoryV2Xml SOAP service with optional sorting and filtering
        specifications. The sorting and filtering parameters are converted to XML format before
        being passed to the SOAP service.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification object that defines
                how the category results should be sorted. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that
                defines criteria for filtering category results. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing category
                information in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategoryV2Xml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_category_v3(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve category information using the GetCategoryV3 SOAP operation.

        This method calls the GetCategoryV3 SOAP endpoint with optional sorting and filtering
        specifications. The sorting and filtering parameters are converted to XML format before
        being passed to the SOAP service.

        Args:
            *args: Variable length argument list to be passed to the SOAP call.
            sorting: Optional specification for sorting the results. If provided, will be
                converted to XML format using its to_xml() method.
            filtering: Optional specification for filtering the results. If provided, will be
                converted to XML format using its to_xml() method.
            **kwargs: Arbitrary keyword arguments to be passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the category
                information.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategoryV3", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_category_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve category data in XML format from the SOAP service.

        This method calls the 'GetCategoryXml' SOAP operation with optional sorting and filtering parameters.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification object that defines how to sort
                the category results. Will be converted to XML if provided. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification object that defines how to
                filter the category results. Will be converted to XML if provided. Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object containing the category XML data returned by the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCategoryXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_company_attribute(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves company attribute information from the SOAP service.

        This method calls the GetCompanyAttribute SOAP operation with optional sorting
        and filtering parameters.

        Args:
            *args: Variable length argument list passed to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, will be converted to XML and included in the SOAP request.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, will be converted to XML and included in the SOAP request.
                Defaults to None.
            **kwargs: Arbitrary keyword arguments passed to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the
                company attribute data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCompanyAttribute", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_company_attribute_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve company attributes in XML format from the SOAP service.

        This method calls the GetCompanyAttributeXml SOAP operation with optional sorting
        and filtering parameters.

        Args:
            *args (Any): Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification for the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs (Any): Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing company attributes
                in XML format.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetCompanyAttributeXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_job_attribute(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve job attributes from the SOAP service.

        This method calls the 'GetJobAttribute' SOAP operation with optional sorting
        and filtering specifications.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting: Optional SortSpec object to specify sorting criteria.
                     If provided, it will be converted to XML format.
            filtering: Optional FilterSpec object to specify filtering criteria.
                       If provided, it will be converted to XML format.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing
                          the requested job attributes.

        Example:
            >>> catalog = Catalog()
            >>> response = catalog.get_job_attribute(
            ...     sorting=SortSpec(field="name", order="asc"),
            ...     filtering=FilterSpec(field="status", value="active")
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetJobAttribute", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_job_attribute_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve job attribute data in XML format from the catalog service.

        This method calls the GetJobAttributeXml SOAP operation with optional sorting
        and filtering specifications.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting: Optional SortSpec object defining the sort order of results.
                     If provided, it will be converted to XML format.
            filtering: Optional FilterSpec object defining filter criteria for results.
                       If provided, it will be converted to XML format.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object containing the job attribute data in XML format.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="status", value="active")
            >>> response = catalog.get_job_attribute_xml(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetJobAttributeXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_attribute(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve object attributes from the catalog service.

        This method calls the 'GetObjectAttribute' SOAP operation with optional sorting
        and filtering specifications.

        Args:
            *args: Variable length argument list passed to the underlying SOAP call.
            sorting: Optional sorting specification to order the results. If provided,
                it will be converted to XML format.
            filtering: Optional filtering specification to filter the results. If provided,
                it will be converted to XML format.
            **kwargs: Arbitrary keyword arguments passed to the underlying SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the
                requested object attributes.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(field="type", value="product")
            >>> response = catalog.get_object_attribute(
            ...     sorting=sort_spec,
            ...     filtering=filter_spec
            ... )
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectAttribute", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_attribute_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve object attributes in XML format from the SOAP service.

        This method calls the 'GetObjectAttributeXml' SOAP operation with optional
        sorting and filtering specifications.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing object attributes
                in XML format.

        Example:
            >>> catalog = CatalogService()
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(criteria="active=true")
            >>> response = catalog.get_object_attribute_xml(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectAttributeXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_category_question(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve object category questions from the catalog service.

        This method calls the GetObjectCategoryQuestion SOAP operation with optional sorting
        and filtering specifications.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting (Optional[SortSpec]): Specification for sorting the results. If provided,
                it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec]): Specification for filtering the results. If provided,
                it will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service containing the object
                category questions data.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectCategoryQuestion", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_object_category_question_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieves object category question data in XML format from the SOAP service.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting: Optional sorting specification to apply to the results.
            filtering: Optional filtering specification to apply to the results.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing object category
                          question data in XML format.

        Note:
            The sorting and filtering parameters are converted to XML format before being
            passed to the underlying SOAP service call.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetObjectCategoryQuestionXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_question(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve questions from the catalog service.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Specification for sorting the results.
                Defaults to None.
            filtering (Optional[FilterSpec], optional): Specification for filtering the results.
                Defaults to None.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the GetQuestion SOAP service call.

        Note:
            If sorting or filtering specifications are provided, they will be converted
            to XML format before being passed to the SOAP service.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetQuestion", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def get_question_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Retrieve question data in XML format from the catalog service.

        This method calls the SOAP service's GetQuestionXml operation with optional
        sorting and filtering parameters.

        Args:
            *args: Additional positional arguments to pass to the SOAP call.
            sorting: Optional SortSpec object defining the sort order for the results.
            filtering: Optional FilterSpec object defining filters to apply to the results.
            **kwargs: Additional keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SOAP service containing question data in XML format.

        Example:
            >>> sort_spec = SortSpec(field="title", order="asc")
            >>> filter_spec = FilterSpec(category="math")
            >>> response = service.get_question_xml(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("GetQuestionXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def set_job_attributes(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Set job attributes with optional sorting and filtering.

        This method calls the SOAP service's SetJobAttributes operation, allowing you to
        configure job attributes with optional sorting and filtering specifications.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting (Optional[SortSpec], optional): Sorting specification for the job attributes.
                If provided, it will be converted to XML format. Defaults to None.
            filtering (Optional[FilterSpec], optional): Filtering specification for the job attributes.
                If provided, it will be converted to XML format. Defaults to None.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response object from the SOAP service call.

        Example:
            >>> sort_spec = SortSpec(field="name", order="asc")
            >>> filter_spec = FilterSpec(criteria="active")
            >>> response = service.set_job_attributes(sorting=sort_spec, filtering=filter_spec)
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("SetJobAttributes", sort=sort_xml, filter=filter_xml, *args, **kwargs)

    def set_job_attributes_xml(self, *args: Any, sorting: Optional[SortSpec] = None, filtering: Optional[FilterSpec] = None, **kwargs: Any) -> SoapResponse:
        """
        Set job attributes using XML-based sorting and filtering specifications.

        Args:
            *args: Variable length argument list to pass to the SOAP call.
            sorting: Optional SortSpec object defining the sort order for job attributes.
                     If provided, it will be converted to XML format.
            filtering: Optional FilterSpec object defining filters for job attributes.
                       If provided, it will be converted to XML format.
            **kwargs: Arbitrary keyword arguments to pass to the SOAP call.

        Returns:
            SoapResponse: The response from the SetJobAttributesXml SOAP operation.
        """
        sort_xml = sorting.to_xml() if sorting else ""
        filter_xml = filtering.to_xml() if filtering else ""
        return self._call("SetJobAttributesXml", sort=sort_xml, filter=filter_xml, *args, **kwargs)
