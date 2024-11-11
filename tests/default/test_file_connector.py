import pytest
from sf_data_integration.file_connector import FileConnector
import logging
import pandas as pd

def test_file_connector_init(tmp_path):
    logger = logging.getLogger("test")
    file_path = tmp_path / "test.csv"
    df = pd.DataFrame({"column1": [1, 2, 3]})
    df.to_csv(file_path, index=False)
    
    connector = FileConnector(str(file_path), logger)
    assert connector.file_path == str(file_path)
    assert connector.logger == logger

def test_file_connector_retrieve_data(tmp_path):
    logger = logging.getLogger("test")
    file_path = tmp_path / "test.csv"
    pd.DataFrame({"column1": [1, 2, 3]}).to_csv(file_path, index=False)
    
    connector = FileConnector(str(file_path), logger)
    data = connector.retrieve_data()
    assert data == [{"column1": 1}, {"column1": 2}, {"column1": 3}]
