from sf_data_integration.logger import setup_logger
import csv

class FileConnector:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = setup_logger("file_connector", log_dir="sf_data_integration/logs")

    def read_data(self):
        """Read data from a CSV file."""
        try:
            with open(self.file_path, mode='r') as file:
                data = list(csv.DictReader(file))
                self.logger.info(f"Read {len(data)} records from file.")
                return data
        except Exception as e:
            self.logger.error(f"Error reading data from file: {e}")
            raise

    def write_data(self, data):
        """Write mapped data to a CSV file."""
        try:
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                self.logger.info(f"Written {len(data)} records to file.")
        except Exception as e:
            self.logger.error(f"Error writing data to file: {e}")
            raise
