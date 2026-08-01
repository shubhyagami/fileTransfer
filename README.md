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
|------|-----

---

## ⏳ Contributing (TVA Edition)

Welcome, Variant! You’ve stumbled upon the **Sacred Timeline of fileTransfer**. Before you submit a pull request, the **Time Variance Authority** requires you to follow these protocols:

### 📜 The Sacred Rules

1. **File a Nexus Event**  
   Before coding, open an issue describing the anomaly you wish to fix or feature you want to add. This prevents timeline branches from diverging.

2. **Reset Your Timeline**  
   Fork the repo and create a branch with a temporal name:  
   `git checkout -b fix/chrono-bug-1234` or `feat/quantum-upload`.

3. **Prune with Purpose**  
   Keep commits clean and atomic. No temporal dust — each commit should tell a story that Mobius M. Mobius would approve of.

4. **Minutemen Code Style**  
   - Use `black` (the official TVA formatter) to lint your code.  
   - Write docstrings that even a Loki variant could understand.  
   - Follow the existing encryption standards — we don’t need another apocalypse.

5. **Test at t

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or later
- OpenSSL (for key generation, optional)

### Installation
```bash
# Clone the repository
git clone https://github.com/shubhyagami/fileTransfer.git
cd fileTransfer

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

### Sending a File
```bash
# Start the receiver (listener) first
python fileTransfer.py receive --port 9000

# In another terminal, send the file
python fileTransfer.py send --file secret.pdf --host <receiver_ip> --port 9000
```

> ⚠️ Replace `<receiver_ip>` with the actual IP address of the receiving machine.  
> For first-time transfers, you’ll be guided through an ephemeral key exchange.

---

## 💡 Pro Tips

- **Use a VPN or Tailscale** for transfers across untrusted networks – adds an extra layer of obfuscation.
- **Transfer directories** by archiving them first: `tar -czf data.tar.gz ./folder` then send the archive.
- **Resume interrupted transfers**? Not yet built-in – but keep an eye on the `resume` branch for upcoming support.
- **Verify file integrity** after transfer: `sha256sum received_file` and compare with the sender’s hash.
- **Bandwidth limiting** can be done via `trickle` or `pv` – e.g., `pv --rate-limit 1m | python fileTransfer.py receive ...`

---

## 📅 Changelog – 2026-08-02

### Added
- **Quick Start section** in README – new users can now get up and running in under a minute.
- **Pro Tips section** – curated advice for power users and paranoid operators.
- **Changelog** – because even the TVA needs a record of timeline adjustments.

### Fixed
- (No code changes today – just documentation pruning.)

---

## 🧠 Weekly Highlight

> *“The only secure file transfer is one that never touches a third party.”*  
> — Mobius M. Mobius, TVA Temporal Engineer (paraphrased)

This week we celebrate **zero-trust architecture**: every byte you send with `fileTransfer` stays encrypted from your keyboard to their disk. No cloud, no logs, no regrets.

---

*Maintained with ⏳ by the TVA Temporal Engineering team.*  
*Prune responsibly.*