# fileTransfer

A lightweight, pure‑Python command‑line tool for secure, peer‑to‑peer file transfer over TCP (or an optional WebSocket relay). No central server is required unless you choose to use one.

## 📦 Badges

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)  
![CI](https://img.shields.io/github/actions/workflow/status/shubhyagami/filetransfer/ci.yml?branch=main&style=flat-square)  
![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)  
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)  
![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)

---

## 🚀 Quickstart

```bash
# Install the package
pip install filetransfer
```

```bash
# 1) Create an identity (key pair)
filetransfer init --identity alice
```

Two key files are created under `~/.filetransfer/keys/`:

```
~/.filetransfer/keys/alice_private.ed25519
~/.filetransfer/keys/alice_public.ed25519
```

Share `alice_public.ed25519` with the peer you want to transfer files to.

```bash
# 2) Send a file
filetransfer send \
  --file ./document.pdf \
  --to bob@203.0.113.5:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

```bash
# 3) Receive a file
filetransfer receive \
  --port 4242 \
  --output ./downloads/
```

---

## ⚡️ Feature Highlights

- **End‑to‑end encryption** – AES‑256‑GCM for data, Ed25519 for authentication and integrity.
- **Peer‑to‑peer architecture** – direct TCP connections with optional WebSocket relay.
- **Resumable transfers** – pause and continue with a session file.
- **Cross‑platform** – works on Linux, macOS, Windows, and WSL.
- **Custom hooks** – run scripts before or after a transfer.
- **Audit logging** – automatically record every transfer.

---

## 📦 Installation

```bash
pip install filetransfer
```

The package works with Python 3.9 or newer.

---

## 📁 Directory Layout

```
~/.filetransfer/
├─ keys/        # Public/private key pairs
├─ sessions/    # Session files for resumable transfers
└─ audit/       # Audit logs
```

---

## 🛠️ Command Reference

| Command | Description |
|---------|-------------|
| `init`   | Generate or refresh a key pair. |
| `send`   | Transfer a file to a remote peer. |
| `receive`| Listen for incoming transfers. |
| `resume` | Continue an interrupted transfer from a session file. |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`). |
| `audit`  | Generate or read audit logs. |

Run `filetransfer <command> --help` for detailed options.

---

## 🧩 Advanced Usage

### Custom chunk size

```bash
filetransfer send --chunk-size 16777216 --file report.pdf …
```

### Resume a transfer

```bash
filetransfer resume --session ~/.filetransfer/sessions/<id>.ftsession
```

### Use a relay server

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

## 📄 Changelog (latest)

### v2.1.0 – 2026‑08‑05

- Added SHA‑3‑512 integrity verification.  
- Introduced `relay list` command.  
- Increased default chunk size to 8 MiB.  
- Fixed race condition in multi‑peer transfers.  
- Corrected Unicode path handling on Windows.

### v2.0.0 – 2026‑04‑12

- Reimplemented session persistence for resumable transfers.  
- Updated key handling to use `cryptography`.  
- Added support for Windows Subsystem for Linux (WSL).

---

## 🤝 Contributing

1. Fork the repository and create a feature/fix branch (`feat/...` or `fix/...`).  
2. Follow the code style – run `black .` before committing.  
3. Run tests with `pytest`; keep coverage ≥ 90 %.  
4. Open a pull request with a clear description referencing any related issue.

Happy hacking!

---

## 📄 License

MIT – see the [LICENSE](LICENSE) file.
