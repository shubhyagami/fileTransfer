[K[2m  [2mmodel z-ai/glm-5.3-flash failed, trying next...[0m[0m
[K[2m  [2mmodel deepseek-ai/deepseek-v4.1-flash failed, trying next...[0m[0m
# fileTransfer

Secure, lightweight, pure‑Python peer‑to‑peer file transfer.

[![PyPI version](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)
[![Python versions](https://img.shields.io/pypi/pyversions/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![CI](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml/badge.svg?branch=main&style=flat-square)](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/codecov/c/github/shubhyagami/fileTransfer/main?label=coverage&style=flat-square)](https://codecov.io/gh/shubhyagami/fileTransfer)

---

## Overview

`fileTransfer` is a command‑line tool that sends and receives files over raw TCP with optional WebSocket relaying for NAT traversal. All traffic is end‑to‑end encrypted with AES‑256‑GCM and authenticated with Ed25519 signatures.

### Key features

- **Secure** – AES‑256‑GCM encryption + Ed25519 signatures
- **Resumable** – interrupted transfers can be continued from where they stopped
- **Audit trail** – chronological logs are kept automatically
- **Cross‑platform** – works on Linux, macOS, Windows (including WSL) with any Python 3.8+ interpreter
- **Pluggable hooks** – run custom scripts before and after transfers
- **WebSocket relay** – fallback transport for peers behind NAT
- **Adjustable chunk size** – tune throughput on high‑speed links

---

## Quick start

```bash
# Install
pip install filetransfer

# Create your identity keys
filetransfer init --identity alice

# Start listening for incoming files
filetransfer receive --port 4242 --output ./downloads

# Send a file to a remote peer
filetransfer send \
  --file ./report.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519

# Resume an interrupted transfer
filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession
```

Run `filetransfer <command> --help` to see all options for a command.

---

## Commands

| Command | What it does |
|---------|--------------|
| `init`  | Generate or refresh an Ed25519 identity key pair |
| `send`  | Transfer a file to a remote peer |
| `receive` | Listen for incoming file transfers |
| `resume` | Continue a stalled transfer using a session file |
| `relay` | Manage WebSocket relay nodes (`list`, `add`, `remove`) |
| `audit` | Query or generate transfer audit logs |
| `hook`  | Register or list custom pre/post‑transfer scripts |

---

## Advanced usage

### Chunk size

On fast links, increase the chunk size for better throughput:

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

## Configuration layout

```text
~/.filetransfer/
├── keys/        # Public/private Ed25519 key pairs
├── sessions/    # Persisted session files for resumable transfers
└── audit/       # Transfer logs
```

---

## Development

```bash
# Supported Python versions
# 3.8 … 3.13

# Run the tests
pytest

# Format the code
black .
```

---

## Changelog

### v3.1.0 (2026‑09‑28)

- Minor bug fixes in session resumption
- Updated documentation examples

### v3.0.0 (2026‑09‑10)

- Added WebSocket relay support
- Introduced `relay` subcommand
- Updated encryption defaults

### v2.1.0 (2026‑08‑05)

- Added SHA‑3‑512 integrity checks
- Added `relay list` command
- Increased default chunk size to 8 MiB
- Fixed race conditions on Windows/WSL

---

## Contributing

1. Fork the repo and create a feature branch (e.g., `feat/…` or `fix/…`).
2. Format the code with `black .`.
3. Run tests with `pytest` and ensure coverage ≥ 90 %.
4. Submit a pull request with a descriptive title and explanation.

---

## License

MIT – see the bundled [LICENSE](LICENSE).
