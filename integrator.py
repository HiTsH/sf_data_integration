from sf_data_integration.connector import Connector
from sf_data_integration.crm_connector import CRMConnector
from sf_data_integration.db_connector import DBConnector
from sf_data_integration.file_connector import FileConnector
from sf_data_integration.logger import setup_logger

class Integrator:
    def __init__(self, source_type, target_system, mapping_file='sf_data_integration/mapping_config.yaml'):
        self.source_type = source_type
        self.target_system = target_system
        self.mapping_file = mapping_file
        self.logger = setup_logger("integrator", log_dir="sf_data_integration/logs")

        self.connector = self.get_connector()

    def get_connector(self):
        """Get the appropriate connector based on the source type."""
        if self.source_type == 'crm':
            return CRMConnector(self.source_type, self.target_system, self.mapping_file)
        elif self.source_type == 'db':
            return DBConnector(self.source_type, self.target_system)
        elif self.source_type == 'file':
            return FileConnector(self.source_type)
        else:
            self.logger.error(f"Unsupported source type: {self.source_type}")
            raise ValueError(f"Unsupported source type: {self.source_type}")

    def integrate(self):
        """Perform the integration."""
        self.connector.migrate()
        self.logger.info("Integration process completed.")
