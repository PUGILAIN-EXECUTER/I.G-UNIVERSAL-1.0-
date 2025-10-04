# I.G-UNIVERSAL-1.0-
🕵️ Universal OSINT Tool - Advanced Open Source Intelligence for Instagram &amp; Roblox | Kali Linux | Educational Purpose Only | Python Security Research | Public Data Analysis
                                                                  
I.R Universal — Universal OSINT Tool

<div align="center">
  
![Roblox](https://img.shields.io/badge/Roblox-000000?style=for-the-badge&logo=roblox&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OSINT](https://img.shields.io/badge/OSINT-Education-blue?style=for-the-badge)

**Advanced Open Source Intelligence Tool for Instagram & Roblox**

*For Educational and Security Research Purposes Only*

</div>

---

## ⚠️ Legal Disclaimer

**WARNING**: This tool is developed **EXCLUSIVELY** for:

* Cybersecurity education and training
* Data-privacy research
* Authorized penetration testing
* Digital security consulting

**❌ Prohibited Uses:**

* Stalking, harassment, or doxxing
* Collecting data without consent
* Any illegal activity
* Violating platform Terms of Service

**The author is not responsible for misuse of this tool. Use it ethically and lawfully.**

#input example ROBLOX

```bash
#!/bin/bash

# Usage: ./search.sh <platform> <username>
# Example: ./search.sh roblox ProPlayer123

PLATFORM=$1
USER=$2

if [ -z "$PLATFORM" ] || [ -z "$USER" ]; then
  echo "Usage: $0 <platform> <username>"
  exit 1
fi

case "$PLATFORM" in
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

* Multi-platform search: GitHub, Twitter/X, Reddit, public pastebins
* Cross-platform identity correlation
* Threaded / concurrent queries for speed

---

## 🛠️ Installation

### Prerequisites

* Linux distro (Kali Linux recommended)
* Python 3.8+
* pip3

### Quick install

```bash
git clone https://github.com/your-username/universal-osint-tool.git
cd universal-osint-tool

chmod +x install.sh
./install.sh

python3 real_osint_tool.py
