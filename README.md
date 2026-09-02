# fileTransfer

A lightweight, pure‑Python command‑line tool for secure, peer‑to‑peer file transfers.  
Files are exchanged directly, without a cloud intermediary, using AES‑256‑GCM for confidentiality and Ed25519 signatures for mutual authentication.  
Supports resumable sessions, real‑time progress reporting, and a minimal plugin system.

---

## Badges

[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![Code style](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)](https://github.com/psf/black)
[![Tests](https://img.shields.io/github/actions/workflow/status/shubhyagami/filetransfer/tests.yml?label=tests&style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)
[![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)

---

## Table of Contents

- [Getting Started](#getting-started)
- [Key Features](#key-features)
- [Installation](#installation)
- [Command Reference](#command-reference)
- [Advanced Usage](#advanced-usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Project Metrics](#project-metrics)
- [Changelog](#changelog)
- [License](#license)

---

## Getting Started

```bash
# Create a key pair for your identity
filetransfer init <username>
```

Your private key is stored in `~/.filetransfer/keys/<username>_private.ed25519`.  
Share the corresponding public key file (`<username>_public.ed25519`) with your peers.

```bash
# Send a file
filetransfer send \
  --file ./document.pdf \
  --to bob:192.168.1.10:4242 \
  --pub-key ~/.filetransfer/keys/bob_public.ed25519
```

```bash
# Receive a file
filetransfer receive --port 4242 --output ./downloads/
```

---

## Key Features

- **End‑to‑End Encryption**: AES‑256‑GCM per transfer
- **Direct P2P**: No relay unless explicitly requested
- **Chunking & Throughput**: Optimised for common network conditions (default 8 MiB)
- **Mutual Authentication**: Ed25519 key exchange protects against MITM
- **Resumable Transfers**: Pause and resume after interruptions
- **Real‑Time Progress**: ETA, throughput, integrity checks
- **Plugin Hooks**: `pre-<cmd>` and `post-<cmd>` scripts
- **Cross‑Platform**: Linux, macOS, Windows, WSL

---

## Installation

```bash
pip install filetransfer
```

Prerequisites: Python 3.9 or newer, the `cryptography`, `asyncio`, and `aiohttp` packages (installed automatically).

---

## Command Reference

| Command | Description |
|---------|-------------|
| `filetransfer init <username>` | Generate a new Ed25519 key pair |
| `filetransfer send …` | Transmit a file to a remote peer |
| `filetransfer receive …` | Listen for incoming transfers |
| `filetransfer resume …` | Continue a previously interrupted transfer |
| `filetransfer relay list` | Discover and rank public relay nodes |
| `filetransfer help <cmd>` | Show help for a specific command |

> **Tip**: Use `filetransfer help` for a full list of options and flags.

---

## Advanced Usage

### Custom Chunk Size

```bash
filetransfer send --chunk-size 16777216 …
```

### Resuming a Transfer

```bash
filetransfer resume --session ~/.filetransfer/sessions/<session_id>.ftsession
```

### Relay Mode

When a direct connection fails, forward through a WebSocket relay:

```bash
filetransfer send \
  --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

> The relay only forwards the encrypted packets; it never sees the plaintext.

### Audit Logging

```bash
filetransfer receive --port 4242 --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## Configuration

All runtime options can be set via environment variables prefixed with `FILETRANSFER_`.  
Example:

```bash
export FILETRANSFER_LOG_LEVEL=INFO
filetransfer send …
```

See `filetransfer help` for the full list of supported variables.

---

## Contributing

1. Fork the repo and create a topic branch (`feat/...` or `fix/...`).
2. Run `black --check .` and `ruff .` (or your preferred linter).
3. Run tests: `pytest tests/ --cov=filetransfer --cov-report=term-missing`.
4. Open a pull request with a concise description; reference the related issue.

---

## Project Metrics

| Metric | Value |
|--------|-------|
| Repo size | 4.2 MB |
| Python source lines | 3,187 |
| Test coverage | 94.6 % |
| Latest release | v2.1.0 (2026‑08‑05) |
| Supported platforms | Linux, macOS, Windows, WSL |
| Cipher suite | AES‑256‑GCM, Ed25519, SHA‑3‑512 |

---

## Changelog

### v2.1.0 — 2026‑08‑05

| Change | Details |
|--------|---------|
| Added | SHA‑3 integrity verification, `relay list` command |
| Changed | Default chunk size↑ from 4 MiB to 8 MiB |
| Fixed | Race condition in multi‑peer transfers, key‑rotation edge case, Unicode paths on Windows |

---

## License

MIT – see the [LICENSE](LICENSE) file.
