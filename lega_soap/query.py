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
    field: str
    value: str
    condition: str = "="

    def normalized_condition(self) -> str:
        cond = self.condition.lower()
        if cond not in _ALLOWED_FILTER_CONDITIONS:
            raise ValueError(f"Invalid filter condition: {self.condition}")
        return _COND_MAP.get(cond, cond)

    def to_xml_fragment(self) -> str:
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
    field: str
    direction: str = "asc"

    def normalized_direction(self) -> str:
        d = self.direction.lower()
        if d not in _ALLOWED_SORT_DIRECTIONS:
            raise ValueError(f"Invalid sort direction: {self.direction}")
        return d

    def to_xml_fragment(self) -> str:
        d = self.normalized_direction()
        return (
            f"<Sort>"
            f"<SortName>{html.escape(self.field)}</SortName>"
            f"<SortDirection>{d}</SortDirection>"
            f"</Sort>"
        )


@dataclass(frozen=True)
class FilterSpec:
    clauses: Tuple[FilterClause, ...] = ()

    @staticmethod
    def from_tuples(*filters: Tuple[str, str, str]) -> "FilterSpec":
        return FilterSpec(tuple(FilterClause(f, v, c) for f, v, c in filters))

    def is_empty(self) -> bool:
        return len(self.clauses) == 0

    def to_xml(self) -> str:
        if self.is_empty():
            return ""
        inner = "".join(c.to_xml_fragment() for c in self.clauses)
        # API-dokumentationen har förekommit med både "Filtering" och "Filtrering".
        # Behåll "Filtering" för kompatibilitet med din befintliga kod.
        return f"<Filtering>{inner}</Filtering>"


@dataclass(frozen=True)
class SortSpec:
    clauses: Tuple[SortClause, ...] = ()

    @staticmethod
    def from_tuples(*sorts: Tuple[str, str]) -> "SortSpec":
        return SortSpec(tuple(SortClause(f, d) for f, d in sorts))

    def is_empty(self) -> bool:
        return len(self.clauses) == 0

    def to_xml(self) -> str:
        if self.is_empty():
            return ""
        inner = "".join(c.to_xml_fragment() for c in self.clauses)
        return f"<Sorting>{inner}</Sorting>"
