# fileTransfer

A lightweight, pure‑Python command‑line utility for secure peer‑to‑peer file transfer over TCP, with an optional WebSocket relay. A central server is not required unless you choose to use one.

---

## 🚀 Prerequisites

- Python 3.9 or newer
- `pip` (or any Python package manager)

---

## 📦 Installation

```bash
pip install filetransfer
```

---

## 📚 Quickstart

1. **Create an identity (key pair)**  

   ```bash
   filetransfer init --identity alice
   ```

   Generates:

   ```text
   ~/.filetransfer/keys/alice_private.ed25519
   ~/.filetransfer/keys/alice_public.ed25519
   ```

   Share `alice_public.ed25519` with the peer you want to transfer files to.

2. **Send a file**  

   ```bash
   filetransfer send \
     --file ./document.pdf \
     --to bob@203.0.113.5:4242 \
     --key ~/.filetransfer/keys/bob_public.ed25519
   ```

3. **Receive a file**  

   ```bash
   filetransfer receive \
     --port 4242 \
     --output ./downloads/
   ```

4. **Resume an interrupted transfer**  

   ```bash
   filetransfer resume \
     --session ~/.filetransfer/sessions/<id>.ftsession
   ```

---

## 📦 Features

- **End‑to‑end encryption** – AES‑256‑GCM for data, Ed25519 for authentication and integrity
- **Direct peer‑to‑peer transfer** – TCP only; WebSocket relay optional
- **Resumable transfers** – pause and resume with a session file
- **Cross‑platform** – Linux, macOS, Windows, WSL
- **Custom hooks** – execute scripts before or after a transfer
- **Audit logging** – automatic log of every transfer, viewable via the `audit` command

---

## 📁 Configuration Directory

```
~/.filetransfer/
├─ keys/        # Public/private key pairs
├─ sessions/     # Session files for resumable transfers
└─ audit/       # Audit logs
```

---

## ⚙️ Command Reference

| Command | Purpose |
|---------|---------|
| `init`  | Generate or refresh a key pair |
| `send`  | Transfer a file to a remote peer |
| `receive` | Listen for incoming transfers |
| `resume` | Continue an interrupted transfer |
| `relay`  | Manage relay nodes (`list`, `add`, `remove`) |
| `audit`  | Query or generate audit logs |

Run `filetransfer <command> --help` for detailed options.

---

## 🔧 Advanced Usage

### Custom chunk size

```bash
filetransfer send --chunk-size 16777216 --file report.pdf …
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

### v3.0.0 – 2026‑09‑10
* Added support for encrypted relay connections
* Introduced `key` command for key rotation
* Updated documentation

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

1. Fork the repository and create a branch (`feat/...` or `fix/...`).
2. Follow the code style – run `black .` before committing.
3. Run the test suite with `pytest`. Keep coverage ≥ 90 %.
4. Open a pull request with a clear description and link to any related issue.

Happy hacking!

---

## 📄 License

MIT – see the [LICENSE](LICENSE) file.
