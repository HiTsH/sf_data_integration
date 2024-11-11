import pytest
from sf_data_integration.connector import SalesforceConnector
import logging

def test_salesforce_connector_init(mocker):
    mocker.patch("simple_salesforce.Salesforce")
    logger = logging.getLogger("test")
    connector = SalesforceConnector("username", "password", "token", logger)
    
    assert connector.sf is not None
    assert connector.logger == logger
