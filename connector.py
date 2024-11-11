from simple_salesforce import Salesforce
from typing import List, Dict, Any
import logging

class SalesforceConnector:
    def __init__(self, username: str, password: str, security_token: str, logger: logging.Logger):
        """
        Initialize the Salesforce connection and logger.

        :param username: Salesforce username.
        :param password: Salesforce password.
        :param security_token: Salesforce security token.
        :param logger: A configured logger instance for logging events and errors.
        """
        try:
            self.sf = Salesforce(username=username, password=password, security_token=security_token)
            self.logger = logger
            self.logger.info("Salesforce connection established successfully.")
        except Exception as e:
            self.logger.error(f"Failed to connect to Salesforce: {e}")

    def insert_records(self, object_name: str, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Insert records into Salesforce for a specified object.

        :param object_name: Salesforce object name (e.g., 'Contact', 'Account')
        :param data: List of records as dictionaries.
        :return: A list of responses from Salesforce for each inserted record.
        """
        self.logger.info(f"Inserting {len(data)} records into Salesforce object '{object_name}'.")
        try:
            # Use Salesforce Bulk API for efficient data insertion
            result = self.sf.bulk.__getattr__(object_name).insert(data)
            self.logger.info(f"Inserted {len(data)} records into {object_name}.")
            return result
        except Exception as e:
            # Log error and return an empty list if insertion fails
            self.logger.error(f"Failed to insert records: {e}")
            return []
    
    def __repr__(self):
        return "SalesforceConnector(username, password, security_token, logger)"
