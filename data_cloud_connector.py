from sf_data_integration.logger import setup_logger

class DataCloudConnector:
    def __init__(self, salesforce_client):
        self.salesforce_client = salesforce_client
        self.logger = setup_logger("data_cloud_connector", log_dir="sf_data_integration/logs")

    def insert_data(self, data):
        """Insert data into Salesforce Data Cloud."""
        try:
            # Hypothetical logic to insert data into Salesforce Data Cloud
            self.salesforce_client.insert_records(data)
            self.logger.info(f"Successfully inserted {len(data)} records into Salesforce Data Cloud.")
        except Exception as e:
            self.logger.error(f"Error inserting data into Salesforce Data Cloud: {e}")
            raise
