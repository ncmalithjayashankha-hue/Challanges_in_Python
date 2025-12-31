import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "data/logs"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR,"pycore.log")

def get_logger(name = "PyCore"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = RotatingFileHandler(
            LOG_FILE, maxBytes=1_000_000, backupCount=3
        )
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger