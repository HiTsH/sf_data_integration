import yaml
from collections import defaultdict

class DataMapper:
    def __init__(self, mapping_file):
        self.mapping_file = mapping_file
        self.mapping_data = self.load_mapping()

    def load_mapping(self):
        """Load and parse the mapping configuration YAML file."""
        with open(self.mapping_file, 'r') as file:
            mapping = yaml.safe_load(file)
        return mapping

    def map_data(self, data, target_system):
        """Map data based on the loaded mapping configuration."""
        mapped_data = []
        for record in data:
            mapped_record = {}
            for source_field, target_field in self.mapping_data[target_system].items():
                if source_field in record:
                    mapped_record[target_field] = record[source_field]
            mapped_data.append(mapped_record)
        return mapped_data
