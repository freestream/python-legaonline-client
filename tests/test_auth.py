import pytest
from unittest.mock import Mock, MagicMock
from lega_soap.auth import Credentials, AuthManager
from lega_soap.exceptions import AuthError

class TestCredentials:
    def test_credentials_creation(self):
        creds = Credentials(user_id=123, hash="test_hash")
        assert creds.user_id == 123
        assert creds.hash == "test_hash"

    def test_credentials_frozen(self):
        creds = Credentials(user_id=123, hash="test_hash")
        with pytest.raises(AttributeError):
            creds.user_id = 456


class TestAuthManager:
    @pytest.fixture
    def mock_service(self):
        return Mock()

    @pytest.fixture
    def credentials(self):
        return Credentials(user_id=123, hash="test_hash")

    @pytest.fixture
    def auth_manager(self, mock_service, credentials):
        return AuthManager(mock_service, credentials)

    def test_init(self, auth_manager, mock_service, credentials):
        assert auth_manager._service == mock_service
        assert auth_manager._creds == credentials
        assert auth_manager._token is None

    def test_token_property_raises_when_not_initialized(self, auth_manager):
        with pytest.raises(AuthError, match="Auth token not initialized"):
            _ = auth_manager.token

    def test_token_property_returns_token(self, auth_manager):
        auth_manager._token = "test_token"
        assert auth_manager.token == "test_token"

    def test_authenticate_success(self, auth_manager, mock_service):
        mock_service.GetAuthToken.return_value = "new_token"
        
        token = auth_manager.authenticate()
        
        assert token == "new_token"
        assert auth_manager._token == "new_token"
        mock_service.GetAuthToken.assert_called_once_with(123, "test_hash")

    def test_authenticate_service_exception(self, auth_manager, mock_service):
        mock_service.GetAuthToken.side_effect = Exception("Service error")
        
        with pytest.raises(AuthError, match="GetAuthToken failed: Service error"):
            auth_manager.authenticate()

    def test_authenticate_empty_token(self, auth_manager, mock_service):
        mock_service.GetAuthToken.return_value = ""
        
        with pytest.raises(AuthError, match="GetAuthToken returned empty token"):
            auth_manager.authenticate()

    def test_authenticate_none_token(self, auth_manager, mock_service):
        mock_service.GetAuthToken.return_value = None
        
        with pytest.raises(AuthError, match="GetAuthToken returned empty token"):
            auth_manager.authenticate()

    def test_validate_no_token(self, auth_manager):
        assert auth_manager.validate() is False

    def test_validate_success(self, auth_manager, mock_service):
        auth_manager._token = "valid_token"
        mock_service.ValidateAuthToken.return_value = True
        
        assert auth_manager.validate() is True
        mock_service.ValidateAuthToken.assert_called_once_with("valid_token")

    def test_validate_failure(self, auth_manager, mock_service):
        auth_manager._token = "invalid_token"
        mock_service.ValidateAuthToken.return_value = False
        
        assert auth_manager.validate() is False

    def test_validate_exception(self, auth_manager, mock_service):
        auth_manager._token = "token"
        mock_service.ValidateAuthToken.side_effect = Exception("Validation error")
        
        assert auth_manager.validate() is False

    def test_ensure_valid_token_no_token(self, auth_manager, mock_service):
        mock_service.GetAuthToken.return_value = "new_token"
        
        token = auth_manager.ensure_valid_token()
        
        assert token == "new_token"
        assert auth_manager._token == "new_token"

    def test_ensure_valid_token_valid_existing(self, auth_manager, mock_service):
        auth_manager._token = "existing_token"
        mock_service.ValidateAuthToken.return_value = True
        
        token = auth_manager.ensure_valid_token()
        
        assert token == "existing_token"
        mock_service.GetAuthToken.assert_not_called()

    def test_ensure_valid_token_invalid_existing(self, auth_manager, mock_service):
        auth_manager._token = "old_token"
        mock_service.ValidateAuthToken.return_value = False
        mock_service.GetAuthToken.return_value = "new_token"
        
        token = auth_manager.ensure_valid_token()
        
        assert token == "new_token"
        assert auth_manager._token == "new_token"
        mock_service.GetAuthToken.assert_called_once_with(123, "test_hash")