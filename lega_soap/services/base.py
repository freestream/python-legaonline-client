from __future__ import annotations

from typing import Any, Callable, Dict
import datetime as dt

from zeep.helpers import serialize_object

from ..exceptions import ServiceError
from ..sanitize import sanitize_object


_EMPTY = (None, "", [], {}, ())


class BaseService:
    def __init__(self, zeep_service, auth_manager, tzinfo: dt.tzinfo):
        self._service = zeep_service
        self._auth = auth_manager
        self._tzinfo = tzinfo

    def _call(self, method_name: str, *args, **kwargs) -> Any:
        token = self._auth.ensure_valid_token()

        try:
            method: Callable[..., Any] = getattr(self._service, method_name)
        except AttributeError as e:
            raise ServiceError(f"SOAP method not found: {method_name}") from e

        filtered_kwargs: Dict[str, Any] = {k: v for k, v in kwargs.items() if v not in _EMPTY}

        try:
            result = method(token, *args, **filtered_kwargs)
        except Exception as e:
            raise ServiceError(f"{method_name} failed: {e}") from e

        serialized = serialize_object(result)
        return sanitize_object(serialized, self._tzinfo)
