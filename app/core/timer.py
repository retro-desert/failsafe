"""Module for timer handling"""
import time
import threading

from app.core import messages
from app.core.container import Container


def start_timer(container: Container, action_runner):
    """Start countdown"""
    def countdown():
        timer = container.config.TIME_LIMIT
        while timer > 0 and not container.exit_event.is_set():
            mins, secs = divmod(timer, 60)
            print(f"{messages.LOG['remaining']} {mins:02d}:{secs:02d}  ", end="\r", flush=True)
            time.sleep(1)
            if container.reset_event.is_set():
                timer += container.config.EXTEND_TIME
                container.reset_event.clear()
            else:
                timer -= 1

        if not container.exit_event.is_set():
            action_runner.run_all()
            container.exit_event.set()

    thread = threading.Thread(target=countdown, daemon=True)
    thread.start()
    return thread
