#!/bin/bash
# Fully automated knowl generation pipeline
# Runs 15 batches in 3 rounds of 6, processes outputs after each round

BATCH_DIR="/Users/ryanpersson/anki/code/blog/tmp/geometry-bundles-batches"
cd "$BATCH_DIR"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$BATCH_DIR/run.log"
}

log "Starting automated knowl generation"

# Check Chrome
if ! pgrep -f "Chrome.*remote-debugging-port" > /dev/null; then
    log "Starting Chrome for Oracle..."
    ~/.oracle/start-chrome.sh &
    sleep 5
fi

# Round 1: batches 1-6
log "=== ROUND 1: batches 01-06 ==="
~/.oracle/oracle-parallel.sh \
    -pf "$BATCH_DIR/batch01.md" \
    -pf "$BATCH_DIR/batch02.md" \
    -pf "$BATCH_DIR/batch03.md" \
    -pf "$BATCH_DIR/batch04.md" \
    -pf "$BATCH_DIR/batch05.md" \
    -pf "$BATCH_DIR/batch06.md" \
    --sessions-file "$BATCH_DIR/sessions-round1.txt"

log "Round 1 complete. Processing outputs..."
python3 "$BATCH_DIR/process-outputs.py" "$BATCH_DIR/sessions-round1.txt"

# Round 2: batches 7-12
log "=== ROUND 2: batches 07-12 ==="
~/.oracle/oracle-parallel.sh \
    -pf "$BATCH_DIR/batch07.md" \
    -pf "$BATCH_DIR/batch08.md" \
    -pf "$BATCH_DIR/batch09.md" \
    -pf "$BATCH_DIR/batch10.md" \
    -pf "$BATCH_DIR/batch11.md" \
    -pf "$BATCH_DIR/batch12.md" \
    --sessions-file "$BATCH_DIR/sessions-round2.txt"

log "Round 2 complete. Processing outputs..."
python3 "$BATCH_DIR/process-outputs.py" "$BATCH_DIR/sessions-round2.txt"

# Round 3: batches 13-15
log "=== ROUND 3: batches 13-15 ==="
~/.oracle/oracle-parallel.sh \
    -pf "$BATCH_DIR/batch13.md" \
    -pf "$BATCH_DIR/batch14.md" \
    -pf "$BATCH_DIR/batch15.md" \
    --sessions-file "$BATCH_DIR/sessions-round3.txt"

log "Round 3 complete. Processing outputs..."
python3 "$BATCH_DIR/process-outputs.py" "$BATCH_DIR/sessions-round3.txt"

# Final count
TOTAL=$(ls /Users/ryanpersson/anki/code/blog/content/geometry-bundles/*.md | wc -l)
log "=== COMPLETE ==="
log "Total knowl files: $TOTAL"

# Build test
log "Testing Hugo build..."
cd /Users/ryanpersson/anki/code/blog
hugo --quiet && log "Hugo build successful" || log "Hugo build FAILED"
