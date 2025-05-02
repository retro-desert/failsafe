from app.actions import telegram_action, email_action
from app import logger

log = logger.get_logger(__name__)


class ActionRunner:
    def __init__(self):
        self.actions = [
            telegram_action.TelegramAction(),
            email_action.EmailAction(),
            # Add more actions here
        ]

    def run_all(self):
        log.warning("Failsafe triggered. Executing actions...")
        for action in self.actions:
            try:
                action.run()
            except Exception as e:
                log.error(f"{action.__class__.__name__} failed: {e}")
