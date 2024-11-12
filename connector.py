from sf_data_integration.logger import setup_logger
from sf_data_integration.mapper import DataMapper
from sf_data_integration.data_cloud_connector import DataCloudConnector
import logging

class Connector:
    def __init__(self, source_system, target_system, mapping_file='sf_data_integration/mapping_config.yaml'):
        self.source_system = source_system
        self.target_system = target_system
        self.mapping_file = mapping_file
        self.logger = setup_logger("connector", log_dir="sf_data_integration/logs")
        self.mapper = DataMapper(self.mapping_file)

    def fetch_data(self):
        """Fetch data from the source system."""
        data = self.source_system.get_data()
        self.logger.info(f"Fetched {len(data)} records from source system.")
        return data

    def map_data(self, data):
        """Map the fetched data to the target system's format using DataMapper."""
        try:
            mapped_data = self.mapper.map_data(data, self.target_system)
            self.logger.info(f"Mapped {len(mapped_data)} records to target system format.")
            return mapped_data
        except Exception as e:
            self.logger.error(f"Error during mapping: {e}")
            raise

    def migrate(self):
        """Perform the migration from source to target system."""
        data = self.fetch_data()
        mapped_data = self.map_data(data)
        self.target_system.insert_data(mapped_data)
        self.logger.info("Migration completed.")
