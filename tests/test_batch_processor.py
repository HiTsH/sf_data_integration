import pytest
from unittest.mock import MagicMock
from sf_data_integration.batch_processor import BatchProcessor

@pytest.fixture
def batch_processor():
    return BatchProcessor(batch_size=50)

def test_process_batches_no_processor(batch_processor):
    # Mock the migrate_batch method
    batch_processor.migrate_batch = MagicMock()

    # Test with sample data
    data = [{'field1': 'value1'}, {'field2': 'value2'}, {'field3': 'value3'}]
    batch_processor.process_batches(data)

    # Assert migrate_batch was called for each batch
    assert batch_processor.migrate_batch.call_count == 1  # Only 1 batch for 3 records
    batch_processor.migrate_batch.assert_called_with(data)  # Ensure the batch passed to migrate_batch is correct

def test_process_batches_with_custom_processor(batch_processor):
    # Define a custom processor function
    def custom_processor(batch):
        return [{'field1': f"{item['field1']}_processed"} for item in batch]

    # Mock the migrate_batch method
    batch_processor.migrate_batch = MagicMock()

    # Test with sample data
    data = [{'field1': 'value1'}, {'field1': 'value2'}, {'field1': 'value3'}]
    batch_processor.process_batches(data, processor_func=custom_processor)

    # Assert migrate_batch was called for each batch
    assert batch_processor.migrate_batch.call_count == 1
    # Verify the custom processor transformed the data
    processed_batch = [{'field1': 'value1_processed'}, {'field1': 'value2_processed'}, {'field1': 'value3_processed'}]
    batch_processor.migrate_batch.assert_called_with(processed_batch)

def test_process_batches_with_empty_data(batch_processor):
    data = []
    batch_processor.process_batches(data)
    batch_processor.migrate_batch.assert_not_called()  # No batches to process
