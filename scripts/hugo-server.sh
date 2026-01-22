#!/bin/bash
#
# Hugo server management script
#
# Usage:
#   ./scripts/hugo-server.sh start    # Start server (kills existing first)
#   ./scripts/hugo-server.sh stop     # Stop server
#   ./scripts/hugo-server.sh restart  # Restart server
#   ./scripts/hugo-server.sh status   # Check if running
#

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PORT=1313
WAIT_TIMEOUT=10

stop_server() {
    if pgrep -f "hugo server" > /dev/null 2>&1; then
        echo "Stopping Hugo server..."
        pkill -f "hugo server" 2>/dev/null || true
        sleep 1
        # Force kill if still running
        if pgrep -f "hugo server" > /dev/null 2>&1; then
            pkill -9 -f "hugo server" 2>/dev/null || true
            sleep 1
        fi
        echo "Server stopped."
    else
        echo "No Hugo server running."
    fi
}

start_server() {
    # Stop any existing server first
    stop_server

    echo "Starting Hugo server on port $PORT..."
    cd "$REPO_ROOT"
    hugo server --port "$PORT" &

    # Wait for server to be ready
    echo -n "Waiting for server..."
    for i in $(seq 1 $WAIT_TIMEOUT); do
        if curl -s -o /dev/null -w "" "http://localhost:$PORT/" 2>/dev/null; then
            echo " ready!"
            echo "Server running at http://localhost:$PORT/"
            return 0
        fi
        echo -n "."
        sleep 1
    done

    echo " timeout!"
    echo "Server may still be starting. Check with: curl http://localhost:$PORT/"
    return 1
}

check_status() {
    if pgrep -f "hugo server" > /dev/null 2>&1; then
        PID=$(pgrep -f "hugo server" | head -1)
        if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$PORT/" 2>/dev/null | grep -q "200"; then
            echo "Hugo server running (PID $PID) and healthy on port $PORT"
            return 0
        else
            echo "Hugo server running (PID $PID) but not responding properly on port $PORT"
            return 1
        fi
    else
        echo "Hugo server not running"
        return 1
    fi
}

case "${1:-status}" in
    start)
        start_server
        ;;
    stop)
        stop_server
        ;;
    restart)
        start_server
        ;;
    status)
        check_status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
