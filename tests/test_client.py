import datetime as dt
from unittest.mock import Mock, patch, MagicMock
import pytest
from zeep.client import Client as ZeepClient
from zeep.settings import Settings as ZeepSettings
from lega_soap.client import Client
from lega_soap.auth import Credentials

@pytest.fixture
def mock_credentials():
    """Fixture for mock credentials."""
    return Mock(spec=Credentials)


@pytest.fixture
def mock_zeep_client():
    """Fixture for mock Zeep client."""
    mock_client = Mock(spec=ZeepClient)
    mock_client.service = Mock()
    return mock_client


@pytest.fixture
def mock_auth_manager():
    """Fixture for mock AuthManager."""
    with patch('lega_soap.client.AuthManager') as mock:
        yield mock


@pytest.fixture
def mock_customer_service():
    """Fixture for mock CustomerService."""
    with patch('lega_soap.client.CustomerService') as mock:
        yield mock


@pytest.fixture
def mock_get_default_tzinfo():
    """Fixture for mock get_default_tzinfo."""
    with patch('lega_soap.client.get_default_tzinfo') as mock:
        mock.return_value = dt.timezone.utc
        yield mock


class TestClient:
    """Tests for the Client class."""

    def test_init_with_provided_zeep_client(
        self, mock_credentials, mock_zeep_client, mock_auth_manager, 
        mock_customer_service, mock_get_default_tzinfo
    ):
        """Test initialization with a provided Zeep client."""
        client = Client(creds=mock_credentials, zeep_client=mock_zeep_client)
        
        assert client.zeep_client == mock_zeep_client
        mock_auth_manager.assert_called_once_with(mock_zeep_client.service, mock_credentials)
        mock_auth_manager.return_value.authenticate.assert_called_once()

    def test_init_creates_zeep_client_when_not_provided(
        self, mock_credentials, mock_auth_manager, mock_customer_service, 
        mock_get_default_tzinfo
    ):
        """Test initialization creates Zeep client when not provided."""
        with patch('lega_soap.client.ZeepClient') as mock_zeep_class:
            mock_zeep_instance = Mock()
            mock_zeep_instance.service = Mock()
            mock_zeep_class.return_value = mock_zeep_instance
            
            client = Client(creds=mock_credentials)
            
            mock_zeep_class.assert_called_once()
            assert client.zeep_client == mock_zeep_instance

    def test_init_with_custom_wsdl_url(self, mock_credentials, mock_auth_manager, 
                                       mock_customer_service, mock_get_default_tzinfo):
        """Test initialization with custom WSDL URL."""
        custom_url = "https://custom.url/api.wsdl"
        
        with patch('lega_soap.client.ZeepClient') as mock_zeep_class:
            mock_zeep_instance = Mock()
            mock_zeep_instance.service = Mock()
            mock_zeep_class.return_value = mock_zeep_instance
            
            client = Client(creds=mock_credentials, wsdl_url=custom_url)
            
            call_args = mock_zeep_class.call_args
            assert call_args.kwargs['wsdl'] == custom_url

    def test_init_authenticate_on_init_true(
        self, mock_credentials, mock_zeep_client, mock_auth_manager, 
        mock_customer_service, mock_get_default_tzinfo
    ):
        """Test authentication is called when authenticate_on_init is True."""
        client = Client(creds=mock_credentials, zeep_client=mock_zeep_client, 
                       authenticate_on_init=True)
        
        mock_auth_manager.return_value.authenticate.assert_called_once()

    def test_init_authenticate_on_init_false(
        self, mock_credentials, mock_zeep_client, mock_auth_manager, 
        mock_customer_service, mock_get_default_tzinfo
    ):
        """Test authentication is not called when authenticate_on_init is False."""
        client = Client(creds=mock_credentials, zeep_client=mock_zeep_client, 
                       authenticate_on_init=False)
        
        mock_auth_manager.return_value.authenticate.assert_not_called()

    def test_init_with_custom_tzinfo(
        self, mock_credentials, mock_zeep_client, mock_auth_manager, 
        mock_customer_service, mock_get_default_tzinfo
    ):
        """Test initialization with custom timezone info."""
        custom_tz = dt.timezone(dt.timedelta(hours=5))
        
        client = Client(creds=mock_credentials, zeep_client=mock_zeep_client, 
                       tzinfo=custom_tz)
        
        assert client.tzinfo == custom_tz
        mock_get_default_tzinfo.assert_not_called()

    def test_init_uses_default_tzinfo(
        self, mock_credentials, mock_zeep_client, mock_auth_manager, 
        mock_customer_service, mock_get_default_tzinfo
    ):
        """Test initialization uses default timezone when not provided."""
        client = Client(creds=mock_credentials, zeep_client=mock_zeep_client)
        
        assert client.tzinfo == dt.timezone.utc
        mock_get_default_tzinfo.assert_called_once()

    def test_customer_service_initialized(
        self, mock_credentials, mock_zeep_client, mock_auth_manager, 
        mock_customer_service, mock_get_default_tzinfo
    ):
        """Test CustomerService is properly initialized."""
        client = Client(creds=mock_credentials, zeep_client=mock_zeep_client)
        
        mock_customer_service.assert_called_once_with(
            mock_zeep_client.service,
            mock_auth_manager.return_value,
            dt.timezone.utc
        )
        assert client.customers == mock_customer_service.return_value

    def test_zeep_settings_configuration(self, mock_credentials, mock_auth_manager, 
                                         mock_customer_service, mock_get_default_tzinfo):
        """Test Zeep settings are configured correctly."""
        with patch('lega_soap.client.ZeepSettings') as mock_settings_class, \
             patch('lega_soap.client.ZeepClient') as mock_zeep_class:
            mock_zeep_instance = Mock()
            mock_zeep_instance.service = Mock()
            mock_zeep_class.return_value = mock_zeep_instance
            
            client = Client(creds=mock_credentials)
            
            mock_settings_class.assert_called_once_with(strict=False, xml_huge_tree=True)