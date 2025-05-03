"""Email notifier"""
import smtplib
from email.mime.text import MIMEText

from app.core.base import Action
from app import config
from app.logger import get_logger


class EmailAction(Action):
    """Action: send message to email"""
    def __init__(self):
        self.log = get_logger(__name__)
        self.config = config

    def run(self):
        if not config.EMAIL_DISABLE:
            try:
                msg = MIMEText(self.config.MESSAGE)
                msg["Subject"] = self.config.EMAIL_SUBJECT
                msg["From"] = self.config.EMAIL_USER
                msg["To"] = self.config.EMAIL_TO

                with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
                    server.login(config.EMAIL_USER, config.EMAIL_PASS)
                    server.send_message(msg)
                    self.log.info("Email sent")
            except Exception as err:
                self.log.error("Email error: %s", err)
