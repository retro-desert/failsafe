from app.actions.base import Action
from app import config, notify


class TelegramAction(Action):
    """Action: send message to telegram"""
    def run(self):
        if not config.TELEGRAM_DISABLE:
            notify.send_telegram(config.MESSAGE)
