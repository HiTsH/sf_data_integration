from typing import Dict, Any
import yaml

class DataMapper:
    """
    DataMapper handles mapping data fields from source to Salesforce-compatible formats.
    """

    def __init__(self):
        with open("mapping_config.yaml", 'r') as file:
            self.mapping_config = yaml.safe_load(file)

    def map_record(self, record: Dict[str, Any], target_object: str) -> Dict[str, Any]:
        """
        Map data fields to match Salesforce's requirements.

        :param record: A single record from the source.
        :param target_object: Salesforce target object (e.g., 'Contact').
        :return: Mapped record ready for Salesforce insertion.
        """
        mapped_record = {self.mapping_config[target_object].get(k, k): v for k, v in record.items()}
        return mapped_record
