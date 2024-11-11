import pytest
import os
from sf_data_integration.logger import setup_logger

def test_setup_logger(tmp_path):
    logger = setup_logger("test_project", log_dir=str(tmp_path))
    assert logger.handlers[0].baseFilename == str(tmp_path / "test_project_log.txt")
    assert logger.level == logging.INFO
