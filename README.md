# fileTransfer

A peer‑to‑peer file‑transfer utility that moves data directly between trusted parties without relying on cloud services. All transfers are end‑to‑end encrypted and authenticated, guaranteeing confidentiality and integrity.

---

## Badges

[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/downloads/)  
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)](https://github.com/psf/black)  
[![Tests](https://img.shields.io/badge/tests-passing-success?style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)  
[![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)  
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)  
[![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)

---

## Overview

`filetransfer` is a lightweight command‑line tool written in Python that enables direct, encrypted transfers between two parties. It uses AES‑256‑GCM for confidentiality, Ed25519 for mutual authentication, and supports resumable sessions, progress reporting, and a simple plugin system.

---

## Key Features

- **End‑to‑End Encryption** – AES‑256‑GCM with per‑transfer keys.  
- **Peer‑to‑Peer Architecture** – No cloud intermediary; connections are established directly.  
- **High‑Performance Chunking** – Optimized chunk sizes for fast transfers on typical networks.  
- **Identity Verification** – Mutual authentication via Ed25519 keys prevents MITM attacks.  
- **Resumable Transfers** – Sessions can be paused and resumed after interruptions.  
- **Progress Reporting** – Real‑time ETA, throughput, and integrity checks.  
- **Plugin System** – Hook into pre‑ and post‑transfer events.  
- **Cross‑Platform** – Runs on Linux, macOS, Windows, and WSL.

---

## Getting Started

### Installation

```bash
pip install filetransfer
```

### Initialize Your Identity

Generate an Ed25519 key pair for your local identity:

```bash
filetransfer init --identity <your_username>
```

Keys are stored in `~/.filetransfer/keys/`. Keep the private key secure and share the public key with peers.

### Send a File

```bash
filetransfer send --file ./document.pdf \
  --to <recipient_username>@<recipient_ip>:4242 \
  --key ~/.filetransfer/keys/<recipient_username>_public.ed25519
```

### Receive a File

```bash
filetransfer receive --port 4242 --output ./downloads/
```

---

## Command‑Line Reference

| Command | Description |
|---------|-------------|
| `filetransfer send` | Transmit a file to a remote peer. |
| `filetransfer receive` | Listen for incoming transfers. |
| `filetransfer resume` | Continue a previously interrupted transfer. |
| `filetransfer relay list` | Discover and rank available relay nodes. |
| `filetransfer init` | Create or refresh your identity keys. |

---

## Advanced Usage

### Large File Optimization

For files larger than 1 GB, you can adjust the chunk size to improve throughput:

```bash
filetransfer send --file massive_dataset.zip \
  --to bob.example.com:4242 \
  --chunk-size 16777216
```

### Resuming Interrupted Transfers

If a connection drops, resume using the saved session manifest:

```bash
filetransfer resume --session ~/.filetransfer/sessions/<session_id>.ftsession
```

### NAT Traversal (Relay Mode)

When direct P2P connectivity fails (e.g., behind restrictive NATs), enable relay routing:

```bash
filetransfer send --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

*Relay mode forwards encrypted packets only; the relay never decrypts the payload.*

### Auditing and Logging

Log each session for compliance or audit trails:

```bash
filetransfer receive --port 4242 --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## Contributing

Contributions are welcome. To keep the workflow consistent:

1. **Open an Issue** – Describe the bug or feature before starting work.  
2. **Fork and Branch** – Use a descriptive branch name (e.g., `fix/session-sync` or `feat/relay-discovery`).  
3. **Follow Code Standards** – Run `black` to format and adhere to existing style.  
4. **Run Tests** – Ensure all tests pass and coverage stays above 90%:

   ```bash
   pytest tests/ --cov=filetransfer --cov-report=term-missing
   ```

5. **Submit a Pull Request** – Include a clear description of changes and reference the original issue.

---

## Project Metrics

| Metric               | Value |
|----------------------|-------|
| Repository size      | 4.2 MB |
| Python source lines  | 3,187 |
| Test coverage        | 94.6 % |
| Latest release       | v2.1.0 (2026‑08‑05) |
| Supported platforms  | Linux · macOS · Windows · WSL |
| Cipher suite         | AES‑256‑GCM · Ed25519 · SHA‑3‑512 |

---

## Changelog

### v2.1.0 — 2026‑08‑05

**Added**
- Native SHA‑3 integrity verification alongside SHA‑256.  
- `filetransfer relay list` to automatically discover the fastest relay nodes.

**Changed**
- Default chunk size increased from 4 MiB to 8 MiB for better high‑latency performance.  
- Read receipts now embed checksum metadata for streaming integrity checks.

**Fixed**
- Resolved a race condition in multi‑peer transfers that could desynchronize session manifests.  
- Patched a key‑rotation edge case that dropped active handoff connections.  
- Fixed Windows path normalization for Unicode file names.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
