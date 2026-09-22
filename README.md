# fileTransfer

Secure, lightweight, pure‑Python peer‑to‑peer file transfer.

---

## 📦 Badges

![PyPI version](https://img.shields.io/pypi/v/filetransfer?style=flat-square)
![Python versions](https://img.shields.io/pypi/pyversions/filetransfer?style=flat-square)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)
![CI status](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml/badge.svg?branch=main&style=flat-square)
![Code coverage](https://img.shields.io/codecov/c/gh/shubhyagami/fileTransfer/main?label=coverage&style=flat-square)

---

## 📄 Overview

`fileTransfer` is a command‑line tool that lets you send and receive files directly between two machines over a TCP connection.  
All data is end‑to‑end encrypted with AES‑256‑GCM and authenticated with Ed25519.  
The tool also supports resumable sessions, optional WebSocket relays for NAT traversal, and audit logging.

---

## 🚀 Getting Started

### 1️⃣ Install

```bash
pip install filetransfer
```

### 2️⃣ Create an identity

```bash
filetransfer init --identity alice
```

Your key pair is stored in `~/.filetransfer/keys/`.  
Share `~/.filetransfer/keys/alice_public.ed25519` with the person you want to talk to.

### 3️⃣ Listen for incoming transfers

```bash
filetransfer receive --port 4242 --output ./downloads
```

The command now blocks until a transfer completes. Press `Ctrl‑C` to stop listening.

### 4️⃣ Send a file

```bash
filetransfer send \
  --file ./report.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

### 5️⃣ Resume a stalled transfer

```bash
filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession
```

---

## ✨ Features

| Feature | What it does |
|---------|--------------|
| **End‑to‑end encryption** | AES‑256‑GCM payload encryption + Ed25519 authentication |
| **Direct or relay transport** | Plain TCP by default; optional WebSocket relay for NAT traversal |
| **Resumable sessions** | Persisted session files let you continue interrupted transfers |
| **Cross‑platform** | Works on Linux, macOS, Windows, and WSL |
| **Extensible hooks** | Run custom scripts before or after a transfer |
| **Audit logging** | `filetransfer audit` prints a chronological transfer history |
| **High‑bandwidth tuning** | Adjust chunk size for optimal throughput |

---

## 📑 Commands

| Command | Purpose |
|---------|---------|
| `init` | Generate or refresh an identity key pair |
| `send` | Transfer a file to a remote peer |
| `receive` | Listen for incoming file transfers |
| `resume` | Continue an interrupted transfer using a session file |
| `relay` | Manage relay nodes (`list`, `add`, `remove`) |
| `audit` | Query or generate transfer audit logs |

Run `filetransfer <command> --help` for full options.

---

## ⚙️ Advanced usage

### Chunk size

Increase the size on fast links:

```bash
filetransfer send --chunk-size 16777216 --file report.pdf ...
```

### WebSocket relay

```bash
filetransfer send \
  --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

### Custom audit log path

```bash
filetransfer receive \
  --port 4242 \
  --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## 📁 Directory layout

```text
~/.filetransfer/
├── keys/        # Public/private Ed25519 key pairs
├── sessions/   # Persisted session files
└── audit/      # Transfer logs
```

---

## 🔧 Changelog

### v3.0.0 (2026‑09‑10)

- Added WebSocket relay support
- New `key` subcommand for key rotation
- Documentation overhaul

### v2.1.0 (2026‑08‑05)

- SHA‑3‑512 integrity checks
- `relay list` introduced
- Default chunk size increased to 8 MiB
- Fixed Windows/WSL race conditions

---

## 🤝 Contributing

1. Fork the repo, create a feature branch (`feat/...` or `fix/...`).
2. Format the code with `black .`.
3. Run tests (`pytest`) and ensure coverage ≥ 90 %.
4. Submit a PR with a clear title and description.

---

## 📜 License

MIT – see the bundled [LICENSE](LICENSE).
