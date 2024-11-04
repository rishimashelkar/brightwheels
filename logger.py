# logger.py

import logging
from config import LOG_FILE

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger