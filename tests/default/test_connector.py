import pytest
from sf_data_integration import SalesforceConnector, setup_logger

# Replace with mock credentials for testing purposes
SF_CREDENTIALS = {
    "username": "test_username",
    "password": "test_password",
    "security_token": "test_security_token"
}

def test_salesforce_connection():
    """
    Test the initialization of SalesforceConnector to ensure it connects successfully.
    """
    logger = setup_logger("test_project")
    connector = SalesforceConnector(**SF_CREDENTIALS, logger=logger)
    
    # Check if Salesforce object is created
    assert connector.sf is not None, "Failed to establish a Salesforce connection."

def test_insert_records():
    """
    Test record insertion into Salesforce (mocked data).
    """
    logger = setup_logger("test_project")
    connector = SalesforceConnector(**SF_CREDENTIALS, logger=logger)
    mock_data = [{"Name": "Test Account"}]
    
    # Simulate record insertion
    result = connector.insert_records("Account", mock_data)
    
    # Check if insertion result is not empty
    assert result is not None, "Insert operation returned no result."
    assert all('id' in r for r in result), "Inserted records do not have IDs (mock)."
