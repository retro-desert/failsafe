"""Container module"""
import threading

from app import config
from app.logger import get_logger


class Container:
    """Container class"""
    def __init__(self):
        self.logger = get_logger
        self.config = config
        self.exit_event = threading.Event()
        self.reset_event = threading.Event()
