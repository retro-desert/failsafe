# Failsafe
![Code Quality](https://img.shields.io/badge/code%20quality-9+%2F10-brightgreen?logo=python&labelColor=2e2e2e)
![Pylint](https://github.com/retro-desert/failsafe/actions/workflows/pylint.yml/badge.svg)

**Failsafe** is a terminal-based watchdog timer that trigger actions unless manually canceled or extended

**Ideal for emergency situations or alert scenarios**

---
## 🚀 Features
- ⏳**Countdown timer with configurable duration**
- ⌨️**Keyboard input control:**
  - `C` — Cancel
  - `E` — Extend
- 📄**Flexible architecture: add your actions easily**
- 📬**Sends notifications via:**
  - Telegram
  - Email
- 🐳**Works in terminal or Docker**
- 🧱**Dependency containerization**
- 📂**Fallback logging**

## 🛠️ Setup
1. **Clone the repository:**
    ```bash
    git clone https://github.com/retro-desert/failsafe.git
    cd failsafe
    ```
2. **Set up a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. **Configure the .env file according to the .env.example**

## ▶️Usage

```bash
python -m app.main
```

**Example output:**
```
 _____ _    ___ _     ____    _    _____ _____ 
|  ___/ \  |_ _| |   / ___|  / \  |  ___| ____|
| |_ / _ \  | || |   \___ \ / _ \ | |_  |  _|  
|  _/ ___ \ | || |___ ___) / ___ \|  _| | |___ 
|_|/_/   \_\___|_____|____/_/   \_\_|   |_____|
created by @retro-desert
→ github.com/retro-desert · eleet.nl

Version 2.0.0

[ C ] Cancel | [ E ] Extend:
[ FAILSAFE ACTIVE ] Time remaining: 00:59

```

## 🐳 Docker Support
**Run with:**

`make run`

OR

`docker-compose run failsafe`

## 📦 Project Structure
```graphql
app/
├── config.py              # Configuration
├── logger.py              # Logging setup
├── main.py                # Entry point
├── version.py             # ASCII art and version
├── actions/
│   ├── base.py            # Action interface
│   ├── email_action.py    # Email notification
│   └── telegram_action.py # Telegram notification
├── core/
│   ├── actions_runner.py  # Action starter
│   ├── container.py       # Dependency injection container
│   ├── failsafe.py        # Main logic
│   ├── input_handle.py    # Keyboard input handling
│   ├── messages.py        # Text messages and prompts
│   └── timer.py           # Countdown timer
```

## ✉️Adding actions
Just **add the file** that inherits from **Action** (base.py) **to** `app/actions/`

**It will be automatically detected**

Example:
```python
from app.actions.base import Action

class MyCustomAction(Action):
    def run(self):
        print("Custom action triggered!")
```

## 📝 Logging
- Default log path: `logs/failsafe.log`
- If permission is denied, fallback: `/tmp/failsafe.log`

## 📄 License
MIT License — feel free to use, modify, and share.

## 🙌