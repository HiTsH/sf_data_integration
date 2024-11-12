import pytest
from sf_data_integration.mapper import Mapper

@pytest.fixture
def mapper():
    return Mapper(mapping_config="sf_data_integration/mapping_config.yaml")

def test_mapper_apply_mapping(mapper):
    # Example input data and expected output after mapping
    input_data = {'field1': 'value1'}
    expected_output = {'mapped_field1': 'value1'}
    
    result = mapper.apply_mapping(input_data)
    assert result == expected_output

def test_mapper_load_mapping_config(mapper):
    assert mapper.mapping_config is not None
