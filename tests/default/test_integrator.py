import pytest
from sf_data_integration.integrator import DataIntegrator
from sf_data_integration.connector import SalesforceConnector
from sf_data_integration.mapper import DataMapper
from sf_data_integration.tracker import DataTracker
from sf_data_integration.batch_processor import BatchProcessor
import logging

def test_data_integrator_init():
    logger = logging.getLogger("test")
    sf_connector = SalesforceConnector("username", "password", "token", logger)
    data_mapper = DataMapper()
    data_tracker = DataTracker()
    batch_processor = BatchProcessor()
    
    integrator = DataIntegrator(sf_connector, data_mapper, data_tracker, batch_processor, logger)
    assert integrator.sf_connector == sf_connector
    assert integrator.data_mapper == data_mapper
    assert integrator.data_tracker == data_tracker
    assert integrator.batch_processor == batch_processor
    assert integrator.logger == logger
