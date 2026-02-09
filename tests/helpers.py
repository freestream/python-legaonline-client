
import datetime as dt
import inspect
from decimal import Decimal
from typing import Any, Optional, get_args, get_origin

from lega_soap.query import IntListSpec, FilterSpec, SortSpec, XmlArray, XmlNode, AnswerPriceInfo


class FakeAuth:
    def __init__(self, token: str = "TOKEN123") -> None:
        self._token = token

    def ensure_valid_token(self) -> str:
        return self._token


def _dummy_for_annotation(ann):
    origin = get_origin(ann)
    args = get_args(ann)
    if origin is Optional:
        if args:
            return _dummy_for_annotation(args[0])

    if ann is inspect._empty or ann is Any:
        return "x"
    if ann is int:
        return 1
    if ann is float:
        return 1.0
    if ann is bool:
        return False
    if ann is str:
        return "x"
    if ann is Decimal:
        return Decimal("1.0")
    if ann is dt.date:
        return dt.date(2026, 2, 4)
    if ann is dt.datetime:
        return dt.datetime(2026, 2, 4, 12, 0, 0)
    if ann is IntListSpec:
        return IntListSpec.from_list([1, 2])
    if ann is FilterSpec:
        return FilterSpec.from_tuples(("Id", "1", "eq"))
    if ann is SortSpec:
        return SortSpec.from_tuples(("Id", "asc"))
    if ann is XmlArray:
        return XmlArray("Ids", "int", [1, 2])
    if ann is XmlNode:
        return XmlNode("X", {"A": 1})
    if ann is AnswerPriceInfo:
        return AnswerPriceInfo(answer_id=1, price=Decimal("1.0"))
    return "x"


def build_required_kwargs(fn):
    sig = inspect.signature(fn)
    kwargs = {}
    for name, p in sig.parameters.items():
        if name == "self":
            continue
        if p.default is not inspect._empty:
            continue
        kwargs[name] = _dummy_for_annotation(p.annotation)
    return kwargs
