from simple_salesforce import Salesforce
from typing import List, Dict, Any
import logging

class SalesforceConnector:
    def __init__(self, username: str, password: str, security_token: str, logger: logging.Logger):
        """
        Initialize the Salesforce connection and logger.
        """
        self.sf = Salesforce(username=username, password=password, security_token=security_token)
        self.logger = logger

    def insert_records(self, object_name: str, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Insert records into Salesforce for a specified object.

        :param object_name: Salesforce object name (e.g., 'Contact', 'Account')
        :param data: List of records as dictionaries.
        :return: Response from Salesforce API.
        """
        try:
            result = self.sf.bulk.__getattr__(object_name).insert(data)
            self.logger.info(f"Inserted {len(data)} records into {object_name}.")
            return result
        except Exception as e:
            self.logger.error(f"Failed to insert records: {e}")
            return []
