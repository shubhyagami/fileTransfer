# fileTransfer

A lightweight pure‑Python command‑line tool for encrypted peer‑to‑peer file transfers.  
No third‑party relay is required unless explicitly requested.

---  

## Badges

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)  
![CI](https://img.shields.io/github/actions/workflow/status/shubhyagami/filetransfer/ci.yml?branch=main&style=flat-square)  
![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)  
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)  
![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)

---  

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Command Reference](#command-reference)
5. [Advanced Usage](#advanced-usage)
6. [Contributing](#contributing)
7. [Metrics](#metrics)
8. [Changelog](#changelog)
9. [License](#license)

---  

## Overview
`fileTransfer` is a pure‑Python CLI that lets you send and receive files securely with end‑to‑end encryption.

- **End‑to‑end encryption** – AES‑256‑GCM for data, Ed25519 for authentication.  
- **Peer‑to‑peer** – Direct TCP connections; optional WebSocket relay.  
- **Resumable** – Pause and resume without data loss.  
- **Cross‑platform** – Linux, macOS, Windows (including WSL).  
- **Hooks** – Run custom scripts before or after each transfer.

---  

## Installation
```
pip install filetransfer
```
The package ships with source only; it runs wherever Python 3.9+ is available.

---  

## Quick Start

### 1. Create an identity
```
filetransfer init --identity alice
```
This creates:

```
~/.filetransfer/keys/alice_private.ed25519
~/.filetransfer/keys/alice_public.ed25519
```
Share the public key file with the peer you want to talk to.

### 2. Send a file
```
filetransfer send \
  --file ./document.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

### 3. Receive a file
```
filetransfer receive \
  --port 4242 \
  --output ./downloads/
```

---  

## Command Reference
| Command | Purpose |
|--------|---------|
| `init` | Generate or refresh a key pair. |
| `send` | Transmit a file to a remote peer. |
| `receive` | Listen for incoming transfers. |
| `resume` | Continue an interrupted transfer. |
| `relay` | Manage relay nodes (`list`, `add`, `remove`). |
| `audit` | Generate or read audit logs. |

Run `filetransfer <command> --help` for detailed options.

---  

## Advanced Usage

### Custom chunk size
```
filetransfer send --chunk-size 16777216 ...
```

### Resuming
```
filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession
```

### Using a relay server
```
filetransfer send \
  --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

### Audit logging
```
filetransfer receive \
  --port 4242 \
  --audit-log ~/.filetransfer/audit/2026-08.log
```

---  

## Contributing
1. Fork the repository and open an issue to discuss your changes.  
2. Create a topic branch (`feat/...`, `fix/...`).  
3. Follow the style guide – run `black` before committing.  
4. Run the tests (`pytest`) and keep coverage above 90 %.  
5. Submit a pull request with a clear description and a link to the issue.

---  

## Metrics
| Metric | Value |
|--------|-------|
| Repo size | 4.2 MB |
| Source lines | 3,187 |
| Test coverage | 94.6 % |
| Latest release | v2.1.0 (2026‑08‑05) |
| Platforms | Linux, macOS, Windows, WSL |
| Cipher suite | AES‑256‑GCM, Ed25519, SHA‑3‑512 |

---  

## Changelog

### v2.1.0 – 2026‑08‑05
- Added SHA‑3‑512 integrity verification.  
- Introduced `relay list` command.  
- Increased default chunk size to 8 MiB.  
- Fixed race condition in multi‑peer transfers.  
- Corrected Unicode path handling on Windows.

### v2.0.0 – 2026‑04‑12
- Reimplemented session persistence for resumable transfers.  
- Updated key handling to use `cryptography.io`.  
- Added support for Windows Subsystem for Linux (WSL).

---  

## License
MIT – see the [LICENSE](LICENSE) file.
