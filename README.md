# Failsafe
![Version](https://img.shields.io/github/v/tag/retro-desert/failsafe?label=version)
![Code Quality](https://img.shields.io/badge/code%20quality-9+%2F10-brightgreen?logo=python&labelColor=2e2e2e)
![Pylint](https://github.com/retro-desert/failsafe/actions/workflows/pylint.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

**Failsafe** is a terminal-based watchdog timer that trigger custom actions unless manually canceled or extended

**Ideal for emergency situations or alert scenarios**

---
## 🚀 Features
- ⏳**Countdown timer with configurable duration**
- 📄**Flexible architecture: add your actions easily**
- ⌨️**Keyboard input control:**
  - `C` — Cancel
  - `E` — Extend
- 📬**Sends notifications via:**
  - Telegram
  - Email
- 🐳**Works in CLI or Docker**
- 🧱**Dependency containerization**
- 📂**Fallback logging**

## 🎯 Use Cases
**Failsafe** is useful in any scenario where inaction could lead to problems. It acts as a watchdog for processes that should not be left unattended
### 🆘 Personal Safety & Failsafe Trigger
**In situations where a person might be alone, at risk, or in a potentially dangerous environment (e.g., hiking, traveling, working late), Failsafe can be preconfigured to send critical alerts to trusted contacts if no interaction is received within a set time window. This acts like a digital "dead man's switch" — useful for peace of mind in uncertain scenarios**
### 🔔 Timed Alerts
**Automatically sends notifications if the timer expires without user intervention — perfect for reminders or critical monitoring**
### 🔐 Forgotten State Prevention
**Helps prevent scenarios where you forget to stop a temporary process — like a dev server, test environment, or access session**

## 🛠️ Setup
1. **Clone the repo**
    ```bash
    git clone https://github.com/retro-desert/failsafe.git
    cd failsafe
    ```
2. **Set up a virtual environment and install dependencies**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. **Configure the `.env` file according to the `.env.example`**
4. **(Optional) [Add your custom actions](#%EF%B8%8Fadding-custom-actions)**

## ▶️ Usage

```bash
python -m app.main
```

**Example output**
```
 _____ _    ___ _     ____    _    _____ _____ 
|  ___/ \  |_ _| |   / ___|  / \  |  ___| ____|
| |_ / _ \  | || |   \___ \ / _ \ | |_  |  _|  
|  _/ ___ \ | || |___ ___) / ___ \|  _| | |___ 
|_|/_/   \_\___|_____|____/_/   \_\_|   |_____|
created by @retro-desert
→ github.com/retro-desert · eleet.nl

Version 2.0.1

[ C ] Cancel | [ E ] Extend:
[ FAILSAFE ACTIVE ] Time remaining: 00:59
```

- **The program activates the timer when it starts**
- **The user sees an interface with the ability to**
  - **`[ C ] Cancel` - stop the timer (cancel the actions)**
  - **`[ E ] Extend` - extend time**
- **If the user does not react before the timer expires, connected actions (e.g. sending a message to Telegram or email) are automatically started**
- **All actions are defined in the `actions` folder and can be extended with custom scripts**

## 🐳 Docker
### Local image - with default actions (Recommended) 
1. **Clone the repo**
    ```bash
    git clone https://github.com/retro-desert/failsafe.git
    cd failsafe
    ```
2. **Configure the `.env` file according to the `.env.example`**
    ```yaml
    # Message to send
    MESSAGE=Very important message
    # Countdown time
    TIME_LIMIT=60
    # Extend time
    EXTEND_TIME=30
    # Disable message sending
    EMAIL_DISABLE=0
    TELEGRAM_DISABLE=0
    # Telegram token
    TELEGRAM_TOKEN=token123
    # Telegram chat id to send message
    TELEGRAM_CHAT_ID=11111
    # Email settings (GMail works)
    EMAIL_USER=sender@example.com
    EMAIL_PASS=qwerty123
    EMAIL_TO=receiver@example.com
    EMAIL_SUBJECT=FAILSAFE message
    # Logs settings
    LOG_DIR=logs
    LOG_FILENAME=failsafe.log
    FALLBACK_LOG_FILE=/tmp/failsafe.log
    ```
3. **(Optional) [Add your custom actions](#%EF%B8%8Fadding-custom-actions)**
4. **Build image**
    ```bash
    make build
    ```
5. **Run**
    ```bash
    make run
    ```

### Remote image - without default actions
1. **Create a working folders**
    ```bash
    mkdir -p failsafe/actions failsafe/logs
    cd failsafe
    ```
2. **Create a `docker-compose.yml`**
    ```yaml
    services:
      failsafe:
        image: retrodesert/failsafe:latest
        container_name: failsafe
        stdin_open: true
        tty: true
        volumes:
          - ./logs:/failsafe/logs
          - ./actions:/failsafe/app/actions
        env_file:
          - .env
    ```
3. **Create the `.env` file according to the `.env.example`**
    ```yaml
    # Message to send
    MESSAGE=Very important message
    # Countdown time
    TIME_LIMIT=60
    # Extend time
    EXTEND_TIME=30
    # Logs settings
    LOG_DIR=logs
    LOG_FILENAME=failsafe.log
    FALLBACK_LOG_FILE=/tmp/failsafe.log
    ```
4. **(Optional) [Add your custom actions](#%EF%B8%8Fadding-custom-actions)**
5. **Run**
    ```bash
    docker-compose run --rm failsafe
    ```

## 🧩 Default actions
|  Action              | Description              | Environment vars                                        |
|----------------------|--------------------------|---------------------------------------------------------|
| `telegram_action.py` | Send message to Telegram | `TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID`                    |
| `email_action.py`    | Send email from GMail    | `EMAIL_USER`, `EMAIL_PASS`, `EMAIL_TO`, `EMAIL_SUBJECT` |

It is also possible to simply disable these actions via variables: `TELEGRAM_DISABLE` and `EMAIL_DISABLE`

## ✉️ Adding custom actions
To add your own scripts, simply place them in the `./app/actions` (docker-compose - `./actions`). It will be automatically detected

Dependency
- **Script should inherit from Action (app/core/base.py)**

Example script
```python
from app.core.base import Action

class MyCustomAction(Action):
    def run(self):
        print("Custom action triggered!")
```

## 📦 Project Structure
```graphql
app/
├── config.py               # Configuration
├── logger.py               # Logging setup
├── main.py                 # Entry point
├── version.py              # ASCII art and version
├── actions/
│   ├── email_action.py     # Email notification
│   └── telegram_action.py  # Telegram notification
├── core/
│   ├── actions_runner.py   # Action starter
│   ├── base.py             # Action interface
│   ├── container.py        # Dependency injection container
│   ├── failsafe.py         # Main logic
│   ├── input_handle.py     # Keyboard input handling
│   ├── messages.py         # Text messages and prompts
│   └── timer.py            # Countdown timer
```

## 📝 Logging
- Default log path: `./logs/failsafe.log`
- If permission is denied, fallback: `/tmp/failsafe.log`

## 📄 License
MIT License — feel free to use, modify, and share.

## 🙌