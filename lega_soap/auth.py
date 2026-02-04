from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .exceptions import AuthError


@dataclass(frozen=True)
class Credentials:
    user_id: int
    hash: str


class AuthManager:
    def __init__(self, zeep_service, creds: Credentials):
        self._service = zeep_service
        self._creds = creds
        self._token: Optional[str] = None

    @property
    def token(self) -> str:
        if not self._token:
            raise AuthError("Auth token not initialized. Call authenticate() first.")
        return self._token

    def authenticate(self) -> str:
        try:
            token = self._service.GetAuthToken(self._creds.user_id, self._creds.hash)
        except Exception as e:
            raise AuthError(f"GetAuthToken failed: {e}") from e

        if not token:
            raise AuthError("GetAuthToken returned empty token.")

        self._token = token
        return token

    def validate(self) -> bool:
        if not self._token:
            return False
        try:
            return bool(self._service.ValidateAuthToken(self._token))
        except Exception:
            return False

    def ensure_valid_token(self) -> str:
        if self._token and self.validate():
            return self._token
        return self.authenticate()
