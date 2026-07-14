# Preview Server Service

Date: 2026-07-01

The imported refactor preview is served by a user systemd service:

```text
knowlpedia-refactor-preview.service
```

Service file:

```text
/home/codex/.config/systemd/user/knowlpedia-refactor-preview.service
```

It serves:

```text
/home/codex/code/knowlpedia-root/knowl-system-refactor/public-imported
```

on:

```text
http://100.69.17.72:8002/
```

This service is intentionally persistent. Do not start a second Knowlpedia
preview server for changes that are visible in `public-imported/`; rebuild that
directory and link to the existing `8002` preview instead.

For unrelated temporary development servers on the Optiplex, use the host helper
documented in `/home/codex/.codex/AGENTS.md` instead:

```bash
devserver start <name> -- <command...>
devserver status <name>
devserver logs -f <name>
devserver stop <name>
```

Use `devserver` for ordinary Codex/dev previews that are not covered by an
existing persistent service; keep this manually named service for the always-on
Knowlpedia comparison preview.

## Agent Response Links

When an agent changes rendered content, examples, or preview-visible behavior,
the final Codex chat response should include a direct URL to the relevant page.
Prefer the Tailscale URL when the page is meant to be opened from another
machine, and include the exact path that demonstrates the change.

## Why The Old Server Went Down

The previous server was started as an ad hoc Codex shell process:

```bash
python3 -m http.server 8002 --bind 0.0.0.0 --directory public-imported
```

That process was parented by the Codex app server, not by systemd. It had no
restart policy and no boot/login integration, so if the Codex PTY/session was
cleaned up, the process simply exited. This looked like a crash from the browser
side, but there was no evidence of an application crash or Python exception.

## Persistence Setup

The current service uses:

```ini
Restart=always
RestartSec=5
```

It is enabled in the `codex` user's default target, and user lingering is enabled:

```bash
systemctl --user is-enabled knowlpedia-refactor-preview.service
loginctl show-user codex --property=Linger
```

Expected:

```text
enabled
Linger=yes
```

## Operations

Check status:

```bash
systemctl --user status knowlpedia-refactor-preview.service --no-pager
```

Restart:

```bash
systemctl --user restart knowlpedia-refactor-preview.service
```

Stop:

```bash
systemctl --user stop knowlpedia-refactor-preview.service
```

View logs:

```bash
journalctl --user -u knowlpedia-refactor-preview.service --no-pager -n 80
```

Check the Tailscale URL:

```bash
curl -I --max-time 5 http://100.69.17.72:8002/topics/
```

## Rebuild Note

The service serves the generated `public-imported` directory directly. After
running:

```bash
make build-imported
```

the service usually does not need a restart, because Python's static server reads
files from disk on each request. Restart only if the service itself is unhealthy.
