# fileTransfer

A lightweight, pure‑Python command‑line tool that encrypts and transfers files directly between peers.

---

## 📦 Badges

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)
![CI](https://img.shields.io/github/actions/workflow/status/shubhyagami/filetransfer/ci.yml?branch=main&style=flat-square)
![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)

---

## 📋 Table of contents
1. [Overview](#overview)
2. [Quick start](#quick-start)
3. [Installation](#installation)
4. [Command reference](#command-reference)
5. [Advanced usage](#advanced-usage)
6. [Contributing](#contributing)
7. [Changelog](#changelog)
8. [License](#license)

---

## 🚀 Overview

`fileTransfer` encrypts files end‑to‑end and sends them over a direct TCP link.  
If a direct path cannot be established, an optional WebSocket relay can be used.  
No third‑party server is required unless you choose to use one.

**Key features**

* End‑to‑end encryption (AES‑256‑GCM for the file and Ed25519 for authentication)
* Peer‑to‑peer architecture – no central server unless you opt‑in
* Resumable transfers – pause and pick up where you left off
* Cross‑platform – works on Linux, macOS, Windows, and WSL
* Custom hooks – run scripts before or after a transfer
* Audit logging – keep a record of every transfer

---

## 🔄 Quick start

> **Prerequisite** – Python 3.9+ must be installed.

```bash
# Install the package
pip install filetransfer
```

### 1. Create an identity

```bash
filetransfer init --identity alice
```

This creates the following files in your home directory:

```
~/.filetransfer/keys/alice_private.ed25519
~/.filetransfer/keys/alice_public.ed25519
```

Share `alice_public.ed25519` with the peer you want to transfer files to.

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

## 📦 Installation

```bash
pip install filetransfer
```

The package is pure Python and runs on any system that has Python 3.9+.

---

## 📚 Command reference

| Command | Description |
|---------|-------------|
| `init`   | Create or refresh a key pair. |
| `send`   | Transmit a file to a remote peer. |
| `receive`| Listen for incoming transfers. |
| `resume` | Continue an interrupted transfer. |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`). |
| `audit`  | Generate or read audit logs. |

Run `filetransfer <command> --help` for a full list of options.

---

## ⚙️ Advanced usage

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

1. Fork the repo and create a branch (`feat/...` or `fix/...`).
2. Follow the code style – run `black .` before committing.
3. Run tests with `pytest`; keep coverage ≥ 90 %.
4. Push a pull request with a clear description referencing the issue.

Happy hacking!

---

## 📜 Changelog

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
