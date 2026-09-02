# fileTransfer

A lightweight, pure‑Python command‑line tool for direct, end‑to‑end encrypted file transfers.  
All traffic is peer‑to‑peer, no cloud‑based relay is required unless explicitly requested.

---

## Badges

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/downloads/)  
[![Code style](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)](https://github.com/psf/black)  
[![CI](https://img.shields.io/github/actions/workflow/status/shubhyagami/filetransfer/ci.yml?branch=main&style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)  
[![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)  
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)  
[![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)

---

## About

`filetransfer` is a pure‑Python CLI that lets two parties exchange files securely and efficiently, without relying on a centralized server.  
- **Encryption** – AES‑256‑GCM per transfer.  
- **Authentication** – Ed25519 signatures prevent man‑in‑the‑middle attacks.  
- **Resumable** – Transfers can be paused and resumed.  
- **Progress reporting** – Real‑time ETA and throughput.  
- **Extensible** – Hook system for pre‑ and post‑transfer scripts.  
- **Cross‑platform** – Runs on Linux, macOS, Windows, and WSL.

---

## Key Features

- **End‑to‑end encryption** – AES‑256‑GCM with a fresh key for each session.  
- **Direct P2P** – Establishes a TCP connection straight between peers.  
- **Optimised chunking** – Default 8 MiB, adjustable for bandwidth.  
- **Mutual authentication** – Ed25519 key pairs verify identities.  
- **Resumable transfers** – Pause and continue seamlessly.  
- **Live progress** – ETA, throughput, and integrity checks.  
- **Hook system** – Run custom scripts before and after transfers.  
- **Cross‑platform** – Supported on Linux, macOS, Windows (including WSL).

---

## Installation

```bash
pip install filetransfer
```

The package is distributed on PyPI; no binary wheels are required.

---

## Quick Start

### 1. Create your identity

```bash
filetransfer init --identity <your_username>
```

Your private key is stored in `~/.filetransfer/keys/`.  
Share your public key (`<your_username>_public.ed25519`) with peers.

### 2. Send a file

```bash
filetransfer send \
  --file ./document.pdf \
  --to <recipient_username>@<recipient_ip>:4242 \
  --key ~/.filetransfer/keys/<recipient_username>_public.ed25519
```

### 3. Receive a file

```bash
filetransfer receive \
  --port 4242 \
  --output ./downloads/
```

---

## Command‑Line Reference

| Command                 | Description                                  |
|-------------------------|-----------------------------------------------|
| `filetransfer init`     | Create or refresh your key pair.              |
| `filetransfer send`     | Transmit a file to a remote peer.             |
| `filetransfer receive`  | Listen for incoming file transfers.           |
| `filetransfer resume`  | Continue an interrupted transfer.            |
| `filetransfer relay list` | Discover available relay nodes.              |

---

## Advanced Usage

### Adjusting Chunk Size

```bash
filetransfer send --chunk-size 16777216 <other options>
```

### Resuming a Session

```bash
filetransfer resume --session ~/.filetransfer/sessions/<session_id>.ftsession
```

### Using a Relay Server

If a direct connection cannot be established, a relay can forward encrypted packets:

```bash
filetransfer send \
  --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

### Audit Logging

```bash
filetransfer receive \
  --port 4242 \
  --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## Contributing

1. Open an issue to discuss a bug or feature.  
2. Fork the repo and create a feature or fix branch (`feat/...` or `fix/...`).  
3. Follow the style guide – run `black` before committing.  
4. Run tests (`pytest`) and keep coverage ≥ 90 %.  
5. Submit a pull request with a concise description and link to the relevant issue.

---

## Project Metrics

| Metric                 | Value                               |
|------------------------|-------------------------------------|
| Repo size              | 4.2 MB                               |
| Python source lines   | 3,187                                |
| Test coverage         | 94.6 %                               |
| Latest release         | v2.1.0 (2026‑08‑05)                 |
| Supported platforms    | Linux · macOS · Windows · WSL         |
| Cipher suite          | AES‑256‑GCM · Ed25519 · SHA‑3‑512   |

---

## Changelog

### v2.1.0 — 2026‑08‑05

- Added SHA‑3 integrity verification.  
- Introduced `relay list` command.  
- Increased default chunk size from 4 MiB to 8 MiB.  
- Fixed race condition in multi‑peer transfers.  
- Corrected Unicode path handling on Windows.

---

## License

MIT License – see the [LICENSE](LICENSE) file.
