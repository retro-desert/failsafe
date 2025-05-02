import time
import threading

from app.core import messages
from app.core.state import exit_event, reset_event
from app import config, logger

log = logger.get_logger(__name__)


def start_timer(action_runner):
    """Start countdown"""
    def countdown():
        timer = config.TIME_LIMIT
        while timer > 0 and not exit_event.is_set():
            mins, secs = divmod(timer, 60)
            print(f"{messages.LOG['remaining']} {mins:02d}:{secs:02d}  ", end="\r", flush=True)
            time.sleep(1)
            if reset_event.is_set():
                timer += config.EXTEND_TIME
                reset_event.clear()
            else:
                timer -= 1

        if not exit_event.is_set():
            action_runner.run_all()
            exit_event.set()

    thread = threading.Thread(target=countdown, daemon=True)
    thread.start()
    return thread
