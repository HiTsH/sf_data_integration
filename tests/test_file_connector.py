import pytest
from sf_data_integration.file_connector import FileConnector

@pytest.fixture
def file_connector():
    return FileConnector(file_path="sample_data.csv")

def test_file_connector_initialization(file_connector):
    assert file_connector.file_path == "sample_data.csv"

def test_file_connector_read_data(file_connector, mocker):
    mock_read = mocker.patch.object(file_connector, 'read_data', return_value=[{'field1': 'value1'}])
    data = file_connector.read_data()
    assert len(data) > 0
    mock_read.assert_called_once()
