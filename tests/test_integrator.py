import pytest
from sf_data_integration.integrator import Integrator

@pytest.fixture
def integrator():
    return Integrator()

def test_integrator_process_data(integrator, mocker):
    data = [{'field1': 'value1'}, {'field2': 'value2'}]
    
    # Mocking the method that would handle data migration
    mock_migrate = mocker.patch.object(integrator, 'migrate_data', return_value=True)

    result = integrator.process_data(data)
    
    assert result is True
    mock_migrate.assert_called_once_with(data)
