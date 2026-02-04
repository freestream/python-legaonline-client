from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List, Optional, Sequence, Tuple, Union
import html


_ALLOWED_FILTER_CONDITIONS = {
    "=", "!=", ">", "<", ">=", "<=",
    "in", "eq", "ne", "gt", "lt", "gte", "ge", "lte", "le",
}

_COND_MAP = {
    "eq": "=",
    "ne": "!=",
    "gt": ">",
    "lt": "<",
    "gte": ">=",
    "ge": ">=",
    "lte": "<=",
    "le": "<=",
    "in": "in",
}


_ALLOWED_SORT_DIRECTIONS = {"asc", "desc"}


@dataclass(frozen=True)
class FilterClause:
    """
    Represents a single filter clause for querying data.

    A FilterClause defines a condition to filter data based on a field name, 
    a value, and a comparison operator (condition).

    Attributes:
        field (str): The name of the field to filter on.
        value (str): The value to compare against.
        condition (str): The comparison operator (default is "="). Must be one of 
            the allowed filter conditions defined in _ALLOWED_FILTER_CONDITIONS.

    Methods:
        normalized_condition() -> str:
            Returns the normalized condition string, converting it to lowercase
            and validating it against allowed conditions. Applies any mappings
            defined in _COND_MAP.
            
            Raises:
                ValueError: If the condition is not in the allowed list.
        
        to_xml_fragment() -> str:
            Converts the filter clause to an XML fragment string with proper
            HTML escaping for field names, values, and conditions.
            
            Returns:
                str: XML string representation of the filter clause in the format:
                    <Filter>
                        <FilterName>...</FilterName>
                        <FilterValue>...</FilterValue>
                        <FilterCondition>...</FilterCondition>
                    </Filter>
    """
    field: str
    value: str
    condition: str = "="

    def normalized_condition(self) -> str:
        """
        Normalize and validate the filter condition.

        Returns:
            str: The normalized condition string that can be used in queries.

        Raises:
            ValueError: If the condition is not in the list of allowed filter conditions.

        Note:
            The method converts the condition to lowercase, validates it against
            _ALLOWED_FILTER_CONDITIONS, and maps it using _COND_MAP if a mapping exists.
        """
        cond = self.condition.lower()
        if cond not in _ALLOWED_FILTER_CONDITIONS:
            raise ValueError(f"Invalid filter condition: {self.condition}")
        return _COND_MAP.get(cond, cond)

    def to_xml_fragment(self) -> str:
        """
        Convert the filter to an XML fragment string.

        This method generates an XML representation of the filter object, including
        the field name, value, and condition. All values are HTML-escaped to prevent
        XML injection and ensure valid XML output.

        Returns:
            str: An XML string fragment representing the filter in the format:
                <Filter>
                    <FilterName>field_name</FilterName>
                    <FilterValue>field_value</FilterValue>
                    <FilterCondition>normalized_condition</FilterCondition>
                </Filter>

        Note:
            All field values are HTML-escaped for security and XML validity.
            The condition is normalized before being escaped.
        """
        cond = html.escape(self.normalized_condition())
        return (
            f"<Filter>"
            f"<FilterName>{html.escape(self.field)}</FilterName>"
            f"<FilterValue>{html.escape(self.value)}</FilterValue>"
            f"<FilterCondition>{cond}</FilterCondition>"
            f"</Filter>"
        )


@dataclass(frozen=True)
class SortClause:
    """
    Represents a sort clause for database queries.

    A SortClause specifies a field to sort by and the direction of the sort
    (ascending or descending). It can be converted to an XML fragment for
    use in SOAP requests.

    Attributes:
        field (str): The name of the field to sort by.
        direction (str): The sort direction, either "asc" or "desc". Defaults to "asc".

    Methods:
        normalized_direction() -> str:
            Returns the normalized (lowercase) sort direction after validation.
            
            Returns:
                str: The validated and normalized sort direction.
                
            Raises:
                ValueError: If the direction is not in the allowed set of directions.
        
        to_xml_fragment() -> str:
            Converts the sort clause to an XML fragment.
            
            Returns:
                str: An XML string representing the sort clause with escaped field name
                     and validated direction.
    """
    field: str
    direction: str = "asc"

    def normalized_direction(self) -> str:
        """
        Normalize and validate the sort direction.

        Returns:
            str: The normalized sort direction in lowercase.

        Raises:
            ValueError: If the direction is not in the allowed sort directions.
        """
        d = self.direction.lower()
        if d not in _ALLOWED_SORT_DIRECTIONS:
            raise ValueError(f"Invalid sort direction: {self.direction}")
        return d

    def to_xml_fragment(self) -> str:
        """
        Convert the Sort object to an XML fragment string.

        This method generates an XML representation of the Sort object, containing
        the field name and sort direction. The field name is HTML-escaped to prevent
        XML injection attacks.

        Returns:
            str: An XML fragment string in the format:
                <Sort>
                    <SortName>field_name</SortName>
                    <SortDirection>direction</SortDirection>
                </Sort>
                where field_name is the HTML-escaped field name and direction is
                the normalized sort direction.

        Example:
            >>> sort = Sort(field="name", direction="asc")
            >>> sort.to_xml_fragment()
            '<Sort><SortName>name</SortName><SortDirection>ASC</SortDirection></Sort>'
        """
        d = self.normalized_direction()
        return (
            f"<Sort>"
            f"<SortName>{html.escape(self.field)}</SortName>"
            f"<SortDirection>{d}</SortDirection>"
            f"</Sort>"
        )


@dataclass(frozen=True)
class FilterSpec:
    """
    Represents a specification for filtering query results.

    A FilterSpec contains zero or more FilterClause objects that define
    the filtering criteria to be applied when querying the LEGA SOAP API.

    Attributes:
        clauses (Tuple[FilterClause, ...]): A tuple of FilterClause objects
            that define the filtering conditions. Defaults to an empty tuple.

    Methods:
        from_tuples(*filters): Creates a FilterSpec from tuples of filter parameters.
        is_empty(): Checks if the FilterSpec contains any filter clauses.
        to_xml(): Converts the FilterSpec to an XML string representation.

    Example:
        >>> spec = FilterSpec.from_tuples(
        ...     ("field1", "value1", "equals"),
        ...     ("field2", "value2", "contains")
        ... )
        >>> xml = spec.to_xml()
    """
    clauses: Tuple[FilterClause, ...] = ()

    @staticmethod
    def from_tuples(*filters: Tuple[str, str, str]) -> "FilterSpec":
        """
        Create a FilterSpec from tuples of filter parameters.

        Args:
            *filters: Variable length argument list of tuples, where each tuple contains:
                - f (str): The field name to filter on
                - v (str): The value to compare against
                - c (str): The comparison operator/condition

        Returns:
            FilterSpec: A new FilterSpec instance containing FilterClause objects
                        created from the provided tuples.

        Example:
            >>> FilterSpec.from_tuples(
            ...     ("name", "John", "equals"),
            ...     ("age", "30", "greater_than")
            ... )
        """
        return FilterSpec(tuple(FilterClause(f, v, c) for f, v, c in filters))

    def is_empty(self) -> bool:
        """
        Check if the query has no clauses.

        Returns:
            bool: True if there are no clauses in the query, False otherwise.
        """
        return len(self.clauses) == 0

    def to_xml(self) -> str:
        """
        Converts the filter object to an XML string representation.

        Returns:
            str: An XML string with the filter clauses wrapped in a <Filtering> tag.
                 Returns an empty string if the filter is empty (no clauses).

        Note:
            The method uses "Filtering" as the XML tag name for compatibility with
            existing code, although the API documentation has shown both "Filtering"
            and "Filtrering" variants.
        """
        if self.is_empty():
            return ""
        inner = "".join(c.to_xml_fragment() for c in self.clauses)
        return f"<Filtering>{inner}</Filtering>"


@dataclass(frozen=True)
class SortSpec:
    """
    Represents a sorting specification for queries.

    A SortSpec contains zero or more SortClause objects that define how query results
    should be sorted. It can be converted to XML format for use in SOAP requests.

    Attributes:
        clauses (Tuple[SortClause, ...]): A tuple of SortClause objects defining the sort order.
            Defaults to an empty tuple.

    Methods:
        from_tuples(*sorts: Tuple[str, str]) -> SortSpec:
            Creates a SortSpec from tuples of (field, direction) pairs.
            
            Args:
                *sorts: Variable number of tuples, each containing a field name and direction.
            
            Returns:
                SortSpec: A new SortSpec instance with the specified sorting clauses.
        
        is_empty() -> bool:
            Checks if the SortSpec has any sorting clauses.
            
            Returns:
                bool: True if there are no sorting clauses, False otherwise.
        
        to_xml() -> str:
            Converts the SortSpec to its XML representation.
            
            Returns:
                str: XML string wrapped in <Sorting> tags containing all sort clauses,
                    or an empty string if there are no clauses.
    """
    clauses: Tuple[SortClause, ...] = ()

    @staticmethod
    def from_tuples(*sorts: Tuple[str, str]) -> "SortSpec":
        """
        Create a SortSpec from tuples of field names and directions.

        Args:
            *sorts: Variable number of tuples, where each tuple contains:
                - field name (str): The field to sort by
                - direction (str): The sort direction (e.g., 'asc' or 'desc')

        Returns:
            SortSpec: A new SortSpec instance containing SortClause objects created from the input tuples.

        Example:
            >>> SortSpec.from_tuples(('name', 'asc'), ('age', 'desc'))
        """
        return SortSpec(tuple(SortClause(f, d) for f, d in sorts))

    def is_empty(self) -> bool:
        """
        Check if the query has no clauses.

        Returns:
            bool: True if there are no clauses in the query, False otherwise.
        """
        return len(self.clauses) == 0

    def to_xml(self) -> str:
        """
        Convert the sorting configuration to an XML string representation.

        Returns:
            str: An XML string containing sorting clauses wrapped in <Sorting> tags.
                 Returns an empty string if no sorting clauses are present.

        Example:
            >>> sorting.to_xml()
            '<Sorting><SortClause field="name" order="asc"/></Sorting>'
        """
        if self.is_empty():
            return ""
        inner = "".join(c.to_xml_fragment() for c in self.clauses)
        return f"<Sorting>{inner}</Sorting>"
