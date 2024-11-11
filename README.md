# sf_data_integration

`sf_data_integration` is a Python package designed to facilitate data migration and integration from various sources (such as files, databases, and CRM systems) into Salesforce. It supports data retrieval, mapping, batching, logging, and tracking of records to ensure efficient and reliable data integration.

## Features

- **Multi-Source Integration**: Retrieve data from CSV files, databases, and CRM systems.
- **Data Mapping**: Map fields from the source data to Salesforce-compatible fields using a customizable configuration.
- **Batch Processing**: Split data into manageable batches for efficient insertion.
- **Tracking and Logging**: Track migrated records to avoid duplication, with detailed logging for monitoring progress and troubleshooting.
- **Salesforce Integration**: Insert data into Salesforce using the Bulk API.

## Project Structure

- `connector.py`: Connects to Salesforce and handles data insertion.
- `crm_connector.py`: Retrieves data from supported CRM systems.
- `file_connector.py`: Reads data from CSV files.
- `db_connector.py`: Connects to databases and executes SQL queries to retrieve data.
- `integrator.py`: Coordinates the end-to-end data integration process.
- `mapper.py`: Maps data fields from the source format to Salesforce-compatible fields.
- `tracker.py`: Tracks migrated records to prevent duplication.
- `batch_processor.py`: Splits data into batches for efficient processing.
- `logger.py`: Configures and manages logging for the package.
- `mapping_config.yaml`: Configurable mappings for fields between source data and Salesforce.
- `examples/example.py`: Example script demonstrating how to use the package.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/sf_data_integration.git
   cd sf_data_integration
   ```
2. **Install Dependencies**
   pip install -r requirements.txt

3. **Environment Variables**
   Set environment variables for Salesforce credentials:
   export SALESFORCE_USERNAME='your_username'
   export SALESFORCE_PASSWORD='your_password'
   export SALESFORCE_SECURITY_TOKEN='your_security_token'

## Configuration

Mapping Configuration
Define field mappings between source data fields and Salesforce fields in mapping_config.yaml. Each Salesforce object (e.g., Account, Contact) can have a customized mapping configuration. For example:
Contact:
source_name: Name
source_email: Email
source_phone: Phone
source_address: MailingAddress

## Usage

Here’s a simple example of how to use sf_data_integration to migrate data from a CSV file to Salesforce.

import os
from sf_data_integration.logger import setup_logger
from sf_data_integration.connector import SalesforceConnector
from sf_data_integration.file_connector import FileConnector
from sf_data_integration.mapper import DataMapper
from sf_data_integration.tracker import DataTracker
from sf_data_integration.batch_processor import BatchProcessor
from sf_data_integration.integrator import DataIntegrator

#Setup logger
logger = setup_logger("sf_data_integration_example", log_dir="log")

#Initialize Salesforce connector with environment credentials
sf_connector = SalesforceConnector(
os.getenv("SALESFORCE_USERNAME"),
os.getenv("SALESFORCE_PASSWORD"),
os.getenv("SALESFORCE_SECURITY_TOKEN"),
logger
)

#Initialize file connector for CSV data
file_connector = FileConnector("path/to/data.csv", logger)

#Initialize data mapper, tracker, and batch processor
data_mapper = DataMapper()
data_tracker = DataTracker("migration_tracking.csv")
batch_processor = BatchProcessor(batch_size=100)

#Initialize data integrator
data_integrator = DataIntegrator(
sf_connector=sf_connector,
data_mapper=data_mapper,
data_tracker=data_tracker,
batch_processor=batch_processor,
logger=logger
)

#Run migration
data_integrator.run_migration(
source="File",
object_name="source_contact",
destination_object="Contact",
data_source_config={"file_path": "path/to/data.csv"}
)

logger.info("Data migration completed.")

## Running Tests

To run tests, navigate to the tests directory and use pytest:
pytest tests/

## Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your_feature).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/your_feature).
Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or issues, please open an issue on GitHub or reach out to the repository owner.
