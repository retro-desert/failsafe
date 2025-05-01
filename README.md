# ⏳ Failsafe
**Failsafe** is a terminal-based watchdog timer that trigger actions unless manually canceled or extended. Ideal for unattended processes or alert scenarios

---
## 🚀 Features
- **Countdown timer with configurable duration**
- **Keyboard input control:**
  - `C` — Cancel
  - `E` — Extend
- **Sends notifications via:**
  - 📬 Telegram
  - 📩 Email
- **Works in terminal or Docker**
- **Fallback logging**

---
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
3. **Configure the .env file according to the .env_example**

---
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
    
Version 1.0

[ C ] Cancel | [ E ] Extend:
[ FAILSAFE ACTIVE ] Time remaining: 00:59

```
---

## 🐳 Docker Support
**Run with:**

`make run`

OR

`docker-compose run failsafe`

---
## 📝 Logging
- Default log path: `logs/failsafe.log`
- If permission is denied, fallback: `/tmp/failsafe.log`

---
## 📁 Project Structure
```graphql
app/
│
├── main.py          # Entry point
├── config.py        # Settings
├── failsafe.py      # Timer and input logic
├── notify.py        # Notification handlers
├── logger.py        # Logging setup
├── version.py       # ASCII and version info
└── ...
```
---
## 📄 License
MIT License — feel free to use, modify, and share.

## 🙌