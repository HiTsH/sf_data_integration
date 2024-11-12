from sf_data_integration.logger import setup_logger

class BatchProcessor:
    def __init__(self, batch_size=100):
        self.batch_size = batch_size
        self.logger = setup_logger("batch_processor", log_dir="sf_data_integration/logs")

    def process_batches(self, data, processor_func=None):
        """Process data in batches, applying transformation/logic to each batch."""
        total_batches = len(data) // self.batch_size + (1 if len(data) % self.batch_size > 0 else 0)
        
        for i in range(total_batches):
            batch = data[i * self.batch_size: (i + 1) * self.batch_size]
            self.logger.info(f"Processing batch {i + 1} of size {len(batch)}.")
            
            # Apply transformation, validation, or migration to each batch
            try:
                if processor_func:
                    # Apply user-defined processor function to each batch
                    self.logger.info(f"Applying custom processing function to batch {i + 1}.")
                    processed_batch = processor_func(batch)
                else:
                    processed_batch = batch  # No custom function, proceed with raw batch
                
                # Further logic for batch processing such as migration to a target system
                self.migrate_batch(processed_batch)

            except Exception as e:
                self.logger.error(f"Error processing batch {i + 1}: {e}")

    def migrate_batch(self, batch):
        """Simulate data migration logic for a batch."""
        # Logic for migrating a batch to the target system, e.g., inserting into a database or API
        self.logger.info(f"Migrating {len(batch)} records to the target system.")
        # For example, this could be calling an API or database insert function
        # target_system.insert_data(batch)
        
        # Simulating migration with a log message (replace with actual implementation)
        self.logger.info(f"Batch migration completed for {len(batch)} records.")
