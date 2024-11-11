import pytest
from sf_data_integration.batch_processor import BatchProcessor

def test_batch_data():
    data = [{"id": i} for i in range(250)]
    batch_processor = BatchProcessor(batch_size=100)
    batches = batch_processor.batch_data(data)
    
    assert len(batches) == 3  # Should create 3 batches
    assert len(batches[0]) == 100
    assert len(batches[1]) == 100
    assert len(batches[2]) == 50
