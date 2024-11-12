import pytest
from sf_data_integration.db_connector import DBConnector

@pytest.fixture
def db_connector():
    return DBConnector(connection_string="Database_Connection_String")

def test_db_connector_initialization(db_connector):
    assert db_connector.connection_string == "Database_Connection_String"

def test_db_connector_connect(db_connector, mocker):
    mock_connect = mocker.patch.object(db_connector, 'connect', return_value=True)
    assert db_connector.connect() is True
    mock_connect.assert_called_once()
