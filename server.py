#!/usr/bin/env python3
"""
Web-based file sharing — ready for Render.
Streams files in chunks (5MB) to bypass proxy body-size limits.
Supports persistent disk via UPLOAD_DIR env var.
"""
import os, sys, shutil
from datetime import datetime, timezone
from pathlib import Path

try:
    from flask import (
        Flask, request, jsonify, send_from_directory,
        render_template_string, abort
    )
except ImportError:
    print("Missing flask. Install with: pip install flask gunicorn")
    sys.exit(1)

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = Path(os.environ.get('UPLOAD_DIR', BASE_DIR / 'uploads'))
TEMP_DIR = UPLOAD_DIR / '.tmp'
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# ── Template ──────────────────────────────────────────────────────────────

INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>dropzone</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #0d1117; color: #c9d1d9; min-height: 100vh;
    display: flex; justify-content: center; padding: 2rem 1rem;
  }
  .container { max-width: 800px; width: 100%; }
  h1 { font-weight: 600; font-size: 1.5rem; margin-bottom: .25rem; }
  .sub { color: #8b949e; font-size: .875rem; margin-bottom: 1.5rem; }

  #dropzone {
    border: 2px dashed #30363d; border-radius: 8px; padding: 2.5rem 1rem;
    text-align: center; cursor: pointer; transition: .15s;
    background: #161b22; margin-bottom: 1rem;
  }
  #dropzone.dragover { border-color: #58a6ff; background: #1c2541; }
  #dropzone.has-error { border-color: #f85149; }
  #dropzone input { display: none; }
  #dropzone .icon { font-size: 2rem; margin-bottom: .5rem; }
  #dropzone p { color: #8b949e; }
  #dropzone strong { color: #c9d1d9; }

  #progress-wrap.active { display: block; }
  #progress-wrap { display: none; margin-bottom: 1rem; }
  #progress-bar { width: 100%; height: 6px; -webkit-appearance: none; appearance: none; border-radius: 3px; overflow: hidden; }
  #progress-bar::-webkit-progress-bar { background: #21262d; }
  #progress-bar::-webkit-progress-value { background: #58a6ff; transition: width .2s; }
  #progress-label { font-size: .8rem; color: #8b949e; margin-top: .3rem; }

  #queue { list-style: none; display: flex; flex-direction: column; gap: .25rem; margin-bottom: 1.5rem; }
  .q-item { font-size: .8rem; color: #8b949e; padding: .3rem .5rem; background: #161b22; border-radius: 4px; }

  #file-list { list-style: none; display: flex; flex-direction: column; gap: .25rem; }
  .file-item {
    display: flex; align-items: center; gap: .75rem;
    padding: .6rem .75rem; border-radius: 6px;
    background: #161b22; border: 1px solid #21262d;
    word-break: break-all;
  }
  .file-item .name { flex: 1; font-size: .875rem; }
  .file-item .size { color: #8b949e; font-size: .75rem; white-space: nowrap; }
  .file-item .actions { display: flex; gap: .4rem; flex-shrink: 0; }
  .file-item button {
    background: none; border: 1px solid #30363d; border-radius: 4px;
    color: #c9d1d9; padding: .25rem .6rem; cursor: pointer; font-size: .75rem;
    transition: .1s;
  }
  .file-item button:hover { background: #21262d; }
  .file-item button.danger:hover { border-color: #f85149; color: #f85149; }
  .empty { color: #8b949e; text-align: center; padding: 2rem; font-size: .875rem; }

  .toast {
    position: fixed; bottom: 1.5rem; right: 1.5rem;
    background: #21262d; border: 1px solid #30363d; border-radius: 6px;
    padding: .75rem 1.25rem; font-size: .875rem;
    opacity: 0; transform: translateY(10px); transition: .2s; pointer-events: none;
  }
  .toast.show { opacity: 1; transform: translateY(0); }
  .toast.error { border-color: #f85149; }
</style>
</head>
<body>
<div class="container">
  <h1>dropzone</h1>
  <p class="sub">Share files — no size limit. Drag & drop or click to upload.</p>

  <div id="dropzone">
    <div class="icon">&#8682;</div>
    <p><strong>Click to select</strong> or drag files here</p>
    <input type="file" id="file-input" multiple>
  </div>

  <div id="progress-wrap">
    <progress id="progress-bar" max="100" value="0"></progress>
    <div id="progress-label"></div>
  </div>

  <ul id="queue"></ul>
  <ul id="file-list"><li class="empty">No files yet</li></ul>
</div>
<div id="toast" class="toast"></div>

<script>
const CHUNK = 5 * 1024 * 1024;
const DZ = document.getElementById('dropzone');
const FI = document.getElementById('file-input');
const FL = document.getElementById('file-list');
const QU = document.getElementById('queue');
const PB = document.getElementById('progress-bar');
const PL = document.getElementById('progress-label');
const PW = document.getElementById('progress-wrap');
const TO = document.getElementById('toast');
let toastTimer;
let queue = [];
let active = false;

function fmtSize(b) {
  if (b === 0) return '0 B';
  const u = ['B','KB','MB','GB','TB'];
  const i = Math.floor(Math.log(b) / Math.log(1024));
  return (b / Math.pow(1024, i)).toFixed(i > 0 ? 1 : 0) + ' ' + u[i];
}

function toast(msg, err) {
  clearTimeout(toastTimer);
  TO.textContent = msg;
  TO.className = 'toast show' + (err ? ' error' : '');
  toastTimer = setTimeout(() => TO.classList.remove('show'), 3500);
}

function renderQueue() {
  QU.innerHTML = queue.map(f => `<li class="q-item">Waiting: ${esc(f.name)} (${fmtSize(f.size)})</li>`).join('');
}

function esc(s) { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }

// ── Drag / Drop ──────────────────────────────────────────────────────────
DZ.addEventListener('click', () => FI.click());
DZ.addEventListener('dragover', e => { e.preventDefault(); DZ.classList.add('dragover'); });
DZ.addEventListener('dragleave', () => DZ.classList.remove('dragover'));
DZ.addEventListener('drop', e => {
  e.preventDefault(); DZ.classList.remove('dragover');
  for (const f of e.dataTransfer.files) queue.push(f);
  renderQueue();
  processQueue();
});
FI.addEventListener('change', () => {
  for (const f of FI.files) queue.push(f);
  renderQueue();
  FI.value = '';
  processQueue();
});

// ── Chunked upload ───────────────────────────────────────────────────────
async function processQueue() {
  if (active || queue.length === 0) return;
  active = true;
  const file = queue.shift();
  renderQueue();
  await uploadFile(file);
  active = false;
  processQueue();
}

async function uploadFile(file) {
  DZ.classList.remove('has-error');
  PW.classList.add('active');
  const total = Math.ceil(file.size / CHUNK);
  const sess = Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
  let done = 0;

  for (let i = 0; i < total; i++) {
    const start = i * CHUNK;
    const end = Math.min(start + CHUNK, file.size);
    const blob = file.slice(start, end);
    const fd = new FormData();
    fd.append('file', blob, file.name);
    fd.append('filename', file.name);
    fd.append('chunk', i);
    fd.append('total', total);
    fd.append('session', sess);

    try {
      const r = await new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/upload');
        xhr.upload.onprogress = e => {
          if (e.lengthComputable) {
            const rawDone = done + e.loaded;
            const pct = (rawDone / file.size * 100).toFixed(1);
            PB.value = parseFloat(pct);
            PL.textContent = `${esc(file.name)} — ${pct}%`;
          }
        };
        xhr.onload = () => resolve(xhr);
        xhr.onerror = () => reject(new Error('network'));
        xhr.send(fd);
      });
      if (r.status !== 200) throw new Error(r.responseText || 'upload fail');
      done += blob.size;
      const resp = JSON.parse(r.responseText);
      if (resp.complete) {
        PW.classList.remove('active');
        PL.textContent = '';
        toast(`Uploaded ${file.name}`);
        refreshList();
        return;
      }
    } catch (e) {
      PW.classList.remove('active');
      PL.textContent = '';
      DZ.classList.add('has-error');
      toast(`Failed: ${file.name} — ${e.message}`, true);
      return;
    }
  }
}

// ── File list ────────────────────────────────────────────────────────────
async function refreshList() {
  try {
    const r = await fetch('/api/files');
    const files = await r.json();
    if (files.length === 0) {
      FL.innerHTML = '<li class="empty">No files yet</li>';
      return;
    }
    FL.innerHTML = files.map(f => `
      <li class="file-item" data-name="${escAttr(f.name)}">
        <span class="name">${esc(f.name)}</span>
        <span class="size">${fmtSize(f.size)}</span>
        <span class="actions">
          <button class="dl-btn">DL</button>
          <button class="danger del-btn">X</button>
        </span>
      </li>
    `).join('');
  } catch { /* silent */ }
}

function escAttr(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#x27;');
}

FL.addEventListener('click', e => {
  const btn = e.target.closest('button');
  if (!btn) return;
  const li = btn.closest('.file-item');
  if (!li) return;
  const name = li.dataset.name;
  if (btn.classList.contains('dl-btn')) {
    const a = document.createElement('a');
    a.href = '/api/download/' + encodeURIComponent(name);
    a.download = name;
    a.click();
  } else if (btn.classList.contains('del-btn')) {
    if (!confirm(`Delete ${name}?`)) return;
    fetch('/api/delete/' + encodeURIComponent(name), { method: 'DELETE' })
      .then(r => { if (r.ok) { toast(`Deleted ${name}`); refreshList(); } })
      .catch(() => toast('Delete failed', true));
  }
});

refreshList();
setInterval(refreshList, 5000);
</script>
</body>
</html>"""

# ── Routes ────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template_string(INDEX_HTML)

@app.route('/api/files')
def list_files():
    files = []
    for f in sorted(UPLOAD_DIR.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
        if f.is_file() and f.parent == UPLOAD_DIR:
            st = f.stat()
            files.append({
                'name': f.name,
                'size': st.st_size,
                'modified': datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat()
            })
    return jsonify(files)

@app.route('/api/upload', methods=['POST'])
def upload_chunk():
    f = request.files.get('file')
    if f is None:
        return 'No file in request', 400
    filename = request.form.get('filename', '')
    chunk_idx = int(request.form.get('chunk', 0))
    total = int(request.form.get('total', 1))
    session = request.form.get('session', '')

    filename = os.path.basename(filename)
    if not filename or not session:
        return 'Missing filename or session', 400

    sess_dir = TEMP_DIR / session
    sess_dir.mkdir(parents=True, exist_ok=True)
    chunk_path = sess_dir / f'{chunk_idx:06d}'
    f.save(chunk_path)

    received = len([p for p in sess_dir.iterdir() if p.is_file()])

    if received >= total:
        dest = UPLOAD_DIR / filename
        if dest.exists():
            stem, ext = dest.stem, dest.suffix
            c = 1
            while dest.exists():
                dest = UPLOAD_DIR / f'{stem}_{c}{ext}'; c += 1
        with open(dest, 'wb') as out:
            for i in range(total):
                cp = sess_dir / f'{i:06d}'
                if cp.exists():
                    out.write(cp.read_bytes())
                    cp.unlink()
        shutil.rmtree(sess_dir, ignore_errors=True)
        return jsonify({'name': dest.name, 'size': dest.stat().st_size, 'complete': True})

    return jsonify({'chunk': chunk_idx, 'received': received, 'total': total, 'complete': False})

@app.route('/api/download/<path:filename>')
def download(filename):
    safe = os.path.basename(filename)
    return send_from_directory(UPLOAD_DIR, safe, as_attachment=True)

@app.route('/api/delete/<path:filename>', methods=['DELETE'])
def delete_file(filename):
    safe = os.path.basename(filename)
    fp = UPLOAD_DIR / safe
    if fp.exists() and fp.is_file():
        fp.unlink()
        return jsonify({'status': 'deleted'})
    abort(404)

# clean stale temp files on startup
for p in TEMP_DIR.iterdir():
    if p.is_dir():
        shutil.rmtree(p, ignore_errors=True)

# ── Entry ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    port = int(os.environ.get('PORT', sys.argv[1] if len(sys.argv) > 1 else 8080))
    print(f"Listening on 0.0.0.0:{port}  |  Uploads: {UPLOAD_DIR}")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
