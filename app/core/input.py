import sys
import tty
import termios
import select
import threading

from app.core import messages
from app.core.state import exit_event, reset_event
from app import logger

log = logger.get_logger(__name__)


def listen_for_input():
    """Listen user input"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        while not exit_event.is_set():
            if select.select([sys.stdin], [], [], 0.1)[0]:
                char = sys.stdin.read(1).lower()
                if char == "c":
                    log.info(messages.LOG["cancelled"])
                    exit_event.set()
                elif char == "e":
                    log.info(messages.LOG["extended"])
                    reset_event.set()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def start_input_listener():
    """Start thread"""
    thread = threading.Thread(target=listen_for_input, daemon=True)
    thread.start()
    return thread
