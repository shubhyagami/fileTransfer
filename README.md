# fileTransfer

A lightweight, pure‑Python command‑line tool for direct, end‑to‑end encrypted file transfers.  
All traffic is peer‑to‑peer; no cloud relay is required unless you explicitly request one.

---

## Badges

| | |
|---|---|
|![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)|![Code style](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)|
|![CI](https://img.shields.io/github/actions/workflow/status/shubhyagami/filetransfer/ci.yml?branch=main&style=flat-square)|![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)|
|![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)|![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)|

---

## Table of Contents
- [Getting Started](#getting-started)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command Reference](#command-reference)
- [Advanced Usage](#advanced-usage)
- [Contributing](#contributing)
- [Project Metrics](#project-metrics)
- [Changelog](#changelog)
- [License](#license)

---

## Getting Started

```bash
pip install filetransfer
```

Create an identity key pair:

```bash
filetransfer init --identity alice
```

Share the generated public key (`alice_public.ed25519`) with the person you want to talk to.

After receiving the peer’s public key, you can send and receive files:

```bash
filetransfer send --file report.pdf --to bob@203.0.113.5:4242 --key ~/.filetransfer/keys/bob_public.ed25519
```

```bash
filetransfer receive --port 4242 --output ./downloads/
```

---

## Features

- **End‑to‑end encryption** – AES‑256‑GCM per transfer.  
- **Mutual authentication** – Ed25519 key pairs.  
- **Peer‑to‑peer** – Direct TCP connections; no intermediary server.  
- **Resumable transfers** – Pause & resume without data loss.  
- **Live progress** – ETA, throughput, and integrity check.  
- **Chunking** – Default 8 MiB, adjustable to match bandwidth.  
- **Hooks** – Run custom scripts before/after transfers.  
- **Cross‑platform** – Linux, macOS, Windows (incl. WSL).

---

## Installation

```bash
pip install filetransfer
```

The package is available on PyPI. No binary wheels are required, so it installs and runs on any system that supports Python 3.9+.

---

## Quick Start

### 1. Initialize identity

```bash
filetransfer init --identity alice
```

Private key → `~/.filetransfer/keys/`.  
Public key → `~/.filetransfer/keys/alice_public.ed25519`.

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

## Command Reference

| Command | Purpose |
|---------|---------|
| `init` | Create or refresh a key pair. |
| `send` | Transmit a file to a remote peer. |
| `receive` | Listen for incoming file transfers. |
| `resume` | Continue an interrupted transfer. |
| `relay list` | Show available public relay nodes (if any). |

For full CLI help, run `filetransfer <command> --help`.

---

## Advanced Usage

### Chunk size

```bash
filetransfer send --chunk-size 16777216 <other options>
```

### Resuming a transfer

```bash
filetransfer resume --session ~/.filetransfer/sessions/<session_id>.ftsession
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

## Contributing

1. Fork the repo and open an issue to discuss the change.  
2. Branch using a descriptive name (`feat/...` or `fix/...`).  
3. Follow the style guide – run `black` before committing.  
4. Run the test suite (`pytest`) and keep coverage above 90 %.  
5. Submit a pull request with a clear description and a link to the issue.

---

## Project Metrics

| Metric | Value |
|--------|-------|
| Repo size | 4.2 MB |
| Python source lines | 3,187 |
| Test coverage | 94.6 % |
| Latest release | v2.1.0 (2026‑08‑05) |
| Supported platforms | Linux · macOS · Windows · WSL |
| Cipher suite | AES‑256‑GCM, Ed25519, SHA‑3‑512 |

---

## Changelog

### v2.1.0 – 2026‑08‑05

- Added SHA‑3‑512 integrity verification.  
- Introduced `relay list` command.  
- Default chunk size increased from 4 MiB to 8 MiB.  
- Fixed a race condition in multi‑peer transfers.  
- Corrected Unicode path handling on Windows.

### v2.0.0 – 2026‑04‑12

- Reimplemented session persistence for resumable transfers.  
- Updated key handling to use cryptography.io.  
- Added support for Windows Subsystem for Linux (WSL).

---

## License

MIT – see the [LICENSE](LICENSE) file.
