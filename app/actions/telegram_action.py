"""Telegram notifier"""
import requests
from app.actions.base import Action
from app import config
from app.logger import get_logger


class TelegramAction(Action):
    """Action: send message to telegram"""

    def __init__(self):
        self.log = get_logger(__name__)
        self.config = config

    def run(self):
        if not config.TELEGRAM_DISABLE:
            try:
                url = f"https://api.telegram.org/bot{self.config.TELEGRAM_TOKEN}/sendMessage"
                data = {"chat_id": self.config.TELEGRAM_CHAT_ID, "text": self.config.MESSAGE}
                response = requests.post(url, data=data, timeout=5)
                response.raise_for_status()
                self.log.info("Telegram message sent")
            except Exception as err:
                self.log.error("Telegram error: %s", err)
