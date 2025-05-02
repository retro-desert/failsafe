from app.actions.base import Action
from app import config, notify


class EmailAction(Action):
    def run(self):
        if not config.EMAIL_DISABLE:
            notify.send_email(subject=config.EMAIL_SUBJECT, body=config.MESSAGE)
