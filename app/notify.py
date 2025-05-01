import smtplib
import requests
from email.mime.text import MIMEText
from app import config
from app.logger import get_logger

log = get_logger(__name__)


def send_telegram(message: str):
    """Send telegram message"""
    try:
        url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": config.TELEGRAM_CHAT_ID, "text": message}
        response = requests.post(url, data=data, timeout=5)
        response.raise_for_status()
        log.info("Telegram message sent")
    except Exception as e:
        log.error(f"Telegram error: {e}")


def send_email(subject: str, body: str):
    """Send email message"""
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = config.EMAIL_USER
        msg["To"] = config.EMAIL_TO

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(config.EMAIL_USER, config.EMAIL_PASS)
            server.send_message(msg)
            log.info("Email sent")
    except Exception as e:
        log.error(f"Email error: {e}")
