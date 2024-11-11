import pytest
from sf_data_integration.tracker import DataTracker
import hashlib

def test_data_tracker():
    tracker = DataTracker()
    record = {"name": "Test"}
    record_hash = tracker.generate_hash(record)
    
    assert not tracker.is_migrated(record_hash)
    
    tracker.track_migration(record_hash)
    assert tracker.is_migrated(record_hash)
    
    tracker.save_tracking()
