# fileTransfer

[![Python Version](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000?style=flat-square&logo=python)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

**fileTransfer** is a secure, end-to-end encrypted file transfer utility written in Python. It enables direct, authenticated, peer-to-peer file sharing between peers without relying on cloud storage or third-party intermediaries.

---

## Features

- **End-to-End Encryption:** AES-256-GCM encryption ensures only intended recipients can read transferred files.
- **Peer-to-Peer Architecture:** Direct connections eliminate cloud dependencies and maintain local data ownership.
- **High-Speed Transfers:** An optimized chunking algorithm achieves gigabit speeds on standard network connections.
- **Identity Verification:** Mutual authentication via Ed25519 key exchange prevents man-in-the-middle attacks.
- **Progress Streaming:** Real-time transfer metrics with ETA, throughput, and integrity checks.
- **Plugin System:** Extend functionality with custom hooks for pre- and post-transfer operations.
- **Cross-Platform:** Runs natively on Linux, macOS, Windows, and WSL environments.

---

## Getting Started

Install the package from PyPI:

```bash
pip install filetransfer
```

Generate your local identity keys:

```bash
filetransfer init --identity alice
```

This creates a pair of Ed25519 keys stored locally in `~/.filetransfer/keys/`. Share your public key with trusted peers, and keep your private key safe.

### Receiving a File

```bash
filetransfer receive --port 4242 --output ./downloads/
```

### Sending a File

```bash
filetransfer send --file ./document.pdf \
  --to bob.example.com:4242 \
  --key ~/.filetransfer/keys/bob_public.ed25519
```

After a successful transfer, the tool performs an automatic SHA-3-512 hash verification:

```
✓ Transfer complete | Integrity verified | 42.7 MB in 3.2s (13.3 MB/s)
```

---

## Advanced Usage

### Large File Optimization
For files exceeding 1 GB, tune your chunk size to reduce overhead:

```bash
filetransfer send --file massive_dataset.zip \
  --to bob.example.com:4242 \
  --chunk-size 16777216  # 16 MB chunks
```

### Resuming Interrupted Transfers
If a transfer drops, you can resume it gracefully using the session file:

```bash
filetransfer resume --session ~/.filetransfer/sessions/abc123.ftsession
```

### NAT Traversal via Relay Mode
If direct P2P connectivity fails due to NAT restrictions, enable relay routing:

```bash
filetransfer send --file report.pdf \
  --to bob:4242 \
  --relay wss://relay.filetransfer.io
```

*Note: Relay mode never decrypts your payload. It simply forwards encrypted packets, keeping your data opaque to the relay server.*

### Compliance Auditing
Log all transfer sessions for compliance and auditing:

```bash
filetransfer receive --port 4242 --audit-log ~/.filetransfer/audit/2026-08.log
```

---

## Contributing

Contributions are welcome. Before opening a pull request, please follow these steps:

1. **Open an Issue:** Describe the bug or feature you want to work on to prevent overlapping work.
2. **Fork and Branch:** Create a branch with a clear, descriptive name (e.g., `fix/session-sync` or `feat/relay-list`).
3. **Follow Code Standards:** Use `black` for formatting. Write clear docstrings and maintain the existing encryption standards.
4. **Run Tests:** Ensure all tests pass and coverage remains above 90% before submitting a PR:
   ```bash
   pytest tests/ --cov=filetransfer --cov-report=term-missing
   ```
5. **Submit a PR:** Provide a clear description of the changes and link the original issue.

---

## Project Metrics

| Metric | Value |
|--------|-------|
| Repository size | 4.2 MB |
| Lines of Python | 3,187 |
| Test coverage | 94.6% |
| Latest release | v2.1.0 |
| Translations | EN, FR, DE, JP |
| Supported platforms | Linux · macOS · Windows · WSL |
| Cipher suite | AES-256-GCM · Ed25519 · SHA-3-512 |

---

## Changelog

### [v2.1.0] — 2026-08-05

**Fixed**
- Resolved a race condition during simultaneous multi-peer transfers that caused session manifests to desynchronize.
- Patched an edge case where Ed25519 key rotation at runtime dropped the active handoff connection.
- Fixed Windows path normalization issue for files containing Unicode characters.

**Added**
- Native support for SHA-3 integrity verification alongside existing SHA-256 hashing.
- New `filetransfer relay list` subcommand to discover the fastest relay nodes automatically.
- French (`fr-FR`) localization fully integrated.

**Changed**
- Default chunk size increased from 4 MB → 8 MB for improved throughput on high-latency links.
- Read receipts now include checksum metadata for real-time integrity streaming.
- Logging verbosity in development mode now prints trace IDs compatible with OpenTelemetry.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for full text.
