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
[![Code Style](https://img.shields.io/badge/code%20style-black-000000?style=flat-square&logo=python)](https://github.com/psf/black)
[![Contributors](https://img.shields.io/badge/contributors-7-orange?style=flat-square)](https://github.com/shubhyagami/fileTransfer/graphs/contributors)
[![Commit Activity](https://img.shields.io/badge/commits-1.2k-blueviolet?style=flat-square)](https://github.com/shubhyagami/fileTransfer/commits)

---

> **`fileTransfer`** is a **secure, end-to-end encrypted file transfer utility** written in Python.  
> No cloud, no middlemen — just direct, authenticated, and encrypted file sharing between peers.  
> Because your data deserves a private highway, not a public postcard.

---

## 🚀 Features

| Icon | Feature | Description |
|------|---------|-------------|
| 🔐 | **End-to-End Encryption** | AES-256-GCM encryption ensures only intended recipients can read transferred files. |
| 🌌 | **Peer-to-Peer Architecture** | Direct connections mean zero cloud dependencies and total ownership of your data. |
| ⚡ | **High-Speed Transfers** | Optimized chunking algorithm achieves gigabit speeds on standard connections. |
| 🛡️ | **Identity Verification** | Mutual authentication via Ed25519 key exchange prevents man-in-the-middle attacks. |
| 📊 | **Progress Streaming** | Real-time transfer metrics with ETA, throughput, and integrity checks. |
| 🧩 | **Plugin System** | Extend functionality with custom hooks for pre/post-transfer operations. |
| 🖥️ | **Cross-Platform** | Runs natively on Linux, macOS, Windows, and WSL environments. |

---

## 🧭 Quick Start Guide

Ready to send files through the Sacred Timeline? Here's how to get moving in minutes:

### 1. Install from PyPI

```bash
pip install filetransfer
```

### 2. Generate Your Identity Keys

```bash
filetransfer init --identity alice
```

This creates a pair of Ed25519 keys stored locally in `~/.filetransfer/keys/`. Share your public key with trusted peers — keep your private key safe.

### 3. Receive a File

```bash
filetransfer receive --port 4242 --output ./downloads/
```

### 4. Send a File

```bash
filetransfer send --file ./secret_plans.pdf \
  --to bob.example.com:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

### 5. Verify Integrity

After every successful transfer, `fileTransfer` performs an automatic SHA-3-512 hash verification. You'll see:

```
✓ Transfer complete | Integrity verified | 42.7 MB in 3.2s (13.3 MB/s)
```

---

## ⏳ Contributing (TVA Edition)

Welcome, Variant! You've stumbled upon the **Sacred Timeline of fileTransfer**. Before you submit a pull request, the **Time Variance Authority** requires you to follow these protocols:

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
   - Follow the existing encryption standards — we don't need another apocalypse.

5. **Test at the End of Time**  
   Run all tests locally before submitting:  
   ```bash
   pytest tests/ --cov=filetransfer --cov-report=term-missing
   ```
   Coverage must remain above 90%. The TVA tolerates no loopholes.

6. **Submit for Chronological Approval**  
   Open your PR with a clear description of what timeline you've altered and why. Link the original issue. A TVA engineer will review and prune.

---

## 💡 Pro Tips from the TVA Engineers

### 🔧 Optimize for Large Transfers

For files exceeding 1 GB, tune your chunk size to reduce overhead:

```bash
filetransfer send --file massive_dataset.zip \
  --to bob.example.com:4242 \
  --chunk-size 16777216  # 16 MB chunks
```

### 🔁 Resume Interrupted Transfers

Sacred Timelines sometimes get pruned mid-transfer. Resume gracefully:

```bash
filetransfer resume --session ~/.filetransfer/sessions/abc123.ftsession
```

### 🌐 Behind NAT? Use Relay Mode

If direct P2P fails due to NAT restrictions, enable the TVA relay:

```bash
filetransfer send --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

> ⚠️ **Note**: Relay mode never decrypts your payload — it simply forwards encrypted packets. Your data stays opaque to the relay.

### 📜 Audit Every Transfer

Log all sessions for compliance:

```bash
filetransfer receive --port 4242 --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## 📈 Project Metrics

| Metric | Value |
|--------|-------|
| 📦 Repository size | 4.2 MB |
| 🐍 Lines of Python | 3,187 |
| 🧪 Test coverage | 94.6% |
| 🔄 Latest release | v2.1.0 "Sylvie" |
| 🌍 Translations | EN, FR, DE, JP |
| ⚙️ Supported platforms | Linux · macOS · Windows · WSL |
| 🔐 Cipher suite | AES-256-GCM · Ed25519 · SHA-3-512 |

---

## 🗓️ Changelog

### [v2.1.0] — Crystal Chronicle — 2026-08-05

**Fixed**
- Resolved a recurring race condition during simultaneous multi-peer transfers that caused session manifests to desynchronize.
- Patched an edge case where Ed25519 key rotation at runtime dropped the active handoff connection.
- Fixed Windows path normalization issue for files containing Unicode characters.

**Added**
- Native support for SHA-3 integrity verification alongside existing SHA-256 hashing.
- New `filetransfer relay list` subcommand to discover the fastest TVA relay nodes automatically.
- French (`fr-FR`) localization fully integrated.

**Changed**
- Default chunk size increased from 4 MB → 8 MB for improved throughput on high-latency links.
- Read receipts now include checksum metadata for real-time integrity streaming.
- Logging verbosity in development mode now prints trace IDs that are compatible with OpenTelemetry.

---

## 🌟 Weekly Highlight — Citizen 42 Award

Each week we honour the Variant who has made the most meaningful contribution to keeping the timeline intact.

**This week's pruned branch:**  
**@he_who_remains_jr** — For implementing the chunk-size auto-tuner in PR #314 that improved WAN transfer speeds by 37%. Mobius personally delivered the commendation.

> *"They'll never see it coming. And neither will the TVA."* — He Who Remains Jr., probably.

---

## 📝 License

This project is licensed under the **MIT License**, because even variants deserve freedom.

See [LICENSE](LICENSE) for full text.

---

<p align="center">
  <em>“For all time. Always.”</em><br>
  <strong>fileTransfer</strong> — Because what good is a timeline if you can't share files across it?
</p>