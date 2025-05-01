import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "failsafe.log")
FALLBACK_LOG_FILE = f"/tmp/failsafe.log"

try:
    os.makedirs(LOG_DIR, exist_ok=True)
except PermissionError:
    pass


def setup_logger():
    """Call this once at startup to configure global logging"""
    if logging.getLogger().hasHandlers():
        return

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    try:
        file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
    except PermissionError:
        print(f"[ WARN ] No permission for '{LOG_FILE}', using fallback log: '{FALLBACK_LOG_FILE}'")
        file_handler = RotatingFileHandler(FALLBACK_LOG_FILE, maxBytes=1_000_000, backupCount=1)

    file_handler.setFormatter(formatter)
    logging.basicConfig(
        level=logging.INFO,
        handlers=[stream_handler, file_handler]
    )


def get_logger(name: str):
    """Return a logger"""
    return logging.getLogger(name)
