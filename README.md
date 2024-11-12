# sf_data_integration

`sf_data_integration` is a Python package designed to streamline the process of integrating and migrating data from various sources into Salesforce and Salesforce Data Cloud. The package supports integration with CRM systems, databases, files, and more, offering a comprehensive set of tools for seamless data migration.

## Features

- **Salesforce Integration**: Easily connect to Salesforce and perform data migration tasks.
- **Salesforce Data Cloud Integration**: Full support for Salesforce Data Cloud, allowing data to be migrated, processed, and managed efficiently.
- **Support for Various Data Sources**: Integrates data from CRMs, databases, and files like CSV, Excel, and others.
- **Batch Processing**: Efficiently process large datasets in batches.
- **Data Tracking**: Use hashes to track data migration status and ensure the integrity of the migration process.
- **Logging**: Detailed logging to monitor the status of the integration process.
- **Customizable Mappings**: Map data from source systems to Salesforce using flexible mapping configurations.

## Installation

To install the `sf_data_integration` package, you can use `pip`:

```bash
pip install sf_data_integration
```

Alternatively, you can install it directly from the repository:

```bash
git clone https://github.com/yourusername/sf_data_integration.git
cd sf_data_integration
pip install .
```

## Requirements

Python 3.6 or higher
The following libraries are required:
pandas==2.1.1
simple-salesforce==1.11.4
pytest==7.4.0
PyYAML==6.0
requests==2.28.2
python-dotenv==1.0.0
boto3==1.26.8
google-cloud==0.34.0
sqlalchemy==2.1.0
psycopg2==2.9.3
openpyxl==3.1.1
loguru==0.6.0
These dependencies are listed in requirements.txt, and you can install them via:

```bash
pip install -r requirements.txt
```

## Configuration

Before using the package, you may need to configure the following:

1. **Salesforce Credentials:** Use environment variables or a .env file to store your Salesforce credentials. Here is an example of the .env file:

```bash
SF_USERNAME=your_salesforce_username
SF_PASSWORD=your_salesforce_password
SF_SECURITY_TOKEN=your_salesforce_security_token
```

2. **Mapping Configuration:** Use the mapping_config.yaml file to define data mappings between your source and Salesforce fields. Below is an example of the configuration:

```yaml
mappings:
  crm_to_sf:
    - source_field: "crm_name"
      destination_field: "Salesforce_Account_Name"
    - source_field: "crm_email"
      destination_field: "Salesforce_Contact_Email"
  db_to_sf:
    - source_field: "db_field_1"
      destination_field: "Salesforce_Field_1"
```

This configuration can be adjusted according to your specific data structure and Salesforce schema.

## Usage

### Salesforce Integration

To connect to Salesforce and upload data, you can use the SalesforceConnector class. Here's an example:

```python
from sf_data_integration import SalesforceConnector

# Initialize the connector
connector = SalesforceConnector()

# Fetch data from Salesforce
sf_data = connector.get_data("SELECT Id, Name FROM Account")

# Upload data to Salesforce
connector.upload_data("Account", sf_data)
```

### CRM Integration

If you're integrating data from a CRM system (e.g., Salesforce, HubSpot), you can use the CRMConnector. Example:

```python
from sf_data_integration import CRMConnector

# Initialize CRM connector
crm_connector = CRMConnector(crm_type="Salesforce")

# Fetch CRM data
crm_data = crm_connector.get_data("SELECT Id, Name FROM Lead")

# Process and map data to Salesforce
crm_connector.upload_data_to_salesforce(crm_data)
```

### Data Cloud Integration

For integrating with Salesforce Data Cloud, you can use the DataCloudConnector:

```python
from sf_data_integration import DataCloudConnector

# Initialize Data Cloud connector
data_cloud_connector = DataCloudConnector()

# Upload data to Salesforce Data Cloud
data_cloud_connector.upload_data(data)
```

### Data Processing in Batches

Use BatchProcessor to handle large datasets in manageable chunks:

```python
from sf_data_integration import BatchProcessor

# Initialize the batch processor
batch_processor = BatchProcessor(batch_size=100)

# Sample data
data = [{"field1": "value1"}, {"field2": "value2"}, {"field3": "value3"}]

# Process the data in batches
batch_processor.process_batches(data)
```

### Data Mapping

Use the DataMapper class to map source fields to Salesforce fields:

```python
from sf_data_integration import DataMapper

# Initialize the mapper with a configuration file
mapper = DataMapper(config_file="path/to/mapping_config.yaml")

# Map source data
mapped_data = mapper.map_data(source_data)
```

### Logging

The package uses logging for debugging and process tracking. Logs are stored in the logs/ directory. Example:

```python
from sf_data_integration import setup_logger

# Set up logger
logger = setup_logger("integration_process", log_dir="logs")

# Log an informational message
logger.info("Data migration started.")
```

### Error Handling

In case of errors, the package will log detailed messages and exceptions. The logs can be reviewed for troubleshooting.

### Testing

To ensure the functionality of the package, you can run the tests using pytest:

```bash
pytest
```

Tests are located in the tests/ directory and cover various components like connectors, batch processing, and data integration.

### Contributing

If you'd like to contribute to sf_data_integration, feel free to fork the repository, create a branch, and submit a pull request. Ensure that tests are included for any new features or bug fixes.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
