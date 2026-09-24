[K[2m  [2mmodel deepseek-ai/deepseek-v4.1-flash failed, trying next...[0m[0m
# fileTransfer

Secure, lightweight, pure‑Python peer‑to‑peer file transfer.

---

## 📦 Badges

![PyPI version](https://img.shields.io/pypi/v/filetransfer?style=flat-square)  
![Python versions](https://img.shields.io/pypi/pyversions/filetransfer?style=flat-square)  
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)  
![CI](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml/badge.svg?branch=main&style=flat-square)  
![Coverage](https://img.shields.io/codecov/c/gh/shubhyagami/fileTransfer/main?label=coverage&style=flat-square)

---

## 📄 Overview

`fileTransfer` is a command‑line tool that lets you **send and receive files directly over a TCP connection**.  
All traffic is end‑to‑end encrypted with **AES‑256‑GCM** and authenticated with **Ed25519**.  

Key features:

- **Direct or relay transport** – plain TCP by default, or a WebSocket relay for NAT traversal.  
- **Resumable sessions** – interrupted transfers can be restarted from where they left off.  
- **Audit logging** – a chronological record of all transfers is kept automatically.  
- **Cross‑platform** – works on Linux, macOS, Windows (including WSL), and any Python 3.8+ interpreter.  

---

## 🚀 Quick start

```bash
# Install the package
pip install filetransfer

# Create your identity key pair
filetransfer init --identity alice

# Listen for incoming transfers (replace with your own port if needed)
filetransfer receive --port 4242 --output ./downloads

# Send a file to a remote peer
filetransfer send \
  --file ./report.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

> **Tip** – To resume a stalled transfer, run  
> `filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession`

---

## ✨ Features

- **End‑to‑end encryption** – payloads are encrypted with AES‑256‑GCM; traffic is authenticated with Ed25519 signatures.  
- **Direct & relayed transport** – fallback to a WebSocket relay for peers behind NAT.  
- **Resumable sessions** – session files are persisted in `~/.filetransfer/sessions/`.  
- **Audit trail** – transfer logs are stored under `~/.filetransfer/audit/`.  
- **Extensible hooks** – run custom scripts before or after any transfer.  
- **Adjustable chunk size** – tweak bandwidth on high‑speed links.  

---

## 📑 Commands

| Command | Purpose |
|---------|---------|
| `init`   | Generate or refresh an identity key pair. |
| `send`   | Transfer a file to a remote peer. |
| `receive` | Listen for incoming file transfers. |
| `resume` | Continue an interrupted transfer using a session file. |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`). |
| `audit`  | Query or generate transfer audit logs. |

Run `filetransfer <command> --help` for full options.

---

## ⚙️ Advanced usage

### Chunk size

On very fast links, increase the size to boost throughput:

```bash
filetransfer send --file report.pdf --chunk-size 16777216 ...
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

## 📁 Configuration layout

```text
~/.filetransfer/
├── keys/        # Public/private Ed25519 key pairs
├── sessions/    # Persisted session files
└── audit/       # Transfer logs
```

---

## 🔧 Development

- Supported Python: 3.8 – 3.13  
- Run the test suite: `pytest`  
- Code formatting: `black .`

---

## 🔔 Changelog

### v3.0.0 (2026‑09‑10)

- Added WebSocket relay support.  
- Introduced `key` subcommand for key rotation.  
- Updated documentation and examples.

### v2.1.0 (2026‑08‑05)

- SHA‑3‑512 integrity checks.  
- New `relay list` command.  
- Default chunk size increased to 8 MiB.  
- Fixed race conditions on Windows/WSL.

---

## 🤝 Contributing

1. Fork the repository and create a feature branch (`feat/...` or `fix/...`).  
2. Format the code with `black .`.  
3. Run tests (`pytest`) and ensure coverage ≥ 90 %.  
4. Submit a pull request with a descriptive title and explanation.

---

## 📜 License

MIT – see the bundled [LICENSE](LICENSE).
