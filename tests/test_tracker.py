import pytest
from sf_data_integration.tracker import Tracker

@pytest.fixture
def tracker():
    return Tracker()

def test_tracker_create_hash(tracker):
    data = {"field1": "value1", "field2": "value2"}
    hash_value = tracker.create_hash(data)
    assert isinstance(hash_value, str)
    assert len(hash_value) > 0

def test_tracker_check_existing_hash(tracker):
    data = {"field1": "value1", "field2": "value2"}
    hash_value = tracker.create_hash(data)
    assert tracker.check_existing_hash(hash_value) is False
