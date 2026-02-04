"""Tests for timezone utility functions."""
import os
import datetime as dt
from unittest.mock import patch, MagicMock
from zoneinfo import ZoneInfo
from lega_soap.timezone import get_default_tzinfo

class TestGetDefaultTzinfo:
    """Tests for get_default_tzinfo function."""

    def test_returns_zoneinfo_when_tz_env_var_is_set(self):
        """Test that function returns ZoneInfo from TZ environment variable."""
        with patch.dict(os.environ, {"TZ": "America/New_York"}):
            result = get_default_tzinfo()
            assert isinstance(result, ZoneInfo)
            assert str(result) == "America/New_York"

    def test_returns_zoneinfo_for_different_timezone(self):
        """Test that function handles different timezone strings."""
        with patch.dict(os.environ, {"TZ": "Europe/London"}):
            result = get_default_tzinfo()
            assert isinstance(result, ZoneInfo)
            assert str(result) == "Europe/London"

    def test_falls_back_to_local_tz_when_tz_env_var_not_set(self):
        """Test that function falls back to local timezone when TZ is not set."""
        with patch.dict(os.environ, {}, clear=True):
            if "TZ" in os.environ:
                del os.environ["TZ"]
            result = get_default_tzinfo()
            assert result is not None
            assert isinstance(result, dt.tzinfo)

    def test_falls_back_when_tz_env_var_is_invalid(self):
        """Test that function handles invalid TZ environment variable gracefully."""
        with patch.dict(os.environ, {"TZ": "Invalid/Timezone"}):
            result = get_default_tzinfo()
            assert result is not None
            assert isinstance(result, dt.tzinfo)

    def test_returns_utc_when_local_tz_is_none(self):
        """Test that function returns UTC when local timezone cannot be determined."""
        with patch.dict(os.environ, {}, clear=True):
            if "TZ" in os.environ:
                del os.environ["TZ"]
            
            mock_datetime = MagicMock()
            mock_datetime.astimezone.return_value.tzinfo = None
            
            with patch("lega_soap.timezone.dt.datetime") as mock_dt_class:
                mock_dt_class.now.return_value = mock_datetime
                result = get_default_tzinfo()
                assert result == dt.timezone.utc

    def test_handles_empty_tz_env_var(self):
        """Test that empty TZ environment variable is treated as not set."""
        with patch.dict(os.environ, {"TZ": ""}):
            result = get_default_tzinfo()
            assert result is not None
            assert isinstance(result, dt.tzinfo)
    def test_tz_env_var_takes_precedence_over_local(self):
        """Test that TZ environment variable takes precedence over local timezone."""
        with patch.dict(os.environ, {"TZ": "UTC"}):
            result = get_default_tzinfo()
            assert isinstance(result, ZoneInfo)
            assert str(result) == "UTC"