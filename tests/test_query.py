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
    def test_filter_clause_to_xml_fragment():
        f = FilterClause("Name", "John", "=")
        xml = f.to_xml_fragment()
        assert xml == "<Filter><FilterName>Name</FilterName><FilterValue>John</FilterValue><FilterCondition>=</FilterCondition></Filter>"


    def test_filter_clause_to_xml_fragment_with_html_escaping():
        f = FilterClause("Field<>", "Value&", "=")
        xml = f.to_xml_fragment()
        assert "<FilterName>Field&lt;&gt;</FilterName>" in xml
        assert "<FilterValue>Value&amp;</FilterValue>" in xml


    def test_filter_clause_default_condition():
        f = FilterClause("Status", "active")
        assert f.condition == "="
        assert f.normalized_condition() == "="


    def test_filter_condition_case_insensitive():
        f = FilterClause("Status", "active", "EQ")
        assert f.normalized_condition() == "="
        
        f2 = FilterClause("Status", "active", "IN")
        assert f2.normalized_condition() == "in"


    def test_filter_spec_is_empty():
        spec = FilterSpec()
        assert spec.is_empty() is True
        
        spec2 = FilterSpec.from_tuples(("Status", "active", "="))
        assert spec2.is_empty() is False


    def test_filter_spec_from_tuples():
        spec = FilterSpec.from_tuples(
            ("Field1", "Value1", "="),
            ("Field2", "Value2", "!=")
        )
        assert len(spec.clauses) == 2
        assert spec.clauses[0].field == "Field1"
        assert spec.clauses[1].field == "Field2"


    def test_sort_clause_to_xml_fragment():
        s = SortClause("Name", "asc")
        xml = s.to_xml_fragment()
        assert xml == "<Sort><SortName>Name</SortName><SortDirection>asc</SortDirection></Sort>"


    def test_sort_clause_to_xml_fragment_with_html_escaping():
        s = SortClause("Field<>", "desc")
        xml = s.to_xml_fragment()
        assert "<SortName>Field&lt;&gt;</SortName>" in xml
        assert "<SortDirection>desc</SortDirection>" in xml


    def test_sort_clause_default_direction():
        s = SortClause("Status")
        assert s.direction == "asc"
        assert s.normalized_direction() == "asc"


    def test_sort_direction_case_insensitive():
        s = SortClause("Status", "ASC")
        assert s.normalized_direction() == "asc"
        
        s2 = SortClause("Status", "DESC")
        assert s2.normalized_direction() == "desc"


    def test_sort_spec_is_empty():
        spec = SortSpec()
        assert spec.is_empty() is True
        
        spec2 = SortSpec.from_tuples(("Status", "asc"))
        assert spec2.is_empty() is False


    def test_sort_spec_from_tuples():
        spec = SortSpec.from_tuples(
            ("Field1", "asc"),
            ("Field2", "desc")
        )
        assert len(spec.clauses) == 2
        assert spec.clauses[0].field == "Field1"
        assert spec.clauses[0].direction == "asc"
        assert spec.clauses[1].field == "Field2"
        assert spec.clauses[1].direction == "desc"


    def test_filter_all_condition_mappings():
        assert FilterClause("F", "V", "ne").normalized_condition() == "!="
        assert FilterClause("F", "V", "gt").normalized_condition() == ">"
        assert FilterClause("F", "V", "lt").normalized_condition() == "<"
        assert FilterClause("F", "V", "gte").normalized_condition() == ">="
        assert FilterClause("F", "V", "ge").normalized_condition() == ">="
        assert FilterClause("F", "V", "lte").normalized_condition() == "<="
        assert FilterClause("F", "V", "le").normalized_condition() == "<="


    def test_filter_direct_operators():
        assert FilterClause("F", "V", "=").normalized_condition() == "="
        assert FilterClause("F", "V", "!=").normalized_condition() == "!="
        assert FilterClause("F", "V", ">").normalized_condition() == ">"
        assert FilterClause("F", "V", "<").normalized_condition() == "<"
        assert FilterClause("F", "V", ">=").normalized_condition() == ">="
        assert FilterClause("F", "V", "<=").normalized_condition() == "<="

