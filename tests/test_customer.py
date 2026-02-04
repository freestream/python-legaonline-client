import datetime as dt
from unittest.mock import Mock, MagicMock
import pytest
from lega_soap.services.customer import CustomerService
from lega_soap.query import FilterSpec, SortSpec

@pytest.fixture
def mock_zeep_service():
    """Fixture for mocked ZEEP service."""
    return Mock()


@pytest.fixture
def mock_auth_manager():
    """Fixture for mocked auth manager."""
    return Mock()


@pytest.fixture
def mock_tzinfo():
    """Fixture for mocked timezone info."""
    return dt.timezone.utc


@pytest.fixture
def customer_service(mock_zeep_service, mock_auth_manager, mock_tzinfo):
    """Fixture for CustomerService instance."""
    return CustomerService(mock_zeep_service, mock_auth_manager, mock_tzinfo)


class TestCustomerService:
    """Test suite for CustomerService class."""

    def test_init(self, mock_zeep_service, mock_auth_manager, mock_tzinfo):
        """Test CustomerService initialization."""
        service = CustomerService(mock_zeep_service, mock_auth_manager, mock_tzinfo)
        assert service is not None

    def test_get_customer_no_params(self, customer_service, monkeypatch):
        """Test get_customer with no optional parameters."""
        mock_call = Mock(return_value=Mock())
        monkeypatch.setattr(customer_service, '_call', mock_call)

        result = customer_service.get_customer()

        mock_call.assert_called_once_with("GetCustomer", "", "", False)
        assert result is not None

    def test_get_customer_with_sorting(self, customer_service, monkeypatch):
        """Test get_customer with sorting parameter."""
        mock_call = Mock(return_value=Mock())
        monkeypatch.setattr(customer_service, '_call', mock_call)
        
        mock_sorting = Mock(spec=SortSpec)
        mock_sorting.to_xml.return_value = "<sort>xml</sort>"

        result = customer_service.get_customer(sorting=mock_sorting)

        mock_sorting.to_xml.assert_called_once()
        mock_call.assert_called_once_with("GetCustomer", "<sort>xml</sort>", "", False)
        assert result is not None

    def test_get_customer_with_filtering(self, customer_service, monkeypatch):
        """Test get_customer with filtering parameter."""
        mock_call = Mock(return_value=Mock())
        monkeypatch.setattr(customer_service, '_call', mock_call)
        
        mock_filtering = Mock(spec=FilterSpec)
        mock_filtering.to_xml.return_value = "<filter>xml</filter>"

        result = customer_service.get_customer(filtering=mock_filtering)

        mock_filtering.to_xml.assert_called_once()
        mock_call.assert_called_once_with("GetCustomer", "", "<filter>xml</filter>", False)
        assert result is not None

    def test_get_customer_with_include_attributes(self, customer_service, monkeypatch):
        """Test get_customer with include_attributes flag."""
        mock_call = Mock(return_value=Mock())
        monkeypatch.setattr(customer_service, '_call', mock_call)

        result = customer_service.get_customer(include_attributes=True)

        mock_call.assert_called_once_with("GetCustomer", "", "", True)
        assert result is not None

    def test_get_customer_with_all_params(self, customer_service, monkeypatch):
        """Test get_customer with all optional parameters."""
        mock_call = Mock(return_value=Mock())
        monkeypatch.setattr(customer_service, '_call', mock_call)
        
        mock_sorting = Mock(spec=SortSpec)
        mock_sorting.to_xml.return_value = "<sort>xml</sort>"
        
        mock_filtering = Mock(spec=FilterSpec)
        mock_filtering.to_xml.return_value = "<filter>xml</filter>"

        result = customer_service.get_customer(
            sorting=mock_sorting,
            filtering=mock_filtering,
            include_attributes=True
        )

        mock_sorting.to_xml.assert_called_once()
        mock_filtering.to_xml.assert_called_once()
        mock_call.assert_called_once_with(
            "GetCustomer", 
            "<sort>xml</sort>", 
            "<filter>xml</filter>", 
            True
        )
        assert result is not None

    def test_get_customer_sorting_none_returns_empty_string(self, customer_service, monkeypatch):
        """Test that None sorting parameter converts to empty string."""
        mock_call = Mock(return_value=Mock())
        monkeypatch.setattr(customer_service, '_call', mock_call)

        customer_service.get_customer(sorting=None)

        args = mock_call.call_args[0]
        assert args[1] == ""

    def test_get_customer_filtering_none_returns_empty_string(self, customer_service, monkeypatch):
        """Test that None filtering parameter converts to empty string."""
        mock_call = Mock(return_value=Mock())
        monkeypatch.setattr(customer_service, '_call', mock_call)

        customer_service.get_customer(filtering=None)

        args = mock_call.call_args[0]
        assert args[2] == ""