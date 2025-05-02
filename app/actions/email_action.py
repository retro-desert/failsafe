"""Email notifier"""
from app.actions.base import Action
from app import notify, config


class EmailAction(Action):
    """Action: send message to email"""
    def run(self):
        if not config.EMAIL_DISABLE:
            notify.send_email(subject=config.EMAIL_SUBJECT, body=config.MESSAGE)
