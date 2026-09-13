# fileTransfer

A lightweight, pure‑Python command‑line tool for secure, peer‑to‑peer file transfer over TCP (with optional WebSocket relay). No central server is required unless you choose to use one.

---

## ⚙️ Prerequisites

- Python 3.9+

---

## 📦 Badges

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)  
![CI](https://img.shields.io/github/actions/workflow/status/shubhyagami/filetransfer/ci.yml?branch=main&style=flat-square)  
![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)  
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)  
![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)

---

## 🚀 Getting Started

1. **Install the package**  
   ```bash
   pip install filetransfer
   ```

2. **Create an identity (key pair)**  
   ```bash
   filetransfer init --identity alice
   ```
   *Creates*
   ```
   ~/.filetransfer/keys/alice_private.ed25519
   ~/.filetransfer/keys/alice_public.ed25519
   ```
   Share `alice_public.ed25519` with the peer you want to transfer files to.

3. **Send a file**  
   ```bash
   filetransfer send \
     --file ./document.pdf \
     --to bob@203.0.113.5:4242 \
     --key ~/.filetransfer/keys/bob_public.ed25519
   ```

4. **Receive a file**  
   ```bash
   filetransfer receive \
     --port 4242 \
     --output ./downloads/
   ```

---

## ✨ Features

| Feature                     | Description |
|-----------------------------|-------------|
| End‑to‑end encryption      | AES‑256‑GCM for data, Ed25519 for authentication and integrity |
| Direct p2p transfer         | TCP connections, optional WebSocket relay |
| Resumable transfers         | Pause and resume with a session file |
| Cross‑platform support     | Linux, macOS, Windows, WSL |
| Custom hooks                | Scripts before/after a transfer |
| Audit logging               | Automatic log of each transfer |

---

## 📁 Configuration Directory

```
~/.filetransfer/
├─ keys/        # Public/private key pairs
├─ sessions/   # Session files for resumable transfers
└─ audit/       # Audit logs
```

---

## 🛠️ Command Reference

| Command | Purpose |
|---------|---------|
| `init`  | Generate or refresh a key pair |
| `send`  | Transfer a file to a remote peer |
| `receive` | Listen for incoming transfers |
| `resume` | Continue an interrupted transfer |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`) |
| `audit`  | Generate or read audit logs |

Run `filetransfer <command> --help` for detailed options.

---

## 🔧 Advanced Usage

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

### Specify audit log location
```bash
filetransfer receive \
  --port 4242 \
  --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## 📄 Changelog (excerpt)

### v2.1.0 – 2026‑08‑05
* Added SHA‑3‑512 integrity verification  
* Introduced `relay list` command  
* Increased default chunk size to 8 MiB  
* Fixed race condition in multi‑peer transfers  
* Corrected Unicode path handling on Windows

### v2.0.0 – 2026‑04‑12
* Reimplemented session persistence for resumable transfers  
* Updated key handling to use `cryptography`  
* Added WSL support

---

## 🤝 Contributing

1. Fork the repo and create a feature or bug‑fix branch (`feat/...` or `fix/...`).  
2. Follow the code style – run `black .` before committing.  
3. Run the test suite with `pytest` and keep coverage ≥ 90 %.  
4. Open a pull request with a clear description and link to any related issue.

Happy hacking!

---

## 📄 License

MIT – see the [LICENSE](LICENSE) file.
