import pytest
from lega_soap.query import FilterSpec, SortSpec, FilterClause, SortClause


def test_filter_condition_normalization():
    f = FilterClause("Status", "active", "eq")
    assert f.normalized_condition() == "="

    f2 = FilterClause("OccasionID", "12,13", "in")
    assert f2.normalized_condition() == "in"

    f3 = FilterClause("X", "1", ">=")
    assert f3.normalized_condition() == ">="


def test_filter_invalid_condition_raises():
    with pytest.raises(ValueError):
        FilterClause("Status", "active", "contains").normalized_condition()


def test_filter_spec_to_xml_empty_is_empty_string():
    assert FilterSpec().to_xml() == ""


def test_filter_spec_to_xml():
    spec = FilterSpec.from_tuples(
        ("OccasionID", "12,13", "in"),
        ("Status", "active", "eq"),
    )
    xml = spec.to_xml()
    assert xml.startswith("<Filtering>")
    assert "<FilterName>OccasionID</FilterName>" in xml
    assert "<FilterValue>12,13</FilterValue>" in xml
    assert "<FilterCondition>in</FilterCondition>" in xml
    assert "<FilterName>Status</FilterName>" in xml
    assert "<FilterCondition>=</FilterCondition>" in xml
    assert xml.endswith("</Filtering>")


def test_sort_invalid_direction_raises():
    with pytest.raises(ValueError):
        SortClause("Status", "up").normalized_direction()


def test_sort_spec_to_xml_empty_is_empty_string():
    assert SortSpec().to_xml() == ""


def test_sort_spec_to_xml():
    spec = SortSpec.from_tuples(
        ("OccasionID", "asc"),
        ("Status", "desc"),
    )
    xml = spec.to_xml()
    assert xml.startswith("<Sorting>")
    assert "<SortName>OccasionID</SortName>" in xml
    assert "<SortDirection>asc</SortDirection>" in xml
    assert "<SortName>Status</SortName>" in xml
    assert "<SortDirection>desc</SortDirection>" in xml
    assert xml.endswith("</Sorting>")
