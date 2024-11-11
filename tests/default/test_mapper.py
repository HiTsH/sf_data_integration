import pytest
from sf_data_integration.mapper import DataMapper

def test_map_data():
    data = [{"source_account_name": "Acme Corp"}]
    target_object = "Account"
    mapped_data = DataMapper.map_data(data, target_object)
    
    assert mapped_data[0]["Name"] == "Acme Corp"
    assert "source_account_name" not in mapped_data[0]
