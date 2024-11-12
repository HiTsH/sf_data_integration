from sf_data_integration.logger import setup_logger
from sf_data_integration.mapper import DataMapper

class CRMConnector:
    def __init__(self, crm_client, target_system, mapping_file='sf_data_integration/mapping_config.yaml'):
        self.crm_client = crm_client
        self.target_system = target_system
        self.mapping_file = mapping_file
        self.logger = setup_logger("crm_connector", log_dir="sf_data_integration/logs")
        self.mapper = DataMapper(self.mapping_file)

    def fetch_data(self):
        """Fetch data from CRM."""
        data = self.crm_client.get_data()
        self.logger.info(f"Fetched {len(data)} records from CRM system.")
        return data

    def map_data(self, data):
        """Map CRM data to target system format."""
        try:
            mapped_data = self.mapper.map_data(data, self.target_system)
            self.logger.info(f"Mapped {len(mapped_data)} records to target system format.")
            return mapped_data
        except Exception as e:
            self.logger.error(f"Error during mapping: {e}")
            raise

    def migrate(self):
        """Perform the migration of CRM data to the target system."""
        data = self.fetch_data()
        mapped_data = self.map_data(data)
        self.target_system.insert_data(mapped_data)
        self.logger.info("CRM data migration completed.")
