from sf_data_integration.connector import SalesforceConnector
from sf_data_integration.data_cloud_connector import DataCloudConnector
from sf_data_integration.integrator import DataIntegrator
from sf_data_integration.logger import setup_logger
from sf_data_integration.mapper import DataMapper
from sf_data_integration.tracker import DataTracker
from sf_data_integration.batch_processor import BatchProcessor
from sf_data_integration.file_connector import FileConnector

# Setup logger
logger = setup_logger("sf_data_integration_project", log_dir="log", compliance_mode=True)

# Initialize connectors and components
sf_connector = SalesforceConnector(access_token="YOUR_ACCESS_TOKEN", instance_url="https://instance.salesforce.com", logger=logger)
data_cloud_connector = DataCloudConnector(access_token="YOUR_ACCESS_TOKEN", instance_url="https://instance.salesforce.com", logger=logger)
data_mapper = DataMapper("mapping_config.yaml")
data_tracker = DataTracker()
batch_processor = BatchProcessor(batch_size=200)

# Initialize DataIntegrator
integrator = DataIntegrator(
    sf_connector=sf_connector,
    data_mapper=data_mapper,
    data_tracker=data_tracker,
    batch_processor=batch_processor,
    data_cloud_connector=data_cloud_connector,
    logger=logger
)

# Run data migration from file to Salesforce
file_connector = FileConnector(file_path="path/to/data.csv", logger=logger)
data_source_config = {"file_path": "path/to/data.csv", "segment_id": "12345"}

integrator.run_migration(source="File", object_name="Contact", destination_object="Contact", data_source_config=data_source_config, activate_segment=True)
