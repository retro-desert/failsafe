from app import logger
from app.core import messages
from app.core.actions_runner import ActionRunner
from app.core.timer import start_timer
from app.core.input import start_input_listener
from app.core.state import reset_event, exit_event

log = logger.get_logger(__name__)
action_runner = ActionRunner()


def start_failsafe():
    """Start threads, main logic"""
    print()
    log.info(messages.LOG["started"])
    print(messages.PROMPT["input"])
    exit_event.clear()
    reset_event.clear()

    timer_thread = start_timer(action_runner)
    input_thread = start_input_listener()

    try:
        timer_thread.join()
        input_thread.join()
    except KeyboardInterrupt:
        log.info(messages.LOG["interrupted"])
        exit_event.set()
