import logging
from pathlib import Path


def setup_logging(file_name: str, file_path: Path):
    logger = logging.getLogger(file_name)
    file_handler = logging.FileHandler(file_path, mode='w')
    file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
