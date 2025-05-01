from decouple import config

# Message to send
MESSAGE = config("MESSAGE")

# Timers
TIME_LIMIT = config("TIME_LIMIT", default=60, cast=int)
EXTEND_TIME = config("EXTEND_TIME", default=30, cast=int)

# Disable message sending
EMAIL_DISABLE = config("EMAIL_DISABLE", default=False, cast=bool)
TELEGRAM_DISABLE = config("TELEGRAM_DISABLE", default=False, cast=bool)

# Telegram
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = config("TELEGRAM_CHAT_ID")

# Email
EMAIL_USER = config("EMAIL_USER")
EMAIL_PASS = config("EMAIL_PASS")
EMAIL_TO = config("EMAIL_TO")
EMAIL_SUBJECT = config("EMAIL_SUBJECT")
