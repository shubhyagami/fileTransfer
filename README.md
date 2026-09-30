# fileTransfer

Secure, lightweight, pure-Python peer-to-peer file transfer.

[![PyPI version](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)
[![Python versions](https://img.shields.io/pypi/pyversions/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![CI](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml/badge.svg?branch=main&style=flat-square)](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/codecov/c/github/shubhyagami/fileTransfer/main?label=coverage&style=flat-square)](https://codecov.io/gh/shubhyagami/fileTransfer)

---

## Overview

`fileTransfer` is a command-line utility that sends files directly between machines over raw TCP. All traffic is end-to-end encrypted with AES-256-GCM, and peers are authenticated with Ed25519 signatures. When a direct connection isn't possible (for example, both peers behind NAT), transfers can be routed through a WebSocket relay without losing end-to-end encryption.

### Features

- **End-to-end encryption** – AES-256-GCM with Ed25519 peer authentication
- **Resumable transfers** – continue interrupted transfers from a session file
- **Audit trail** – chronological transfer logs kept automatically
- **WebSocket relay** – fallback transport for peers behind NAT
- **Pluggable hooks** – run custom scripts before and after transfers
- **Tunable chunk size** – adjust throughput on high-speed links
- **Cross-platform** – Linux, macOS, and Windows (including WSL), Python 3.8+

---

## Installation

```bash
pip install filetransfer
```

Requires Python 3.8 or newer.

---

## Getting started

```bash
# Generate your identity keys
filetransfer init --identity alice

# Listen for incoming files
filetransfer receive --port 4242 --output ./downloads

# Send a file to a remote peer
filetransfer send \
  --file ./report.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519

# Resume an interrupted transfer
filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession
```

Run `filetransfer <command> --help` for the full list of options for each command.

---

## Commands

| Command | Description |
|---------|-------------|
| `init` | Generate or refresh an Ed25519 identity key pair |
| `send` | Transfer a file to a remote peer |
| `receive` | Listen for incoming file transfers |
| `resume` | Continue a stalled transfer from a session file |
| `relay` | Manage WebSocket relay nodes (`list`, `add`, `remove`) |
| `audit` | Query or export transfer audit logs |
| `hook` | Register or list pre-/post-transfer scripts |

---

## Advanced usage

### Larger chunk sizes

On fast local networks, increasing the chunk size can improve throughput:

```bash
filetransfer send \
  --file report.pdf \
  --to bob@203.0.113.5:4242 \
  --chunk-size 16777216
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
├── keys/       # Ed25519 public/private key pairs
├── sessions/   # Session files for resumable transfers
└── audit/      # Transfer logs
```

---

## Development

Python 3.8–3.13 are supported and tested.

```bash
# Run the test suite
pytest

# Format the code
black .
```

---

## Changelog

### v3.1.0 – 2026-09-28
- Fixed minor bugs in session resumption
- Updated documentation examples

### v3.0.0 – 2026-09-10
- Added WebSocket relay support and the `relay` sub-command
- Updated encryption defaults

### v2.1.0 – 2026-08-05
- Added SHA-3-512 integrity checks
- Added `relay list`
- Increased default chunk size to 8 MiB
- Fixed race conditions on Windows/WSL

---

## Contributing

1. Fork the repository and create a feature branch (`feat/...` or `fix/...`).
2. Format your changes with `black .`.
3. Run the test suite with `pytest` and keep coverage at or above 90%.
4. Open a pull request with a descriptive title and explanation.

---

## License

MIT – see [LICENSE](LICENSE).
