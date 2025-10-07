# I.G-UNIVERSAL-1.0

<div align="center">

# 🕵️ I.R Universal — Universal OSINT Tool

![Roblox](https://img.shields.io/badge/Roblox-000000?style=for-the-badge\&logo=roblox\&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge\&logo=kali-linux\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![OSINT](https://img.shields.io/badge/OSINT-Education-blue?style=for-the-badge)

</div>

**Advanced Open Source Intelligence Tool for Roblox**

---

<div align="center">

![Python3](https://img.shields.io/badge/language-Python3-red)
![GPLv3](https://img.shields.io/badge/license-GPLv3-blue)
![Version-1.3](https://img.shields.io/badge/version-1.3-green)
![Telegram](https://img.shields.io/badge/platform-Telegram-blue)
![Docker](https://img.shields.io/badge/platform-Docker-lightgrey)

</div>

> *For Educational and Security Research Purposes Only*

[![Screenshot-2025-10-06-185259.png](https://i.postimg.cc/zGsQTVyZ/Screenshot-2025-10-06-185259.png)](https://postimg.cc/SnGVhQLD)

## ⚠️ Legal Disclaimer

**WARNING**: This tool is developed **EXCLUSIVELY** for:

* Cybersecurity education and training
* Data privacy research
* Authorized penetration testing
* Digital security consulting

**❌ Prohibited Uses:**

* Stalking, harassment, or doxxing
* Collecting data without consent
* Any illegal activity
* Violating platform Terms of Service

**The author is not responsible for misuse of this tool. Use it ethically and legally.**

---

## 🚀 Features

### 📷 Instagram OSINT

* Public profile scraping (basic info)
* Content analysis: hashtags, posts, engagement metrics
* Social graph insights: followers / following patterns
* Metadata extraction (when available): timestamps, geo-tags

### 🎮 Roblox OSINT

* Player profile lookup and stats
* Activity audit: groups, friends, recent sessions
* Real-time online status checks
* Asset inspection: owned items and approximate valuations

### 🌐 Universal Search

* Multi-platform search: GitHub, X (ex-Twitter), Reddit, public pastebins
* Cross-platform identity correlation
* Threaded / concurrent queries for speed

---

## 🛠️ Installation

### Prerequisites

* Linux distro (Kali Linux recommended)
* Python 3.8+
* pip3
* Git
* Docker (optional)

### Quick Install

```bash
git clone https://github.com/your-username/universal-osint-tool.git
cd universal-osint-tool

chmod +x install.sh
./install.sh

python3 real_osint_tool.py
```

---

## 🧩 Main Files (Included in repo)

* `install.sh` — installation script (creates virtualenv, installs dependencies)
* `real_osint_tool.py` — main entrypoint (CLI / Telegram bridge)
* `search.sh` — bash demo script to format output
* `README.md` — this file

---

## 📥 Example Output (Demonstration)

```bash
[🎮] Search REAL Roblox info for: ProPlayer123
👤 Profile:
  Name: ProPlayer123
  ID: 123456789
  Friends: 87
  Groups: 5
  Status: 🟢 Online

# input example INSTAGRAM

[📷] Search REAL Instagram information for: johndoe

👤 Public Profile:
  Name: John Doe
  Bio: Digital Creator | Travel 🌍
  Followers: 1,245
  Following: 287
  Posts: 142
```

---

## 🧾 Ethical Usage

This project is intended for educational purposes. Before performing any public data collection, always check platform policies and obtain permissions when required.

---

## ⬇️ Example Scripts

### `install.sh`

```bash
#!/usr/bin/env bash
set -e

# install.sh - sets up environment and dependencies
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
else
  echo "# requirements.txt not found — installing common dependencies" 
  pip install requests beautifulsoup4 python-telegram-bot
fi

echo "Installation complete. Activate env with: source venv/bin/activate"
```

### `search.sh` (Demo)

```bash
#!/usr/bin/env bash

# Usage: ./search.sh <platform> <username>
PLATFORM="$1"
USER="$2"

if [ -z "$PLATFORM" ] || [ -z "$USER" ]; then
  echo "Usage: $0 <platform> <username>"
  exit 1
fi

case "${PLATFORM,,}" in
  roblox)
    echo "[🎮] Search REAL Roblox info for: $USER"
    echo "👤 Profile:"
    echo "  Name: $USER"
    echo "  ID: 123456789"
    echo "  Friends: 87"
    echo "  Groups: 5"
    echo "  Status: 🟢 Online"
    ;;
  instagram)
    echo "[📷] Search REAL Instagram information for: $USER"
    echo "👤 Public Profile:"
    echo "  Name: John Doe"
    echo "  Bio: Digital Creator | Travel 🌍"
    echo "  Followers: 1,245"
    echo "  Following: 287"
    echo "  Posts: 142"
    ;;
  *)
    echo "❌ Platform not supported. Try: roblox | instagram"
    ;;
esac
```
