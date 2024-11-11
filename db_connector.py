import pandas as pd
from typing import List, Dict, Any
import logging
import sqlalchemy

class DBConnector:
    """
    Retrieves data from a database source using SQLAlchemy.
    """

    def __init__(self, db_url: str, logger: logging.Logger):
        """
        Initializes DBConnector.

        :param db_url: Database connection URL.
        :param logger: Logger instance for recording events.
        """
        self.engine = sqlalchemy.create_engine(db_url)
        self.logger = logger
        self.logger.info(f"DBConnector initialized for database: {db_url}")

    def retrieve_data(self, query: str) -> List[Dict[str, Any]]:
        """
        Executes a query and returns data as a list of dictionaries.

        :param query: SQL query to execute.
        :return: List of records.
        """
        self.logger.info(f"Executing query: {query}")
        try:
            df = pd.read_sql(query, self.engine)
            return df.to_dict(orient="records")
        except Exception as e:
            self.logger.error(f"Failed to retrieve data: {e}")
            return []
