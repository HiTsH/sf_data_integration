from typing import List, Dict, Any

class BatchProcessor:
    """
    Processes data in batches for efficient migration.
    """

    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    def batch_data(self, data: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
        """
        Splits data into batches.

        :param data: Data to split.
        :return: Batches of data.
        """
        return [data[i:i + self.batch_size] for i in range(0, len(data), self.batch_size)]
