# fileTransfer

A lightweight, peer‑to‑peer command‑line tool for end‑to‑end encrypted file transfers.

---

## Badges  

[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/downloads/)  
[![Code style](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)](https://github.com/psf/black)  
[![Tests](https://img.shields.io/badge/tests-passing-success?style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)  
[![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)  
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)  
[![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)  

---  

## About  

`filetransfer` is a pure‑Python CLI that lets two parties exchange files directly, with no cloud intermediary.  
Data is protected with AES‑256‑GCM for confidentiality and Ed25519 signatures for mutual authentication.  The tool supports resumable sessions, real‑time progress reporting, and a simple plugin system for custom logic.

---  

## Key Features  

* **End‑to‑End Encryption** – AES‑256‑GCM with per‑transfer keys.  
* **Direct P2P** – Connections are established straight between peers.  
* **High‑Performance Chunking** – Optimised chunk sizes for common network conditions.  
* **Mutual Authentication** – Ed25519 keys protect against man‑in‑the‑middle attacks.  
* **Resumable Transfers** – Pause and resume after interruptions.  
* **Live Progress Reporting** – ETA, throughput, and integrity checks.  
* **Plugin Hooks** – Run custom pre‑ and post‑transfer logic.  
* **Cross‑Platform** – Works on Linux, macOS, Windows, and WSL.

---  

## Installation  

    pip install filetransfer

---  

## Getting Started  

### 1. Create your identity  

    filetransfer init --identity <your_username>

Your private key is stored in `~/.filetransfer/keys/`.  Keep it safe and share the public key file with peers.

### 2. Send a file  

    filetransfer send --file ./document.pdf \
      --to <recipient_username>@<recipient_ip>:4242 \
      --key ~/.filetransfer/keys/<recipient_username>_public.ed25519

### 3. Receive a file  

    filetransfer receive --port 4242 --output ./downloads/

---  

## Command‑Line Reference  

| Command                | Description                                |
|------------------------|--------------------------------------------|
| `filetransfer send`    | Transmit a file to a remote peer.         |
| `filetransfer receive` | Listen for incoming transfers.             |
| `filetransfer resume` | Continue a previously interrupted transfer.|
| `filetransfer relay list` | Discover and rank available relay nodes. |
| `filetransfer init`    | Create or refresh your identity keys.      |

---  

## Advanced Usage  

* **Adjust chunk size** – e.g. `--chunk-size 16777216`.  
* **Resume a session** –  
    `filetransfer resume --session ~/.filetransfer/sessions/<session_id>.ftsession`  
* **Relay mode** – When direct P2P fails:  
    ```
    filetransfer send --file report.pdf \
      --to bob:4242 \
      --relay wss://relay.filetransfer.io
    ```  
    (The relay forwards encrypted packets only; it never decrypts the payload.)  
* **Audit log** – Keep a record for compliance:  
    `filetransfer receive --port 4242 --audit-log ~/.filetransfer/audit/2026-08.log`

---  

## Contributing  

1. Open an issue to describe the bug or feature.  
2. Fork the repository and create a clear branch (`fix/...` or `feat/...`).  
3. Follow the style guide – run `black` before committing.  
4. Run tests and keep coverage ≥ 90 %:  
    ```
    pytest tests/ --cov=filetransfer --cov-report=term-missing
    ```  
5. Submit a pull request with a concise description and reference the related issue.

---  

## Project Metrics  

| Metric                   | Value                         |
|--------------------------|-------------------------------|
| Repo size                | 4.2 MB                        |
| Python source lines      | 3,187                         |
| Test coverage           | 94.6 %                        |
| Latest release           | v2.1.0 (2026‑08‑05)           |
| Supported platforms     | Linux · macOS · Windows · WSL|
| Cipher suite             | AES‑256‑GCM · Ed25519 · SHA‑3‑512|

---  

## Changelog  

### v2.1.0 — 2026‑08‑05  

**Added**  
- SHA‑3 integrity verification alongside SHA‑256.  
- `filetransfer relay list` for discovering fast relay nodes.  

**Changed**  
- Default chunk size increased from 4 MiB to 8 MiB.  
- Read receipts now embed checksum metadata for streaming checks.  

**Fixed**  
- Resolved a race condition in multi‑peer transfers.  
- Patched key‑rotation edge case that dropped active connections.  
- Fixed Unicode path handling on Windows.

---  

## License  

MIT License – see the [LICENSE](LICENSE) file.
