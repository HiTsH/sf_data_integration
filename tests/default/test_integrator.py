import pandas as pd
import pytest
from sf_data_integration import DataIntegrator

def test_load_data():
    """
    Test loading data from a sample CSV file.
    """
    integrator = DataIntegrator(sources=["data/sample.csv"])
    data = integrator.load_data()
    
    assert not data.empty, "Loaded data is empty."
    assert isinstance(data, pd.DataFrame), "Loaded data is not a DataFrame."

def test_clean_data():
    """
    Test cleaning of the loaded data.
    """
    integrator = DataIntegrator(sources=["data/sample.csv"])
    data = pd.DataFrame({
        "required_column": [1, None, 2],
        "duplicated_column": [1, 1, 2]
    })
    cleaned_data = integrator.clean_data(data)
    
    # Check that data has no missing required values and duplicates are removed
    assert cleaned_data["required_column"].isna().sum() == 0, "There are NaN values in required columns."
    assert cleaned_data.duplicated().sum() == 0, "Duplicates are not removed."

def test_transform_data():
    """
    Test transforming the data for Salesforce compatibility.
    """
    integrator = DataIntegrator(sources=[])
    data = pd.DataFrame({"OldColumnName": ["value1", "value2"]})
    transformed_data = integrator.transform_data(data)
    
    # Check transformation result
    assert isinstance(transformed_data, list), "Transformed data is not a list."
    assert all("NewColumnName" in record for record in transformed_data), "Column renaming failed."
