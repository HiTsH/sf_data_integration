import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(project_name: str, log_dir: str = "log") -> logging.Logger:
    """
    Sets up a rotating logger for a specific project.

    :param project_name: Name of the project to customize log filename.
    :param log_dir: Directory where log files will be stored.
    :return: Configured logger instance.
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file = os.path.join(log_dir, f"{project_name}_log.txt")
    logger = logging.getLogger(project_name)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger
