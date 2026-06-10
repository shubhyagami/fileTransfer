#!/usr/bin/env python3
import socket
import os
import sys
import threading
import json
import hashlib
import argparse

CHUNK_SIZE = 1024 * 1024

def send_file(conn, filepath):
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(CHUNK_SIZE):
            sha256.update(chunk)
    filehash = sha256.hexdigest()

    metadata = json.dumps({
        'type': 'file',
        'filename': filename,
        'filesize': filesize,
        'sha256': filehash
    })
    conn.sendall(len(metadata).to_bytes(4, 'big'))
    conn.sendall(metadata.encode())

    sent = 0
    with open(filepath, 'rb') as f:
        while chunk := f.read(CHUNK_SIZE):
            conn.sendall(chunk)
            sent += len(chunk)
            progress = sent / filesize * 100
            print(f"\r  Sent: {progress:.1f}% ({sent}/{filesize} bytes)", end='')
    print()
    print(f"  Sent {filename} ({filesize} bytes, SHA256: {filehash[:16]}...)")
    return True

def receive_file(conn, save_dir):
    raw = conn.recv(4)
    if not raw:
        return None
    meta_len = int.from_bytes(raw, 'big')

    meta_data = b''
    while len(meta_data) < meta_len:
        chunk = conn.recv(meta_len - len(meta_data))
        if not chunk:
            raise ConnectionError("Connection lost while receiving metadata")
        meta_data += chunk

    meta = json.loads(meta_data.decode())
    filename = meta['filename']
    filesize = meta['filesize']
    expected_hash = meta['sha256']

    save_path = os.path.join(save_dir, filename)
    counter = 1
    while os.path.exists(save_path):
        name, ext = os.path.splitext(filename)
        save_path = os.path.join(save_dir, f"{name}_{counter}{ext}")
        counter += 1

    sha256 = hashlib.sha256()
    received = 0
    with open(save_path + '.part', 'wb') as f:
        while received < filesize:
            remaining = filesize - received
            read_size = min(CHUNK_SIZE, remaining)
            chunk = conn.recv(read_size)
            if not chunk:
                raise ConnectionError("Connection lost while receiving file")
            f.write(chunk)
            sha256.update(chunk)
            received += len(chunk)
            progress = received / filesize * 100
            print(f"\r  Received: {progress:.1f}% ({received}/{filesize} bytes)", end='')

    filehash = sha256.hexdigest()
    if filehash == expected_hash:
        os.rename(save_path + '.part', save_path)
        print(f"\n  Received {filename} ({filesize} bytes, verified)")
    else:
        os.remove(save_path + '.part')
        print(f"\n  Hash mismatch! File corrupted.")
        return None

    return save_path

def receiver_loop(conn, save_dir):
    print("  Waiting for incoming files...")
    while True:
        try:
            result = receive_file(conn, save_dir)
            if result is None:
                break
        except (ConnectionError, EOFError):
            print("  Connection closed by peer.")
            break
        except Exception as e:
            print(f"  Error: {e}")
            break

def start_server(port, save_dir):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', port))
    server.listen(1)
    print(f"Listening on port {port}...")

    conn, addr = server.accept()
    print(f"Connected by {addr}")

    t = threading.Thread(target=receiver_loop, args=(conn, save_dir), daemon=True)
    t.start()
    return conn

def connect_to_peer(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f"Connected to {host}:{port}")
    return sock

def interactive_shell(conn, save_dir):
    """Interactive mode: send files, change dir, etc."""
    print("\nCommands: send <path> | dir <path> | status | quit")
    while True:
        try:
            cmd = input("> ").strip()
            if not cmd:
                continue
            if cmd.startswith('send '):
                fp = cmd[5:].strip()
                if os.path.isfile(fp):
                    send_file(conn, fp)
                else:
                    print(f"File not found: {fp}")
            elif cmd == 'quit':
                break
            elif cmd.startswith('dir '):
                nd = cmd[4:].strip()
                if os.path.isdir(nd):
                    save_dir = os.path.abspath(nd)
                    print(f"Receive dir: {save_dir}")
                else:
                    print(f"Not a directory: {nd}")
            elif cmd == 'status':
                print(f"Connected. Receiving to: {save_dir}")
            else:
                print("Unknown command")
        except KeyboardInterrupt:
            break

def main():
    parser = argparse.ArgumentParser(description='P2P File Sharing (raw TCP, no HTTP)')
    parser.add_argument('--listen', '-l', type=int, metavar='PORT',
                        help='Start in listen mode on PORT')
    parser.add_argument('--connect', '-c', type=str, metavar='HOST:PORT',
                        help='Connect to a peer')
    parser.add_argument('--send', type=str, metavar='FILE',
                        help='Send a file immediately after connecting')
    parser.add_argument('--receive-dir', '-o', type=str, default='.',
                        help='Directory to save received files')

    args = parser.parse_args()
    if not args.listen and not args.connect:
        parser.print_help()
        return

    save_dir = os.path.abspath(args.receive_dir)
    os.makedirs(save_dir, exist_ok=True)

    conn = None
    if args.listen:
        conn = start_server(args.listen, save_dir)
    elif args.connect:
        host, port_str = args.connect.rsplit(':', 1)
        port = int(port_str)
        conn = connect_to_peer(host, port)
        t = threading.Thread(target=receiver_loop, args=(conn, save_dir), daemon=True)
        t.start()

    if args.send and conn:
        send_file(conn, args.send)

    if conn:
        interactive_shell(conn, save_dir)
        conn.close()

    print("Done.")

if __name__ == '__main__':
    main()

// sync @ 2026-06-11T05:20:41.616674
