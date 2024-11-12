import pytest
import logging
from sf_data_integration.logger import setup_logger

@pytest.fixture
def logger(tmp_path):
    return setup_logger("test_logger", log_dir=str(tmp_path))

def test_logger_initialization(logger, tmp_path):
    log_file = str(tmp_path / "test_logger_log.txt")
    assert logger.handlers[0].baseFilename == log_file
    assert logger.level == logging.INFO

def test_logger_log_message(logger, tmp_path):
    logger.info("Test message")
    with open(str(tmp_path / "test_logger_log.txt"), "r") as f:
        logs = f.read()
    assert "Test message" in logs
