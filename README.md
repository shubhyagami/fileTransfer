# fileTransfer

A lightweight, peer‑to‑peer command‑line utility for end‑to‑end encrypted file transfers. All data is encrypted with AES‑256‑GCM, authenticated with Ed25519, and designed for trusted environments that require no cloud intermediate.

---  

## Badges  

[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/downloads/)  
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)](https://github.com/psf/black)  
[![Tests](https://img.shields.io/badge/tests-passing-success?style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)  
[![Coverage](https://img.shields.io/badge/coverage-94.6%25-success?style=flat-square)](https://github.com/shubhyagami/filetransfer/actions)  
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)  
[![PyPI](https://img.shields.io/pypi/v/filetransfer?style=flat-square)](https://pypi.org/project/filetransfer/)  

---  

## About  

`filetransfer` is a small, pure‑Python CLI that enables direct, encrypted transfers between two parties. It uses AES‑256‑GCM for confidentiality, Ed25519 for mutual authentication, and supports resumable sessions, progress reporting, and a simple plugin system.

---  

## Key Features  

- **End‑to‑End Encryption** – AES‑256‑GCM with per‑transfer keys.  
- **True Peer‑to‑Peer** – No cloud intermediary; connections are established directly.  
- **High‑Performance Chunking** – Optimized chunk sizes for typical networks.  
- **Mutual Authentication** – Ed25519 keys prevent man‑in‑the‑middle attacks.  
- **Resumable Transfers** – Pause and resume after interruptions.  
- **Live Progress Reporting** – ETA, throughput, and integrity checks.  
- **Plugin Hooks** – Run custom pre‑ and post‑transfer logic.  
- **Cross‑Platform** – Works on Linux, macOS, Windows, and WSL.  

---  

## Installation  

```bash
pip install filetransfer
```  

---  

## Quick Start  

### 1. Generate an identity  

```bash
filetransfer init --identity <your_username>
```  

Your private key is stored in `~/.filetransfer/keys/`. Protect it and share the public key with peers.  

### 2. Send a file  

```bash
filetransfer send --file ./document.pdf \
  --to <recipient_username>@<recipient_ip>:4242 \
  --key ~/.filetransfer/keys/<recipient_username>_public.ed25519
```  

### 3. Receive a file  

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

- **Chunk Size Tuning** – Adjust for large files, e.g., `--chunk-size 16777216`.  
- **Resuming Transfers** – Resume a saved session:  
  ```bash
  filetransfer resume --session ~/.filetransfer/sessions/<session_id>.ftsession
  ```  
- **NAT Traversal (Relay Mode)** – Use a relay when direct P2P fails:  
  ```bash
  filetransfer send --file report.pdf \
    --to bob:4242 \
    --relay wss://relay.filetransfer.io
  ```  
  *The relay forwards encrypted packets only; it never decrypts the payload.*  
- **Auditing** – Log each session for compliance:  
  ```bash
  filetransfer receive --port 4242 --audit-log ~/.filetransfer/audit/2026-08.log
  ```  

---  

## Contributing  

1. **Open an Issue** – Explain bugs or feature requests before starting work.  
2. **Fork & Branch** – Use a clear branch name (e.g., `fix/session-sync` or `feat/relay-discovery`).  
3. **Follow Style** – Run `black` to format and keep code consistent.  
4. **Run Tests** – Ensure all tests pass and coverage stays above 90%:  
   ```bash
   pytest tests/ --cov=filetransfer --cov-report=term-missing
   ```  
5. **Submit a Pull Request** – Include a concise description of changes and reference the related issue.  

---  

## Project Metrics  

| Metric | Value |
|--------|-------|
| Repository size | 4.2 MB |
| Python source lines | 3,187 |
| Test coverage | 94.6 % |
| Latest release | v2.1.0 (2026‑08‑05) |
| Supported platforms | Linux · macOS · Windows · WSL |
| Cipher suite | AES‑256‑GCM · Ed25519 · SHA‑3‑512 |

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
