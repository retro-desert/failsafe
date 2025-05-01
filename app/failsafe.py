import select
import sys
import termios
import threading
import time
import tty
from app import config, notify
from app.logger import get_logger

log = get_logger(__name__)

exit_event = threading.Event()
timer_reset_event = threading.Event()


def trigger_action():
    """Trigger call"""
    print()
    log.info("[ FAILSAFE ] Sending messages...")

    if not config.TELEGRAM_DISABLE:
        notify.send_telegram(config.MESSAGE)
    if not config.EMAIL_DISABLE:
        notify.send_email(subject=config.EMAIL_SUBJECT, body=config.MESSAGE)
    exit_event.set()


def countdown():
    """Countdown to trigger call"""
    timer = config.TIME_LIMIT
    print()
    log.info("Failsafe started")
    print("\n[ C ] Cancel | [ E ] Extend:")
    while not exit_event.is_set():
        if timer_reset_event.is_set():
            timer += config.EXTEND_TIME
            timer_reset_event.clear()

        mins, secs = divmod(timer, 60)
        print(f"\r[ FAILSAFE ACTIVE ] Time remaining: {mins:02}:{secs:02}  ", end="", flush=True)
        time.sleep(1)
        timer -= 1

        if timer <= 0:
            trigger_action()


def listen_input():
    """Listen for user input (extend or exit)"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)
        while not exit_event.is_set():
            if select.select([sys.stdin], [], [], 0.1)[0]:
                char = sys.stdin.read(1).lower()
                if char == "c":
                    print()
                    log.info("Failsafe cancelled")
                    exit_event.set()
                elif char == "e":
                    print()
                    log.info("Failsafe extended by %s", config.EXTEND_TIME)
                    timer_reset_event.set()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
