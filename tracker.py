from sf_data_integration.logger import setup_logger
import hashlib

class Tracker:
    def __init__(self, tracking_file='sf_data_integration/logs/tracking_log.txt'):
        self.tracking_file = tracking_file
        self.logger = setup_logger("tracker", log_dir="sf_data_integration/logs")

    def track_data(self, data):
        """Track the migration progress by creating hashes for data."""
        hashes = {}
        for record in data:
            record_hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
            hashes[record_hash] = record
        with open(self.tracking_file, 'w') as file:
            file.write(str(hashes))
        self.logger.info(f"Tracked {len(hashes)} records in migration process.")
