import pytest
from sf_data_integration.crm_connector import CRMConnector
import logging

def test_crm_connector_init():
    logger = logging.getLogger("test")
    connection_params = {"api_key": "dummy_key"}
    connector = CRMConnector("HubSpot", connection_params, logger)
    
    assert connector.crm_name == "HubSpot"
    assert connector.connection_params == connection_params
    assert connector.logger == logger
