import pytest
from sf_data_integration.db_connector import DBConnector
import logging

def test_db_connector_init(mocker):
    mock_engine = mocker.patch("sqlalchemy.create_engine")
    logger = logging.getLogger("test")
    connector = DBConnector("sqlite:///:memory:", logger)
    
    assert connector.engine == mock_engine.return_value
    assert connector.logger == logger
