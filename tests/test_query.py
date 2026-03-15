
from decimal import Decimal
from lega_soap.query import FilterClause, FilterSpec, SortClause, SortSpec, IntListSpec, XmlNode, XmlArray, AnswerPriceInfo


def test_filter_clause_normalizes_conditions() -> None:
    assert FilterClause("A", "1", "eq").normalized_condition() == "="
    assert FilterClause("A", "1", "gte").normalized_condition() == ">="
    assert FilterClause("A", "1", "in").normalized_condition() == "in"


def test_filter_spec_to_xml() -> None:
    spec = FilterSpec.from_tuples(("Status", "eq", "active"))
    xml = spec.to_xml()
    assert xml.startswith("<Filtering>")
    assert "<FilterName>Status</FilterName>" in xml
    assert "<FilterValue>active</FilterValue>" in xml


def test_sort_spec_to_xml() -> None:
    spec = SortSpec.from_tuples(("Name", "asc"), ("Id", "desc"))
    xml = spec.to_xml()
    assert xml.startswith("<Sorting>")
    assert "<SortName>Name</SortName>" in xml
    assert "<SortDirection>asc</SortDirection>" in xml


def test_int_list_spec_to_xml() -> None:
    spec = IntListSpec.from_list([1, 2, 3])
    assert spec.to_xml() == "<int>1</int><int>2</int><int>3</int>"


def test_xml_node_and_array_rendering() -> None:
    node = XmlNode("AttributeAlternative", {
        "AttributeAlternativeID": 7,
        "AttributeAlternativeDescription": "A&B",
    })
    xml = node.to_xml()
    assert "<AttributeAlternativeDescription>A&amp;B</AttributeAlternativeDescription>" in xml

    arr = XmlArray("Ids", "int", [1, 2])
    assert arr.to_xml() == "<Ids><int>1</int><int>2</int></Ids>"


def test_answer_price_info_helper_to_xml() -> None:
    api = AnswerPriceInfo(answer_id=1, price=Decimal("9.50"))
    node = api.to_xml()
    xml = node.to_xml()
    assert "<AnswerID>1</AnswerID>" in xml
    assert "<Price>9.50</Price>" in xml
