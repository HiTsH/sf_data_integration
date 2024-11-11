import pandas as pd
from typing import List, Dict, Any
import logging

class FileConnector:
    """
    Reads data from file sources, such as CSV or Excel.
    """

    def __init__(self, file_path: str, logger: logging.Logger):
        """
        Initializes FileConnector.

        :param file_path: Path to the file.
        :param logger: Logger instance for recording events.
        """
        self.file_path = file_path
        self.logger = logger
        self.logger.info(f"FileConnector initialized for file: {file_path}")

    def retrieve_data(self) -> List[Dict[str, Any]]:
        """
        Reads data from a file into a list of dictionaries.

        :return: List of records.
        """
        self.logger.info(f"Reading data from file: {self.file_path}")
        try:
            df = pd.read_csv(self.file_path)
            return df.to_dict(orient="records")
        except Exception as e:
            self.logger.error(f"Failed to read data from file: {e}")
            return []
