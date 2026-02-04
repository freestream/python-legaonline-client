import datetime as dt
from unittest.mock import Mock, patch, MagicMock
import pytest
from lega_soap.services.base import BaseService
from lega_soap.exceptions import ServiceError

class TestBaseService:
    @pytest.fixture
    def mock_service(self):
        """Create a mock SOAP service."""
        return Mock()

    @pytest.fixture
    def mock_auth(self):
        """Create a mock authentication manager."""
        auth = Mock()
        auth.ensure_valid_token.return_value = "mock_token_123"
        return auth

    @pytest.fixture
    def tzinfo(self):
        """Create a timezone info object."""
        return dt.timezone.utc

    @pytest.fixture
    def base_service(self, mock_service, mock_auth, tzinfo):
        """Create a BaseService instance."""
        return BaseService(mock_service, mock_auth, tzinfo)

    def test_init(self, mock_service, mock_auth, tzinfo):
        """Test BaseService initialization."""
        service = BaseService(mock_service, mock_auth, tzinfo)
        assert service._service == mock_service
        assert service._auth == mock_auth
        assert service._tzinfo == tzinfo

    @patch('lega_soap.services.base.serialize_object')
    @patch('lega_soap.services.base.sanitize_object')
    def test_call_success(self, mock_sanitize, mock_serialize, base_service, mock_service, mock_auth):
        """Test successful SOAP method call."""
        mock_method = Mock(return_value="soap_result")
        mock_service.test_method = mock_method
        mock_serialize.return_value = "serialized_result"
        mock_sanitize.return_value = "sanitized_result"

        result = base_service._call("test_method", "arg1", kwarg1="value1")

        mock_auth.ensure_valid_token.assert_called_once()
        mock_method.assert_called_once_with("mock_token_123", "arg1", kwarg1="value1")
        mock_serialize.assert_called_once_with("soap_result")
        mock_sanitize.assert_called_once_with("serialized_result", dt.timezone.utc)
        assert result == "sanitized_result"

    @patch('lega_soap.services.base.serialize_object')
    @patch('lega_soap.services.base.sanitize_object')
    def test_call_filters_empty_kwargs(self, mock_sanitize, mock_serialize, base_service, mock_service):
        """Test that empty values in kwargs are filtered out."""
        mock_method = Mock(return_value="result")
        mock_service.test_method = mock_method
        mock_serialize.return_value = "serialized"
        mock_sanitize.return_value = "sanitized"

        base_service._call(
            "test_method",
            valid="value",
            none_val=None,
            empty_str="",
            empty_list=[],
            empty_dict={},
            empty_tuple=(),
            keep_this="keep"
        )

        mock_method.assert_called_once_with("mock_token_123", valid="value", keep_this="keep")

    @patch('lega_soap.services.base.serialize_object')
    @patch('lega_soap.services.base.sanitize_object')
    def test_call_method_execution_fails(self, mock_sanitize, mock_serialize, base_service, mock_service):
        """Test ServiceError is raised when SOAP method execution fails."""
        mock_method = Mock(side_effect=Exception("SOAP error"))
        mock_service.test_method = mock_method

        with pytest.raises(ServiceError, match="test_method failed: SOAP error"):
            base_service._call("test_method")

    @patch('lega_soap.services.base.serialize_object')
    @patch('lega_soap.services.base.sanitize_object')
    def test_call_with_args_and_kwargs(self, mock_sanitize, mock_serialize, base_service, mock_service):
        """Test SOAP method call with both positional and keyword arguments."""
        mock_method = Mock(return_value="result")
        mock_service.complex_method = mock_method
        mock_serialize.return_value = "serialized"
        mock_sanitize.return_value = "sanitized"

        base_service._call("complex_method", "arg1", "arg2", key1="val1", key2="val2")

        mock_method.assert_called_once_with("mock_token_123", "arg1", "arg2", key1="val1", key2="val2")

    def test_call_ensures_valid_token(self, base_service, mock_auth, mock_service):
        """Test that authentication token is ensured before method call."""
        mock_method = Mock(return_value="result")
        mock_service.test_method = mock_method

        with patch('lega_soap.services.base.serialize_object'), \
             patch('lega_soap.services.base.sanitize_object'):
            base_service._call("test_method")

        mock_auth.ensure_valid_token.assert_called_once()