# ╔══════════════════════════════════════════════════════════╗
# ║  ███████╗██╗██╗     ███████╗████████╗██████╗  █████╗   ║
# ║  ██╔════╝██║██║     ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ║
# ║  █████╗  ██║██║     █████╗     ██║   ██████╔╝███████║  ║
# ║  ██╔══╝  ██║██║     ██╔══╝     ██║   ██╔══██╗██╔══██║  ║
# ║  ██║     ██║███████╗███████╗   ██║   ██║  ██║██║  ██║  ║
# ║  ╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝  ║
# ║      ████████╗██████╗  █████╗ ███╗   ██╗███████╗       ║
# ║      ╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝       ║
# ║         ██║   ██████╔╝███████║██╔██╗ ██║█████╗         ║
# ║         ██║   ██╔══██╗██╔══██║██║╚██╗██║██╔══╝         ║
# ║         ██║   ██║  ██║██║  ██║██║ ╚████║███████╗       ║
# ║         ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝       ║
# ╚══════════════════════════════════════════════════════════╝

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square&logo=github)](https://github.com/shubhyagami/fileTransfer)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/badge/stars-%E2%AD%90%20142-yellow?style=flat-square)](https://github.com/shubhyagami/fileTransfer/stargazers)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![Encryption](https://img.shields.io/badge/encryption-AES--256--GCM-red?style=flat-square&logo=openssl)](https://en.wikipedia.org/wiki/Galois/Counter_Mode)
[![Discord](https://img.shields.io/badge/discord-join%20chat-7289DA?style=flat-square&logo=discord)](https://discord.gg/tva-engineering)

---

> **`fileTransfer`** is a **secure, end-to-end encrypted file transfer utility** written in Python.  
> No cloud, no middlemen — just direct, authenticated, and encrypted file sharing between peers.  
> Because your data deserves a private highway, not a public postcard.

---

## 🚀 Features

| Icon | Feature |
|------|---------|
| 🔒 | **AES-256-GCM encryption** – Military-grade, authenticated encryption |
| 🧑‍💻 | **Zero-knowledge authentication** – Passwords never leave your machine |
| 📡 | **Peer-to-peer transfer** – No central server, no metadata leaks |
| ⚡ | **Resumable transfers** – Network hiccup? Pick up right where you left off |

---

## ⚡ Quick Start

Get up and running in under 60 seconds. No cloud accounts, no API keys, no nonsense.

### Installation

```bash
# Clone the repository
git clone https://github.com/shubhyagami/fileTransfer.git
cd fileTransfer

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Sending a File

```bash
# On the sender's machine
python filetransfer.py send --file secret_plans.pdf --port 5050

# Output:
# ╔══════════════════════════════════════════════════╗
# ║  🔒 Encrypted channel established               ║
# ║  📡 Listening on 
```

---

## 💡 Pro Tips

| Tip | Description |
|-----|-------------|
| 🧩 **Resume broken transfers** | Use `--resume` when the connection drops. The client automatically re‑requests missing chunks — no data wasted. |
| 📦 **Send entire folders** | Combine with `tar` on the fly: `tar czf - ./my_folder \| python filetransfer.py send --stream` — the receiver extracts with `tar xzf -`. |
| 🔐 **Automate with password files** | Pass a password file via `--password-file` instead of typing it interactively. Handy for cron jobs or CI/CD pipelines. |

---

## 📅 Changelog

### [1.2.0] - 2026-07-31

#### Added
- **Pro Tips section** in README with practical usage hints.
- **Automatic port binding fallback**: if the requested port is busy, the tool now tries the next available port and informs you.

#### Fixed
- Resolved a rare race condition during concurrent chunk requests on high‑latency networks.

---

*Your privacy is not a feature — it's the default. Stay encrypted.*