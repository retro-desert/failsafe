"""Module for input handling"""
import sys
import tty
import termios
import select
import threading

from app.core import messages
from app.core.container import Container


def listen_for_input(container: Container) -> None:
    """Listen user input"""
    log = container.logger(__name__)
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        while not container.exit_event.is_set():
            if select.select([sys.stdin], [], [], 0.1)[0]:
                char = sys.stdin.read(1).lower()
                if char == "c":
                    log.info(messages.LOG["cancelled"])
                    container.exit_event.set()
                elif char == "e":
                    log.info(messages.LOG["extended"])
                    container.reset_event.set()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def start_input_listener(container: Container) -> threading.Thread:
    """Start thread"""
    thread = threading.Thread(target=listen_for_input, args=(container,), daemon=True)
    thread.start()
    return thread
