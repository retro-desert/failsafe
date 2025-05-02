"""Config module"""
from decouple import config

# Message to send
MESSAGE = config("MESSAGE", cast=str, default="")

# Timers
TIME_LIMIT = config("TIME_LIMIT", cast=int, default=60)
EXTEND_TIME = config("EXTEND_TIME", cast=int, default=30)

# Disable message sending
EMAIL_DISABLE = config("EMAIL_DISABLE", cast=bool, default=False)
TELEGRAM_DISABLE = config("TELEGRAM_DISABLE", cast=bool, default=False)

# Telegram
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN", cast=str, default="")
TELEGRAM_CHAT_ID = config("TELEGRAM_CHAT_ID", cast=str, default="")

# Email
EMAIL_USER = config("EMAIL_USER", cast=str, default="")
EMAIL_PASS = config("EMAIL_PASS", cast=str, default="")
EMAIL_TO = config("EMAIL_TO", cast=str, default="")
EMAIL_SUBJECT = config("EMAIL_SUBJECT", cast=str, default="")

# Logs
LOG_DIR = config("LOG_DIR", cast=str, default="logs")
LOG_FILENAME = config("LOG_FILE", cast=str, default="failsafe.log")
FALLBACK_LOG_FILE = config("FALLBACK_LOG_FILE", cast=str, default="/tmp/failsafe.log")
