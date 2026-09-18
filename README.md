# fileTransfer

A lightweight, pure‑Python command‑line tool for secure peer‑to‑peer file transfers over TCP.  
It supports optional WebSocket relays for NAT traversal and an optional central relay server.

![PyPI version](https://img.shields.io/pypi/v/filetransfer?style=flat-square)
![Python versions](https://img.shields.io/pypi/pyversions/filetransfer?style=flat-square)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)
![CI Status](https://github.com/shubhyagami/fileTransfer/actions/workflows/ci.yml/badge.svg?branch=main&style=flat-square)
![Coverage](https://img.shields.io/codecov/c/gh/shubhyagami/fileTransfer/main?label=coverage&style=flat-square)

---

## Quickstart

### Install

```bash
pip install filetransfer
```

### Create an identity

```bash
filetransfer init --identity alice
```

`filetransfer` stores the key pair in `~/.filetransfer/keys/`.  
Share `~/.filetransfer/keys/alice_public.ed25519` with the peer you want to communicate with.

### Receive a file

```bash
filetransfer receive --port 4242 --output ./downloads
```

### Send a file

```bash
filetransfer send \
  --file ./report.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

### Resume a stalled transfer

```bash
filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession
```

---

## Features

- **End‑to‑end encryption** – AES‑256‑GCM payload encryption + Ed25519 authentication.
- **Direct or relay‑based transport** – TCP is used directly, but WebSocket relays are supported for NAT traversal.
- **Resumable transfers** – Session files allow you to pick up where you left off.
- **Cross‑platform** – Works on Linux, macOS, Windows, and WSL.
- **Extensible hooks** – Run custom scripts before or after a transfer.
- **Audit logs** – `filetransfer audit` gives a complete transfer history.

---

## Commands

| Command | Purpose |
|---------|---------|
| `init`   | Generate or refresh an identity key pair. |
| `send`   | Transfer a file to a remote peer. |
| `receive`| Listen for incoming file transfers. |
| `resume` | Continue an interrupted transfer using a session file. |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`). |
| `audit`  | Query or generate transfer audit logs. |

Run `filetransfer <command> --help` for detailed options.

---

## Advanced Tips

### Adjust chunk size

For high‑bandwidth links, a larger chunk size speeds transfer:

```bash
filetransfer send --chunk-size 16777216 --file report.pdf ...
```

### Use a WebSocket relay

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

## Directory layout

`fileTransfer` stores its data in `~/.filetransfer/`:

```
~/.filetransfer/
├─ keys/        # Public/private Ed25519 key pairs
├─ sessions/    # Persisted session files
└─ audit/       # Transfer logs
```

---

## Changelog (latest)

### v3.0.0 (2026‑09‑10)

- Encrypted WebSocket relay support.
- `key` command added for key rotation.
- Documentation overhaul.

### v2.1.0 (2026‑08‑05)

- SHA‑3‑512 integrity checks.
- `relay list` command.
- Default chunk size increased to 8 MiB.
- Fixed race conditions on Windows and WSL.

### v2.0.0 (2026‑04‑12)

- Complete session persistence redesign.
- Migrated key handling to `cryptography`.
- Official WSL support.

---

## Contributing

1. Fork the repo and create a feature branch (`feat/...` or `fix/...`).
2. Run `black .` to keep code style.
3. Ensure tests pass (`pytest`) – coverage ≥ 90 %.
4. Open a PR with a clear description and any related issue.

---

## License

MIT – see the bundled [LICENSE](LICENSE).
