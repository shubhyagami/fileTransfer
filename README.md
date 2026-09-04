# fileTransfer

A lightweight, pure‑Python command‑line tool for encrypted peer‑to‑peer file transfers.  
No third‑party relay is required unless you choose to use one.

---

## 📦 Badges

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)
![CI](https://img.shields.io/github/actions/workflow/status/shubhyagami/filetransfer/ci.yml?branch=main&style=flat-square)
![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Command Reference](#command-reference)
6. [Advanced Usage](#advanced-usage)
7. [Contributing](#contributing)
8. [Changelog](#changelog)
9. [License](#license)

---

## 🚀 Overview

`fileTransfer` encrypts your data end‑to‑end (AES‑256‑GCM for the file, Ed25519 for authentication) and transfers it over a direct TCP link.  
Optional WebSocket relays can be used when a direct connection is not possible.

Key features:

- **End‑to‑end encryption** – no back‑doors, all keys stay local.
- **Peer‑to‑peer** – no central server unless you opt‑in.
- **Resumable** – pause a transfer and pick up where you left off.
- **Cross‑platform** – works on Linux, macOS, Windows, and WSL.
- **Hooks** – run custom scripts before or after each transfer.

---

## ⚡ Getting Started

1. **Create an identity** – generate a key pair.  
2. **Share the public key** with the peer.  
3. **Send or receive** files using the CLI.

---

## 📦 Installation

```bash
pip install filetransfer
```

The package contains only source files and runs on any system with Python 3.9+.

---

## 🔄 Quick Start

### 1. Create an identity

```bash
filetransfer init --identity alice
```

This creates:

```
~/.filetransfer/keys/alice_private.ed25519
~/.filetransfer/keys/alice_public.ed25519
```

Share `alice_public.ed25519` with your peer.

### 2. Send a file

```bash
filetransfer send \
    --file ./document.pdf \
    --to bob@203.0.113.5:4242 \
    --key ~/.filetransfer/keys/bob_public.ed25519
```

### 3. Receive a file

```bash
filetransfer receive \
    --port 4242 \
    --output ./downloads/
```

---

## 📚 Command Reference

| Command | Purpose |
|---------|---------|
| `init`   | Generate or refresh a key pair. |
| `send`   | Transmit a file to a remote peer. |
| `receive`| Listen for incoming transfers. |
| `resume` | Continue an interrupted transfer. |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`). |
| `audit`  | Generate or read audit logs. |

Run `filetransfer <command> --help` for detailed options.

---

## ⚙️ Advanced Usage

### Custom chunk size

```bash
filetransfer send --chunk-size 16777216 --file report.pdf …
```

### Resuming a transfer

```bash
filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession
```

### Using a relay server

```bash
filetransfer send \
    --file report.pdf \
    --to bob:4242 \
    --relay wss://relay.filetransfer.io
```

### Audit logging

```bash
filetransfer receive \
    --port 4242 \
    --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## 🤝 Contributing

1. Fork the repository and open an issue to discuss your idea.  
2. Branch off a topic name (`feat/...`, `fix/...`).  
3. Keep the style consistent – run `black .` before committing.  
4. Paste a test or run `pytest` and maintain coverage ≥ 90 %.  
5. Submit a pull request with a clear description and link to the issue.

---

## 📜 Changelog (latest)

### v2.1.0 – 2026‑08‑05
* Added SHA‑3‑512 integrity verification.  
* Introduced `relay list` command.  
* Increased default chunk size to 8 MiB.  
* Fixed race condition in multi‑peer transfers.  
* Corrected Unicode path handling on Windows.

### v2.0.0 – 2026‑04‑12
* Reimplemented session persistence for resumable transfers.  
* Updated key handling to use `cryptography`.  
* Added support for Windows Subsystem for Linux (WSL).

---

## 📄 License

MIT – see the [LICENSE](LICENSE) file.
