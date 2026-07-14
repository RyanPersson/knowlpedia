#!/usr/bin/env python3
"""Manage one tracked local Knowlpedia preview server."""

from __future__ import annotations

import argparse
import json
import os
import signal
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / ".preview-server"
STATE_FILE = STATE_DIR / "state.json"
LOG_FILE = STATE_DIR / "preview.log"


def default_python() -> str:
    venv_python = ROOT / ".venv" / "bin" / "python"
    return str(venv_python if venv_python.exists() else Path(sys.executable))


def load_state() -> dict[str, object] | None:
    if not STATE_FILE.exists():
        return None
    try:
        return json.loads(STATE_FILE.read_text())
    except json.JSONDecodeError:
        return {"error": "state file is not valid JSON", "path": str(STATE_FILE)}


def save_state(state: dict[str, object]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def remove_state() -> None:
    try:
        STATE_FILE.unlink()
    except FileNotFoundError:
        pass


def pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def port_accepts_connection(host: str, port: int) -> bool:
    try:
        with socket.create_connection((host, port), timeout=0.4):
            return True
    except OSError:
        return False


def port_has_listener(port: int) -> bool:
    return bool(listener_pids(port))


def listener_pids(port: int) -> list[int]:
    result = subprocess.run(
        ["lsof", "-nP", "-t", f"-iTCP:{port}", "-sTCP:LISTEN"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        return []
    pids: list[int] = []
    for line in result.stdout.splitlines():
        try:
            pids.append(int(line.strip()))
        except ValueError:
            pass
    return pids


def wait_for_port(host: str, port: int, timeout: float = 3.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if port_accepts_connection(host, port) or port_has_listener(port):
            return True
        time.sleep(0.05)
    return False


def tracked_state_status() -> tuple[dict[str, object] | None, bool]:
    state = load_state()
    if not state or "pid" not in state:
        return state, False
    try:
        pid = int(state["pid"])
    except (TypeError, ValueError):
        return state, False
    return state, pid_alive(pid)


def print_state(state: dict[str, object], alive: bool) -> None:
    status = "running" if alive else "stale"
    print(f"tracked preview: {status}")
    for key in ["pid", "url", "directory", "log", "started_at", "command"]:
        value = state.get(key)
        if value:
            if isinstance(value, list):
                value = " ".join(str(item) for item in value)
            print(f"  {key}: {value}")


def command_start(args: argparse.Namespace) -> int:
    state, alive = tracked_state_status()
    if state and alive:
        print_state(state, True)
        print("already running; reusing the tracked preview")
        return 0

    if state and not alive:
        print("removing stale preview state")
        remove_state()

    directory = (ROOT / args.directory).resolve()
    if not directory.exists():
        print(f"preview directory does not exist: {directory}", file=sys.stderr)
        print("run the relevant build first, e.g. `make build-content`", file=sys.stderr)
        return 1

    if port_has_listener(args.port):
        print(f"port is already in use: http://{args.host}:{args.port}/", file=sys.stderr)
        print("run `make preview-scan` to inspect local listeners", file=sys.stderr)
        return 1

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    log = LOG_FILE.open("ab")
    command = [
        default_python(),
        "-m",
        "http.server",
        str(args.port),
        "--bind",
        args.host,
        "--directory",
        str(directory),
    ]
    process = subprocess.Popen(
        command,
        cwd=ROOT,
        stdin=subprocess.DEVNULL,
        stdout=log,
        stderr=subprocess.STDOUT,
        start_new_session=True,
    )
    log.close()

    url = f"http://{args.host}:{args.port}/"
    state = {
        "pid": process.pid,
        "host": args.host,
        "port": args.port,
        "url": url,
        "directory": str(directory),
        "log": str(LOG_FILE),
        "started_at": datetime.now(timezone.utc).isoformat(),
        "command": command,
    }
    save_state(state)

    if not wait_for_port(args.host, args.port):
        if process.poll() is not None:
            remove_state()
            print(f"preview process exited during startup with code {process.returncode}", file=sys.stderr)
            print(f"log: {LOG_FILE}", file=sys.stderr)
            return 1
        print(f"preview process started but did not accept connections: pid {process.pid}", file=sys.stderr)
        print(f"log: {LOG_FILE}", file=sys.stderr)
        return 1

    print(f"started preview: {url}")
    print(f"pid: {process.pid}")
    print(f"log: {LOG_FILE}")
    return 0


def command_status(args: argparse.Namespace) -> int:
    state, alive = tracked_state_status()
    if not state:
        print("tracked preview: not running")
    else:
        print_state(state, alive)

    if args.scan:
        return command_scan(args)
    return 0


def command_adopt(args: argparse.Namespace) -> int:
    state, alive = tracked_state_status()
    if state and alive:
        print_state(state, True)
        print("already tracking a running preview")
        return 0

    pids = listener_pids(args.port)
    if not pids:
        print(f"no listener found on port {args.port}", file=sys.stderr)
        return 1
    if len(pids) > 1:
        joined = ", ".join(str(pid) for pid in pids)
        print(f"multiple listeners found on port {args.port}: {joined}", file=sys.stderr)
        return 1

    directory = (ROOT / args.directory).resolve()
    if not directory.exists():
        print(f"preview directory does not exist: {directory}", file=sys.stderr)
        return 1

    url = f"http://{args.host}:{args.port}/"
    adopted_state = {
        "pid": pids[0],
        "host": args.host,
        "port": args.port,
        "url": url,
        "directory": str(directory),
        "log": str(LOG_FILE),
        "started_at": datetime.now(timezone.utc).isoformat(),
        "command": ["adopted existing listener"],
        "adopted": True,
    }
    save_state(adopted_state)
    print(f"adopted preview: {url}")
    print(f"pid: {pids[0]}")
    return 0


def command_stop(args: argparse.Namespace) -> int:
    state, alive = tracked_state_status()
    if not state:
        print("tracked preview: not running")
        return 0
    if not alive:
        print_state(state, False)
        remove_state()
        print("removed stale preview state")
        return 0

    pid = int(state["pid"])
    try:
        os.kill(pid, signal.SIGTERM)
    except PermissionError:
        print(f"permission denied stopping preview pid {pid}", file=sys.stderr)
        print("rerun the same stop command with sufficient permissions", file=sys.stderr)
        return 1
    deadline = time.monotonic() + 5
    while time.monotonic() < deadline:
        if not pid_alive(pid):
            remove_state()
            print(f"stopped preview pid {pid}")
            return 0
        time.sleep(0.1)

    if args.force:
        try:
            os.kill(pid, signal.SIGKILL)
        except PermissionError:
            print(f"permission denied force-stopping preview pid {pid}", file=sys.stderr)
            return 1
        remove_state()
        print(f"force-stopped preview pid {pid}")
        return 0

    print(f"preview pid {pid} did not stop after SIGTERM", file=sys.stderr)
    print("rerun with `--force` if this is the tracked preview you want to kill", file=sys.stderr)
    return 1


def command_restart(args: argparse.Namespace) -> int:
    stop_args = argparse.Namespace(force=args.force)
    stopped = command_stop(stop_args)
    if stopped != 0:
        return stopped
    return command_start(args)


def command_scan(args: argparse.Namespace) -> int:
    lsof = subprocess.run(
        ["lsof", "-nP", "-iTCP", "-sTCP:LISTEN"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if lsof.returncode not in (0, 1):
        print(lsof.stderr.strip(), file=sys.stderr)
        return lsof.returncode

    lines = lsof.stdout.splitlines()
    if not lines:
        print("no TCP listeners found")
        return 0

    if args.all:
        print(lsof.stdout.rstrip())
        return 0

    header, *rows = lines
    python_rows = [row for row in rows if row.startswith("Python")]
    if not python_rows:
        print("no Python TCP listeners found")
        return 0

    print(header)
    for row in python_rows:
        print(row)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    start = subparsers.add_parser("start", help="start or reuse the tracked preview")
    start.add_argument("--host", default="127.0.0.1")
    start.add_argument("--port", type=int, default=8012)
    start.add_argument("--directory", default="public-imported")
    start.set_defaults(func=command_start)

    status = subparsers.add_parser("status", help="show tracked preview state")
    status.add_argument("--scan", action="store_true", help="also list Python TCP listeners")
    status.add_argument("--all", action="store_true", help="with --scan, show all TCP listeners")
    status.set_defaults(func=command_status)

    stop = subparsers.add_parser("stop", help="stop the tracked preview")
    stop.add_argument("--force", action="store_true")
    stop.set_defaults(func=command_stop)

    adopt = subparsers.add_parser("adopt", help="track an existing preview listener")
    adopt.add_argument("--host", default="127.0.0.1")
    adopt.add_argument("--port", type=int, default=8012)
    adopt.add_argument("--directory", default="public-imported")
    adopt.set_defaults(func=command_adopt)

    restart = subparsers.add_parser("restart", help="restart the tracked preview")
    restart.add_argument("--host", default="127.0.0.1")
    restart.add_argument("--port", type=int, default=8012)
    restart.add_argument("--directory", default="public-imported")
    restart.add_argument("--force", action="store_true")
    restart.set_defaults(func=command_restart)

    scan = subparsers.add_parser("scan", help="list local Python TCP listeners")
    scan.add_argument("--all", action="store_true", help="show all TCP listeners")
    scan.set_defaults(func=command_scan)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
