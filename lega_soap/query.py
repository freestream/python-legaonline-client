from __future__ import annotations

from decimal import Decimal
from dataclasses import dataclass
from typing import Any, Mapping, Optional, Sequence, Union, Tuple, Generic, TypeVar
import html
import datetime as dt


XmlScalar = Union[str, int, float, bool, Decimal]
XmlValue = Union["XmlNode", "XmlArray", XmlScalar, None, Sequence[Any]]

T = TypeVar("T")

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


def _escape_scalar(v: XmlScalar) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    return html.escape(str(v))


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
    the filtering criteria to be applied when querying the LegaOnline SOAP API.

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


@dataclass(frozen=True)
class IntListSpec:
    """
    A specification class for handling lists of integers in XML format.

    This class provides functionality to store, validate, and convert integer sequences
    to XML representation, with optional wrapping in a parent element.

    Attributes:
        values (Tuple[int, ...]): A tuple of integer values. Defaults to an empty tuple.

    Methods:
        from_list(values: Sequence[int]) -> IntListSpec:
            Creates an IntListSpec instance from a sequence of integers.

            Args:
                values: A sequence of integers to convert.

            Returns:
                A new IntListSpec instance with the provided values.

        is_empty() -> bool:
            Checks if the specification contains any values.

            Returns:
                True if there are no values, False otherwise.

        to_xml(*, wrap: str | None = None) -> str:
            Converts the integer list to an XML string representation.

            Args:
                wrap: Optional name of a wrapper element to enclose the integer list.

            Returns:
                An XML string with each integer wrapped in <int> tags. If wrap is provided,
                the entire list is enclosed in the specified wrapper element. Returns an
                empty string if the specification is empty.
    """
    values: Tuple[int, ...] = ()

    @staticmethod
    def from_list(values: Sequence[int]) -> "IntListSpec":
        """
        Create an IntListSpec from a sequence of integer values.

        Args:
            values (Sequence[int]): A sequence of integer values to convert into an IntListSpec.

        Returns:
            IntListSpec: A new IntListSpec instance containing the provided values as a tuple.

        Example:
            >>> IntListSpec.from_list([1, 2, 3])
            IntListSpec((1, 2, 3))
        """
        return IntListSpec(tuple(int(v) for v in values))

    def is_empty(self) -> bool:
        """
        Check if the query has no values.

        Returns:
            bool: True if the values list is empty, False otherwise.
        """
        return len(self.values) == 0

    def to_xml(self, *, wrap: str | None = None) -> str:
        """
        Convert the object to an XML string representation.

        Args:
            wrap (str | None, optional): If provided, wraps the generated XML elements
                in an outer tag with this name. Defaults to None.

        Returns:
            str: An XML string containing <int> elements for each value in self.values.
                Returns an empty string if the object is empty. If wrap is provided,
                the <int> elements are wrapped in the specified tag.

        Example:
            >>> obj.values = [1, 2, 3]
            >>> obj.to_xml()
            '<int>1</int><int>2</int><int>3</int>'
            >>> obj.to_xml(wrap='numbers')
            '<numbers><int>1</int><int>2</int><int>3</int></numbers>'
        """
        if self.is_empty():
            return ""
        inner = "".join(f"<int>{v}</int>" for v in self.values)
        if wrap:
            return f"<{wrap}>{inner}</{wrap}>"
        return inner


@dataclass(frozen=True)
class StrListSpec:
    """
    A specification class for handling lists of strings in XML format.

    This class provides functionality to store, validate, and convert string sequences
    to XML representation, with optional wrapping in a parent element.

    Attributes:
        values (Tuple[str, ...]): A tuple of string values. Defaults to an empty tuple.

    Methods:
        from_list(values: Sequence[str]) -> StrListSpec:
            Creates an StrListSpec instance from a sequence of strings.

            Args:
                values: A sequence of strings to convert.

            Returns:
                A new StrListSpec instance with the provided values.

        is_empty() -> bool:
            Checks if the specification contains any values.

            Returns:
                True if there are no values, False otherwise.

        to_xml(*, wrap: str | None = None) -> str:
            Converts the string list to an XML string representation.
            Args:
                wrap: Optional name of a wrapper element to enclose the string list.

            Returns:
                An XML string with each string wrapped in <string> tags. If wrap is provided,
                the entire list is enclosed in the specified wrapper element. Returns an
                empty string if the specification is empty.
    """
    values: Tuple[str, ...] = ()

    @staticmethod
    def from_list(values: Sequence[str]) -> "StrListSpec":
        """
        Create an StrListSpec from a sequence of string values.

        Args:
            values (Sequence[str]): A sequence of string values to convert into an StrListSpec.

        Returns:
            StrListSpec: A new StrListSpec instance containing the provided values as a tuple.

        Example:
            >>> StrListSpec.from_list(["a", "b", "c"])
            StrListSpec(("a", "b", "c"))
        """
        return StrListSpec(tuple(values))

    def is_empty(self) -> bool:
        """
        Check if the query has no values.

        Returns:
            bool: True if the values list is empty, False otherwise.
        """
        return len(self.values) == 0

    def to_xml(self, *, wrap: str | None = None) -> str:
        """
        Convert the object to an XML string representation.

        Args:
            wrap (str | None, optional): If provided, wraps the generated XML elements
                in an outer tag with this name. Defaults to None.

        Returns:
            str: An XML string containing <string> elements for each value in self.values.
                Returns an empty string if the object is empty. If wrap is provided,
                the <string> elements are wrapped in the specified tag.

        Example:
            >>> obj.values = ["a", "b", "c"]
            >>> obj.to_xml()
            '<string>a</string><string>b</string><string>c</string>'
            >>> obj.to_xml(wrap='strings')
            '<strings><string>a</string><string>b</string><string>c</string></strings>'
        """
        if self.is_empty():
            return ""
        inner = "".join(f"<string>{v}</string>" for v in self.values)
        if wrap:
            return f"<{wrap}>{inner}</{wrap}>"
        return inner


@dataclass(frozen=True)
class XmlNode:
    """
    Generic XML element with dynamic children.

    - fields values can be:
      - scalar => <Key>value</Key>
      - XmlNode/XmlArray => embedded as-is
      - list/tuple => repeats the key tag for each item (useful for maxOccurs=unbounded)
    """
    tag: str
    fields: Mapping[str, XmlValue]

    def to_xml(self) -> str:
        inner: list[str] = []

        for key, value in self.fields.items():
            if value is None:
                continue

            # Embedded nodes
            if isinstance(value, (XmlNode, XmlArray)):
                inner.append(value.to_xml())
                continue

            # Repeated elements: <key>...</key><key>...</key>
            if isinstance(value, (list, tuple)):
                for item in value:
                    if item is None:
                        continue
                    if isinstance(item, (XmlNode, XmlArray)):
                        # If you want repeated <key> wrapper around XmlNode, wrap explicitly with XmlNode(tag=key,...)
                        inner.append(item.to_xml())
                    else:
                        inner.append(f"<{key}>{_escape_scalar(item)}</{key}>")
                continue

            # Scalar
            inner.append(f"<{key}>{_escape_scalar(value)}</{key}>")

        return f"<{self.tag}>{''.join(inner)}</{self.tag}>"


@dataclass(frozen=True)
class XmlArray(Generic[T]):
    """
    Wrapper tag + repeated item tag.

    Example (ArrayOfInt in ops):
      XmlArray("occasionIDs", "int", [1,2])
      -> <occasionIDs><int>1</int><int>2</int></occasionIDs>

    Example (CalculatePriceInfo/AnswerPriceInfo):
      XmlArray("AnswerPriceInfo", "AnswerPriceInfo", [XmlNode("AnswerPriceInfo", {...})])
      -> <AnswerPriceInfo><AnswerPriceInfo>...</AnswerPriceInfo></AnswerPriceInfo>
    """
    wrapper_tag: str
    item_tag: str
    items: Sequence[Union[XmlNode, XmlScalar]]

    def to_xml(self) -> str:
        """
        Serializes the items in the collection to an XML string.

        Returns:
            str: An XML representation of the items, wrapped in the specified wrapper tag.
                 If the collection is empty, returns an empty string.

        The method iterates over each item in `self.items`:
            - If the item is an instance of XmlNode and its tag matches `self.item_tag`, its XML is appended directly.
            - If the item is an XmlNode but its tag differs, it is wrapped in `self.item_tag` tags.
            - Otherwise, the item is treated as a scalar, escaped, and wrapped in `self.item_tag` tags.
        The resulting XML fragments are concatenated and wrapped in `self.wrapper_tag`.
        """
        if not self.items:
            return ""

        inner: list[str] = []
        for item in self.items:
            if isinstance(item, XmlNode):
                # If node.tag differs from item_tag, wrap it
                if item.tag == self.item_tag:
                    inner.append(item.to_xml())
                else:
                    inner.append(
                        f"<{self.item_tag}>{item.to_xml()}</{self.item_tag}>")
            else:
                inner.append(
                    f"<{self.item_tag}>{_escape_scalar(item)}</{self.item_tag}>")

        return f"<{self.wrapper_tag}>{''.join(inner)}</{self.wrapper_tag}>"


@dataclass(frozen=True)
class AnswerPriceInfo:
    """
    Represents pricing information for an answer in the LegaOnline SOAP API.

    Attributes:
        answer_id (int): The unique identifier for the answer.
        price (Union[Decimal, int, float, str]): The price associated with the answer.
            Can be represented as a Decimal, integer, float, or string value.

    Methods:
        to_xml() -> XmlNode: Converts the answer price information to an XML node
            representation with 'AnswerID' and 'Price' attributes.
    """
    answer_id: int
    price: Union[Decimal, int, float, str]

    def to_xml(self) -> XmlNode:
        """
        Convert the AnswerPriceInfo object to an XML node representation.

        Returns:
            XmlNode: An XML node with tag "AnswerPriceInfo" containing the answer ID and price as attributes.
        """
        return XmlNode(
            "AnswerPriceInfo",
            {
                "AnswerID": self.answer_id,
                "Price": self.price,
            },
        )

@dataclass(frozen=True)
class JobSpec:
    """
    Logical representation of a Job payload for SetJobs / SetJob.

    This maps to the Job complexType in the WSDL.
    """
    job_id: Optional[int] = None
    occasion_id: Optional[int] = None
    customer_id: Optional[int] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None

    def to_xml(self) -> XmlNode:
        """
        Converts the current job instance into an XmlNode representation.

        Returns:
            XmlNode: An XmlNode object representing the job, with attributes for JobID, OccasionID,
            CustomerID, StartDate, EndDate, and Description.
        """
        return XmlNode(
            "Job",
            {
                "JobID": self.job_id,
                "OccasionID": self.occasion_id,
                "CustomerID": self.customer_id,
                "StartDate": self.start_date,
                "EndDate": self.end_date,
                "Description": self.description,
            },
        )
        
@dataclass(frozen=True)
class OccasionAnswerSpec:
    """
    Logical representation of an OccasionAnswer item for SetOccasionAnswer.

    Typical fields in these APIs:
      - OccasionID (int)
      - QuestionID (int) or AnswerID (int)
      - Value (string) and/or Quantity (int) and/or Price (decimal)

    Adjust field names to match your WSDL once confirmed.
    """
    occasion_id: int
    answer_id: int
    value: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[Union[Decimal, int, float, str]] = None

    def to_xml(self) -> "XmlNode":
        """
        Converts the current instance into an XmlNode representing an 'OccasionAnswer'.

        Returns:
            XmlNode: An XmlNode object with the tag 'OccasionAnswer' and attributes
                populated from the instance's occasion_id, answer_id, value, quantity, and price.
        """
        return XmlNode(
            "OccasionAnswer",
            {
                "OccasionID": self.occasion_id,
                "AnswerID": self.answer_id,
                "Value": self.value,
                "Quantity": self.quantity,
                "Price": self.price,
            },
        )

@dataclass(frozen=True)
class OccasionLocationSpec:
    """
    Logical representation of an OccasionLocation item for SetOccasionLocation.

    Adjust field names to match your WSDL once confirmed.
    """
    occasion_id: Optional[int] = None
    location_id: Optional[int] = None
    location_address_id: Optional[int] = None

    def to_xml(self) -> "XmlNode":
        """
        Converts the current instance into an XmlNode representing an OccasionLocation.

        Returns:
            XmlNode: An XmlNode object with the tag "OccasionLocation" and attributes
                "OccasionID", "LocationID", and "LocationAddressID" populated from the instance.
        """
        return XmlNode(
            "OccasionLocation",
            {
                "OccasionID": self.occasion_id,
                "LocationID": self.location_id,
                "LocationAddressID": self.location_address_id,
            },
        )

@dataclass(frozen=True)
class OccasionObjectAnswerSpec:
    """
    Logical representation of an OccasionObjectAnswerSpec item for SetOccasionObjectAnswerSpec.

    Adjust field names to match your WSDL once confirmed.
    """
    answer_id: Optional[int] = None
    occasion_id: Optional[int] = None
    object_id: Optional[int] = None
    answer_text: Optional[str] = None
    answer_time: Optional[dt.datetime] = None
    answer_number: Optional[int] = None

    def to_xml(self) -> "XmlNode":
        """
        Converts the current object instance into an XmlNode representing an "OccObjectAnswer".

        Returns:
            XmlNode: An XmlNode object with the tag "OccObjectAnswer" and attributes populated
            from the instance's answer_id, occasion_id, object_id, answer_text, answer_time, and answer_number.
        """
        return XmlNode(
            "OccObjectAnswer",
            {
                "AnswerID": self.answer_id,
                "OccasionID": self.occasion_id,
                "ObjectID": self.object_id,
                "AnswerText": self.answer_text,
                "AnswerTime": self.answer_time,
                "AnswerNumber": self.answer_number,
            },
        )

@dataclass(frozen=True)
class OccasionParticipantNumberSpec:
    """
    Logical representation of an OccasionParticipantNumberSpec item for SetOccasionParticipantNumberSpec.

    Adjust field names to match your WSDL once confirmed.
    """
    participant_number: Optional[int] = None
    occasion_id: Optional[int] = None

    def to_xml(self) -> "XmlNode":
        """
        Converts the current instance into an XmlNode representing an OccasionParticipantNumber.

        Returns:
            XmlNode: An XML node with the tag "OccasionParticipantNumber" and attributes
                "ParticipantNumber" and "OccasionID" set from the instance's properties.
        """
        return XmlNode(
            "OccasionParticipantNumber",
            {
                "ParticipantNumber": self.participant_number,
                "OccasionID": self.occasion_id,
            },
        )

@dataclass(frozen=True)
class OccasionQuantitySpec:
    """
    Logical representation of an OccasionQuantitySpec item for SetOccasionQuantitySpec.

    Adjust field names to match your WSDL once confirmed.
    """
    occasion_id: Optional[int] = None
    quantity: Optional[int] = None

    def to_xml(self) -> "XmlNode":
        """
        Converts the current instance into an XmlNode representing an 'OccasionQuantity' element.

        Returns:
            XmlNode: An XmlNode object with the tag 'OccasionQuantity' and attributes
                'OccasionID' and 'Quantity' set to the instance's corresponding values.
        """
        return XmlNode(
            "OccasionQuantity",
            {
                "OccasionID": self.occasion_id,
                "Quantity": self.quantity,
            },
        )

@dataclass(frozen=True)
class OccasionSeatingInfoSpec:
    """
    Logical representation of an OccasionSeatingInfoSpec item for SetOccasionSeatingInfoSpec.

    Adjust field names to match your WSDL once confirmed.
    """
    occasion_id: Optional[int] = None
    seating_id: Optional[int] = None

    def to_xml(self) -> "XmlNode":
        """
        Converts the current instance into an XmlNode representing occasion seating information.

        Returns:
            XmlNode: An XML node with the tag "OccasionSeatingInfo" and attributes "OccasionID" and "SeatingID"
                populated from the instance's occasion_id and seating_id.
        """
        return XmlNode(
            "OccasionSeatingInfo",
            {
                "OccasionID": self.occasion_id,
                "SeatingID": self.seating_id,
            },
        )

@dataclass(frozen=True)
class ReportParameterSpec:
    """
    Logical representation of an ReportParameterSpec item for SetReportParameterSpec.

    Adjust field names to match your WSDL once confirmed.
    """
    name: Optional[str] = None
    value: Optional[str] = None

    def to_xml(self) -> "XmlNode":
        """
        Converts the current object into an XmlNode representing a report parameter.

        Returns:
            XmlNode: An XmlNode instance with the tag "ReportParameter" and attributes
                "Name" and "Value" set to the object's name and value, respectively.
        """
        return XmlNode(
            "ReportParameter",
            {
                "Name": self.name,
                "Value": self.value,
            },
        )


@dataclass(frozen=True)
class OrderInfoSpec:
    """
    Logical representation of an OrderInfoSpec item for SetOrderInfoSpec.

    Adjust field names to match your WSDL once confirmed.
    """
    pickup: Optional[bool] = None
    reservation_id: Optional[int] = None
    pickup_earliest: Optional[dt.datetime] = None
    pickup_latest: Optional[dt.datetime] = None
    delivery_latest: Optional[dt.datetime] = None
    sender_reference: Optional[str] = None
    goods_type: Optional[str] = None
    message: Optional[str] = None
    weight: Optional[float] = None
    volume: Optional[float] = None
    package_count: Optional[int] = None
    distance_kilometers: Optional[float] = None
    pickup_name: Optional[str] = None
    pickup_address: Optional[str] = None
    pickup_address2: Optional[str] = None
    pickup_entre_code: Optional[str] = None
    pickup_zip: Optional[str] = None
    pickup_city: Optional[str] = None
    pickup_phone: Optional[str] = None
    delivery_name: Optional[str] = None
    delivery_address: Optional[str] = None
    delivery_address2: Optional[str] = None
    delivery_entre_code: Optional[str] = None
    delivery_zip: Optional[str] = None
    delivery_city: Optional[str] = None
    delivery_phone: Optional[str] = None

    def to_xml(self) -> "XmlNode":
        """
        Converts the current object's order information into an XmlNode representation.

        Returns:
            XmlNode: An XmlNode instance with the tag "OrderInfo" and attributes populated
            from the object's properties, including pickup and delivery details, reservation
            information, goods type, message, weight, volume, package count, distance, and
            contact information for both pickup and delivery locations.
        """
        return XmlNode(
            "OrderInfo",
            {
                "Pickup": self.pickup,
                "ReservationID": self.reservation_id,
                "PickupEarliest": self.pickup_earliest,
                "PickupLatest": self.pickup_latest,
                "DeliveryLatest": self.delivery_latest,
                "SenderReference": self.sender_reference,
                "GoodsType": self.goods_type,
                "Message": self.message,
                "Weight": self.weight,
                "Volume": self.volume,
                "PackageCount": self.package_count,
                "DistanceKilometers": self.distance_kilometers,
                "PickupName": self.pickup_name,
                "PickupAddress": self.pickup_address,
                "PickupAddress2": self.pickup_address2,
                "PickupEntreCode": self.pickup_entre_code,
                "PickupZip": self.pickup_zip,
                "PickupCity": self.pickup_city,
                "PickupPhone": self.pickup_phone,
                "DeliveryName": self.delivery_name,
                "DeliveryAddress": self.delivery_address,
                "DeliveryAddress2": self.delivery_address2,
                "DeliveryEntreCode": self.delivery_entre_code,
                "DeliveryZip": self.delivery_zip,
                "DeliveryCity": self.delivery_city,
                "DeliveryPhone": self.delivery_phone,
            },
        )
