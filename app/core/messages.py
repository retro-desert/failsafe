from app import config

LOG = {
    "started": "Failsafe started",
    "interrupted": "Interrupted",
    "triggered": "Failsafe triggered. Executing actions...",
    "cancelled": "Failsafe cancelled",
    "extended": f"Failsafe extended by {config.EXTEND_TIME}",
    "remaining": "[ FAILSAFE ACTIVE ] Time remaining:"
}

PROMPT = {
    "input": "\n[ C ] Cancel | [ E ] Extend:"
}
