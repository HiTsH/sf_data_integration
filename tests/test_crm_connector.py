import pytest
from sf_data_integration.crm_connector import CRMConnector

@pytest.fixture
def crm_connector():
    return CRMConnector(crm_url="https://crm.example.com", api_key="api_key")

def test_crm_connector_initialization(crm_connector):
    assert crm_connector.crm_url == "https://crm.example.com"
    assert crm_connector.api_key == "api_key"

def test_crm_connector_fetch_data(crm_connector, mocker):
    mock_fetch_data = mocker.patch.object(crm_connector, 'fetch_data', return_value={"data": []})
    data = crm_connector.fetch_data()
    assert "data" in data
    mock_fetch_data.assert_called_once()
