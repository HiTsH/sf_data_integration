import pandas as pd
import hashlib
from typing import Dict

class DataTracker:
    def __init__(self, tracking_file: str = 'migration_tracking.csv'):
        self.tracking_file = tracking_file
        try:
            self.migrated_hashes = pd.read_csv(self.tracking_file)['hash'].tolist()
        except FileNotFoundError:
            self.migrated_hashes = []

    def generate_hash(self, record: Dict[str, Any]) -> str:
        record_string = ''.join([str(value) for value in record.values()])
        return hashlib.sha256(record_string.encode()).hexdigest()

    def is_migrated(self, record_hash: str) -> bool:
        return record_hash in self.migrated_hashes

    def track_migration(self, record_hash: str):
        self.migrated_hashes.append(record_hash)

    def save_tracking(self):
        df = pd.DataFrame({'hash': self.migrated_hashes})
        df.to_csv(self.tracking_file, index=False)
