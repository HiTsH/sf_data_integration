import os
from sf_data_integration.logger import setup_logger
from sf_data_integration.connector import SalesforceConnector
from sf_data_integration.file_connector import FileConnector
from sf_data_integration.mapper import DataMapper
from sf_data_integration.tracker import DataTracker
from sf_data_integration.batch_processor import BatchProcessor
from sf_data_integration.integrator import DataIntegrator

# Configure logger for the example run
logger = setup_logger("sf_data_integration_example", log_dir="log")

# Salesforce connection details (replace with environment variables or secure storage)
username = os.getenv("SALESFORCE_USERNAME", "your_username")
password = os.getenv("SALESFORCE_PASSWORD", "your_password")
security_token = os.getenv("SALESFORCE_SECURITY_TOKEN", "your_security_token")

# Initialize Salesforce connector
sf_connector = SalesforceConnector(username, password, security_token, logger)

# Initialize File connector for CSV data source
file_connector = FileConnector("path/to/your/data.csv", logger)

# Initialize Data Mapper and Tracker for data mapping and tracking
data_mapper = DataMapper()
data_tracker = DataTracker(tracking_file="migration_tracking.csv")

# Initialize Batch Processor to handle batch data processing
batch_processor = BatchProcessor(batch_size=100)

# Initialize Data Integrator with all components
data_integrator = DataIntegrator(
    sf_connector=sf_connector,
    data_mapper=data_mapper,
    data_tracker=data_tracker,
    batch_processor=batch_processor,
    logger=logger
)

# Define the data source configuration for file-based migration
data_source_config = {
    "file_path": "path/to/your/data.csv",
}

# Run migration from CSV file source to Salesforce "Contact" object
data_integrator.run_migration(
    source="File",
    object_name="source_contact",      # This is the source data identifier; e.g., CSV headers
    destination_object="Contact",      # Destination object in Salesforce
    data_source_config=data_source_config
)

# Log completion
logger.info("Example data migration from CSV to Salesforce completed successfully.")
