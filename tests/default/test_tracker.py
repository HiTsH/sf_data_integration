import pytest
from sf_data_integration import DataTracker
import hashlib

def test_generate_hash():
    """
    Test hash generation for a sample record.
    """
    tracker = DataTracker()
    sample_record = {"Name": "Test", "Value": 123}
    
    record_hash = tracker.generate_hash(sample_record)
    expected_hash = hashlib.sha256("Test123".encode()).hexdigest()
    
    assert record_hash == expected_hash, "Generated hash does not match expected hash."

def test_is_migrated():
    """
    Test the check for already migrated data.
    """
    tracker = DataTracker()
    sample_hash = "sample_hash"
    tracker.migrated_hashes = [sample_hash]
    
    assert tracker.is_migrated(sample_hash), "Failed to recognize already migrated data."

def test_track_migration():
    """
    Test adding a new hash to the migrated list.
    """
    tracker = DataTracker()
    sample_hash = "new_hash"
    
    tracker.track_migration(sample_hash)
    assert sample_hash in tracker.migrated_hashes, "Hash was not added to the migrated list."

def test_save_tracking(tmp_path):
    """
    Test saving the migrated hashes to a CSV file.
    """
    # Use a temporary file for testing
    temp_file = tmp_path / "test_tracking.csv"
    tracker = DataTracker(tracking_file=temp_file)
    tracker.track_migration("sample_hash")
    
    # Save the tracking file and verify
    tracker.save_tracking()
    assert temp_file.exists(), "Tracking file was not created."
    
    saved_data = pd.read_csv(temp_file)
    assert "sample_hash" in saved_data['hash'].values, "Tracking data not saved correctly."
