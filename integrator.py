from typing import List, Dict, Any
import logging

from .connector import SalesforceConnector
from .crm_connector import CRMConnector
from .file_connector import FileConnector
from .db_connector import DBConnector
from .mapper import DataMapper
from .tracker import DataTracker
from .batch_processor import BatchProcessor

class DataIntegrator:
    """
    Coordinates data integration from various sources (CRM, file, database) to Salesforce.
    """

    def __init__(self, sf_connector: SalesforceConnector, data_mapper: DataMapper, 
                 data_tracker: DataTracker, batch_processor: BatchProcessor, logger: logging.Logger):
        self.sf_connector = sf_connector
        self.data_mapper = data_mapper
        self.data_tracker = data_tracker
        self.batch_processor = batch_processor
        self.logger = logger

    def run_migration(self, source: str, object_name: str, destination_object: str, 
                      data_source_config: Dict[str, Any]) -> None:
        """
        Manages data migration from CRM, file, or database to Salesforce.

        :param source: Type of data source ('CRM', 'File', or 'Database').
        :param object_name: CRM or database table name.
        :param destination_object: Salesforce object for data migration.
        :param data_source_config: Configuration for data source.
        """
        # Select source connector based on input
        if source == "CRM":
            connector = CRMConnector(data_source_config['crm_type'], data_source_config['config'], self.logger)
            data = connector.retrieve_data(object_name)
        elif source == "File":
            connector = FileConnector(data_source_config['file_path'], self.logger)
            data = connector.retrieve_data()
        elif source == "Database":
            connector = DBConnector(data_source_config['db_url'], self.logger)
            data = connector.retrieve_data(data_source_config['query'])
        else:
            self.logger.error("Invalid data source specified.")
            return

        # Process data for migration
        data_to_migrate = [record for record in data if not self.data_tracker.is_migrated(self.data_tracker.generate_hash(record))]
        mapped_data = [self.data_mapper.map_record(record) for record in data_to_migrate]
        batched_data = self.batch_processor.batch_data(mapped_data)

        # Insert into Salesforce
        for batch in batched_data:
            self.sf_connector.insert_records(destination_object, batch)
            for record in batch:
                self.data_tracker.track_migration(self.data_tracker.generate_hash(record))
        self.data_tracker.save_tracking()
        self.logger.info("Data migration completed.")
