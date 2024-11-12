import pytest
from sf_data_integration.connector import Connector

@pytest.fixture
def connector():
    return Connector(api_url="https://api.salesforce.com", auth_token="dummy_token")

def test_connector_initialization(connector):
    assert connector.api_url == "https://api.salesforce.com"
    assert connector.auth_token == "dummy_token"

def test_connector_get_data(connector, mocker):
    # Mock the actual API call
    mock_response = {"data": [{"id": 1, "name": "Test Record"}]}
    mocker.patch.object(connector, 'get_data', return_value=mock_response)

    data = connector.get_data()
    assert data == mock_response
    assert "data" in data
    assert len(data["data"]) > 0
