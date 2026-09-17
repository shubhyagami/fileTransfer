[K[2m  [2mmodel openai/gpt-oss-20b failed, trying next...[0m[0m
[K[2m  [2mmodel openai/gpt-oss-120b failed, trying next...[0m[0m
# fileTransfer

A lightweight, pure-Python command-line tool for secure peer-to-peer file transfers over TCP. It supports optional WebSocket relays for NAT traversal and an optional central relay server.

[![PyPI version](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)
[![Python versions](https://img.shields.io/pypi/pyversions/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![CI Status](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml/badge.svg?branch=main&style=flat-square)](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/codecov/c/gh/shubhyagami/fileTransfer/main?label=coverage&style=flat-square)](https://app.codecov.io/gh/shubhyagami/fileTransfer)

---

## 🚀 Getting Started

### Installation
Install the package via pip:
```bash
pip install filetransfer
```

### Initial Setup
Generate your identity key pair to begin secure communications:
```bash
filetransfer init --identity alice
```
Share your public key (`~/.filetransfer/keys/alice_public.ed25519`) with the peer you intend to transfer files to.

### Basic Usage

**To receive a file:**
Run this on the destination machine to listen for incoming transfers.
```bash
filetransfer receive --port 4242 --output ./downloads/
```

**To send a file:**
```bash
filetransfer send \
  --file ./document.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

**To resume a stalled transfer:**
If a connection is interrupted, use the session file to pick up where you left off.
```bash
filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession
```

---

## ✨ Features

- **End-to-End Encryption**: AES-256-GCM for payload encryption and Ed25519 for authentication and integrity.
- **Flexible Connectivity**: Direct P2P via TCP, with optional WebSocket relay support.
- **Resumable Transfers**: State is persisted to session files to handle network instability.
- **Cross-Platform**: Full support for Linux, macOS, Windows, and WSL.
- **Extensible**: Integrated hooks to execute custom scripts before or after transfers.
- **Auditability**: Built-in logging for all transfers, accessible via `filetransfer audit`.

---

## ⚙️ Command Reference

| Command | Description |
|---------|-------------|
| `init`   | Generate or refresh identity key pairs |
| `send`   | Transfer a file to a remote peer |
| `receive`| Listen for incoming file transfers |
| `resume` | Continue an interrupted transfer from a session file |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`) |
| `audit`  | Query or generate transfer audit logs |

*For detailed options, run `filetransfer <command> --help`.*

---

## 🔧 Advanced Usage

### Optimizing Performance
Adjust the chunk size for high-bandwidth connections (e.g., 16 MiB):
```bash
filetransfer send --chunk-size 16777216 --file report.pdf ...
```

### Using a Relay Server
Bypass firewalls or NATs by using a WebSocket relay:
```bash
filetransfer send \
  --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

### Custom Audit Logging
Specify a custom path for the transfer log:
```bash
filetransfer receive --port 4242 --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## 📁 Directory Structure

The tool maintains its state in the following directory:
```
~/.filetransfer/
├─ keys/        # Public and private Ed25519 key pairs
├─ sessions/    # Session files for resuming transfers
└─ audit/       # Transfer history and audit logs
```

---

## 📝 Changelog

### v3.0.0 (2026-09-10)
- Added encrypted relay connections.
- Introduced `key` command for seamless key rotation.
- Overhauled documentation.

### v2.1.0 (2026-08-05)
- Implemented SHA-3-512 for enhanced integrity verification.
- Added `relay list` command.
- Increased default chunk size to 8 MiB.
- Fixed race conditions in multi-peer transfers and Windows Unicode path handling.

### v2.0.0 (2026-04-12)
- Completely reimplemented session persistence for transfers.
- Migrated key handling to the `cryptography` library.
- Added official support for WSL.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository and create a feature branch (`feat/...` or `fix/...`).
2. Ensure code style consistency by running `black .` before committing.
3. Ensure the test suite passes with `pytest` (minimum 90% coverage required).
4. Submit a pull request with a clear description and linked issue.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more details.
