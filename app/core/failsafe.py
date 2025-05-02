"""Main logic with threads"""
from app.core import messages
from app.core.actions_runner import ActionRunner
from app.core.container import Container
from app.core.input_handle import start_input_listener
from app.core.timer import start_timer


def start_failsafe(container: Container) -> None:
    """Start threads, main logic"""
    log = container.logger(__name__)
    action_runner = ActionRunner(container)
    print()
    log.info(messages.LOG["started"])
    print(messages.PROMPT["input"])
    container.exit_event.clear()
    container.reset_event.clear()

    timer_thread = start_timer(container=container, action_runner=action_runner)
    input_thread = start_input_listener(container)

    try:
        timer_thread.join()
        input_thread.join()
    except KeyboardInterrupt:
        log.info(messages.LOG["interrupted"])
        container.exit_event.set()
