# fileTransfer

A lightweight, pure‑Python command‑line tool for secure peer‑to‑peer file transfer over TCP, with an optional WebSocket relay and optional central relay server.

---

## 📦 Badges

[![PyPI version](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)
[![Python versions](https://img.shields.io/pypi/pyversions/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![CI Status](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml/badge.svg?branch=main&style=flat-square)](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/codecov/c/gh/shubhyagami/fileTransfer/main?label=coverage&style=flat-square)](https://app.codecov.io/gh/shubhyagami/fileTransfer)

---

## 🚀 Getting Started

```bash
# Install from PyPI
pip install filetransfer
```

```bash
# Generate a key pair named “alice”
filetransfer init --identity alice
```

Share `~/.filetransfer/keys/alice_public.ed25519` with the peer you want to transfer files to.

```bash
# Send a file
filetransfer send \
  --file ./document.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

```bash
# Receive a file
filetransfer receive \
  --port 4242 \
  --output ./downloads/
```

To resume a stalled transfer:

```bash
filetransfer resume \
  --session ~/.filetransfer/sessions/<id>.ftsession
```

---

## 📚 Features

| Feature | Description |
|---------|-------------|
| **End‑to‑end encryption** | AES‑256‑GCM for payload, Ed25519 for authentication and integrity |
| **Direct P2P** | Uses TCP; a WebSocket relay is optional and requires no central server |
| **Resumable transfers** | Session files allow pause/resume |
| **Cross‑platform** | Works on Linux, macOS, Windows, WSL |
| **Hooks** | Run custom scripts before/after a transfer |
| **Audit logging** | Automatic, viewable via `filetransfer audit` |

---

## 📁 Configuration

```
~/.filetransfer/
├─ keys/        # Public / private key pairs
├─ sessions/    # Session files for resumable transfers
└─ audit/        # Audit logs
```

---

## ⚙️ Command Reference

| Command | Purpose |
|---------|---------|
| `init`   | Generate or refresh a key pair |
| `send`   | Transfer a file to a remote peer |
| `receive`| Listen for incoming transfers |
| `resume` | Continue an interrupted transfer |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`) |
| `audit`  | Query or generate audit logs |

Run `filetransfer <cmd> --help` for detailed options.

---

## 🔧 Advanced Usage

### Chunk size

```bash
filetransfer send --chunk-size 16777216 --file report.pdf …
```

### Relay server

```bash
filetransfer send \
  --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

### Custom audit log location

```bash
filetransfer receive \
  --port 4242 \
  --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## 📄 Changelog (excerpt)

### v3.0.0 – 2026‑09‑10
* Encrypted relay connections
* `key` command for key rotation
* Updated documentation

### v2.1.0 – 2026‑08‑05
* SHA‑3‑512 integrity verification
* `relay list` command
* Default chunk size increased to 8 MiB
* Fixed race condition in multi‑peer transfers
* Unicode path handling fixed on Windows

### v2.0.0 – 2026‑04‑12
* Reimplemented session persistence for resumable transfers
* Updated key handling to use `cryptography`
* Added WSL support

---

## 🤝 Contributing

1. Fork the repo and create a feature branch (`feat/...` or `fix/...`).
2. Follow the style guidelines – run `black .` before committing.
3. Run the test suite with `pytest` and keep coverage ≥ 90 %.
4. Open a pull request with a clear title and description, and link any related issue.

Happy hacking!

---

## 📄 License

MIT – see the [LICENSE](LICENSE) file.
