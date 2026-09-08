# Knowl feedback preview

The recovered feedback UI is integrated on `knowl-feedback-ui`, based on develop at e516a40, in `ab-tests/knowlpedia`. Its sibling content repository remains on the merged develop revision 959d9768. The original checkout's uncommitted files and its September 4 stashes were left intact.

## Live service

[Open Knowlpedia with feedback](http://100.69.17.72:8012/). Use **Ask Codex** on a full page or an expanded knowl. Ask uses a read-only turn. Flag issue records and investigates a concern in the knowl’s `[[issues]]` metadata; Request change can apply corrections. Both use a workspace-write turn, with Flag constrained by its instructions to issue metadata. The current knowl ID, title, selected text and reviewer message are sent to the local bridge.

The persistent service is `devserver-knowlpedia-feedback.service`, serving `ab-tests/knowlpedia/public-imported`. The existing rendered content and review pages were retained; the compiler's runtime-asset copier refreshed the feedback JavaScript and CSS. No content rebuild or mathematical edits were needed.

From `ab-tests/knowlpedia`:

```bash
devserver status knowlpedia-feedback
devserver logs -f knowlpedia-feedback
devserver restart knowlpedia-feedback -- .venv/bin/python scripts/knowl_feedback_server.py --host 0.0.0.0 --port 8012 --directory public-imported --token-file .preview-server/codex-access-token
```

The key is stored in `.preview-server/codex-access-token` with mode 0600. The original key was carried over; it is reused on restart and only generated when the file is missing. The dialog remembers it in this browser's local storage. Do not commit the key. The feedback conversation ID is separately persisted in `.preview-server/feedback-thread.json`; completed HTTP job records are memory-only.

## Consolidated previews

| Port | Service | Result |
| --- | --- | --- |
| 8012 | knowlpedia-feedback | Active; updated develop plus feedback UI |
| 8012 | old knowlpedia-quaternionic-psh | Stopped and replaced |
| 8013 | knowlpedia-quantum-chaos-preview | Stopped and disabled; duplicate original output |
| 8015 | knowlpedia-astra-benchmark | Stopped; same output now served on 8012 |
| 8016 | knowlpedia-graph-iteration | Stopped; graph branch already merged |
| 8014 | knowlpedia-gephi-lite | Retained; distinct graph-analysis tool |

The comparison pages are now available on port 8012: [merge diff](http://100.69.17.72:8012/review/merge-changes/), [develop diff](http://100.69.17.72:8012/review/content-changes/), and [pinned comparison](http://100.69.17.72:8012/review/develop-comparison/). Unrelated services were not stopped. Old historical documents may still link to port 8015.

## Compatibility and validation

The original UI patch applied cleanly over the merged graph and reader changes. A request-generation guard prevents a delayed response for a closed dialog from appearing under a different knowl. The bridge uses the installed Codex App Server schema (CLI 0.153.4), with explicit read-only or workspace-write permissions and the current checkout on resume. Protocol reference: [official App Server documentation](https://learn.chatgpt.com/docs/app-server).

140 Python tests pass, including token persistence. Browser tests cover existing nested knowl interactions, themes, feedback payloads, 320/390/1440px dialogs, and late-response isolation. Live checks reject requests without a token and cross-origin requests. A real read-only question returned “Commutativity; Scalar identity” after reading the current vector-space source. The UI remains development-only; production excludes knowl-testing.js.

## Refactor ledger viewer

Open **Ask Codex → Refactor ledger → Load review history** on any page or expanded knowl. The existing access-key field authenticates this read-only request. The viewer shows matching entries from the sibling content repository's `reviews/refactor-ledger.json`, in reverse batch order, with expandable evidence, changes, sources, assumptions and recorded hashes. These are historical editorial records, not certification of the current text; separate dependency-review reports are not included.

The development-only `/__knowlpedia/reviews?knowlId=...` endpoint reads the ledger on demand, so ledger edits appear without rebuilding. Nothing is copied into production assets, and opening the viewer does not invoke a model or create a feedback turn.

## Flagged issue metadata

Flag issue instructs Codex to persist an `[[issues]]` record in the selected
knowl's TOML front matter before investigation, then add its assessment.
The authoritative field and lifecycle convention is the sibling content
repository's `EDITORIAL.md`, under “Flagged issues.” The reply identifies the
saved issue ID, status and file. Request change can resolve a matching issue
with a recorded explanation and checks. These records are Git-visible content
metadata; the flag action does not commit them. They are not yet displayed
in the refactor-ledger viewer, which continues to show review history.

## Shared conversation page

### Messages about a diff

Each generated comparison has a **Message about this diff** action. It opens
the shared conversation in a new tab with the knowl and comparison attached.
Opening it does not submit a message. The composer shows the selected diff,
links back to it, and offers **Remove diff context** for unrelated questions.

On submission, the bridge reads the generated snapshot from the comparison's
`notes/` directory. It includes both complete sources, the unified diff,
pinned Git revisions, source path, and saved review records in the model's
reference context. A hash identifies the exact snapshot opened by the reviewer;
if regeneration changed it, the bridge asks the reviewer to reopen the diff
instead of silently attaching another version. Conversation history displays
the diff identity without repeating the full source payload.

Messaging requires the development preview profile. After a production-only
validation build, restore the interactive preview with
`make build-content KNOWLPEDIA_PROFILE=development EXTRA_CONTENT_SOURCES=`
and regenerate the comparison (the build replaces the output directory).
The 3,539 production knowls are unchanged; the development preview also
includes its testing fixtures. The same persistent service, access key, and
feedback thread are reused.

Validation: `node tests/review_conversation_smoke.mjs` checks the review button,
attached context, submission payload, removal, and desktop/mobile layouts.
Model submissions are intercepted in this test; it creates no feedback turn.

### General messages

Open `/conversation/` on the feedback preview, or follow **Open shared
conversation** in a knowl's dialog. It reads the same persistent Codex thread
through App Server `thread/read`, including the existing reviewer messages,
assistant progress messages and replies. Internal instructions, reasoning and
tool payloads are not exposed. History requires the same bearer key as
feedback; no history is exported into build artifacts. The page and its
script are served only by the development feedback server.

Ask defaults to read-only. Request change allows edits under the existing
workspace policy. A knowl ID is optional for these general messages, but
required for Flag issue. All requests use the existing serialized feedback
queue and shared thread. History refreshes every five seconds while visible.

Dictation records up to 29 seconds with MediaRecorder and posts audio to the
same-origin, access-key-protected `/__knowlpedia/transcribe` endpoint. FFmpeg
decodes supported browser formats in memory to mono 16 kHz signed 16-bit PCM.
The bridge forwards this to the existing Parakeet service's private request
socket and inserts the returned text into the editable draft without sending
it to Codex. Uploads are limited to 5 MB and decoded audio to 30 seconds; only
one dictation request is accepted at a time. No audio or dictation transcript
is written to disk by this path. The shared-model interface is documented in
[Oreo Voice experiments](/home/codex/code/home-automation/docs/oreo-voice-experiments.md).

Microphone capture requires HTTPS or localhost and browser permission.
Tailscale Serve provides `https://optiplex.taildb538a.ts.net/` privately within
the tailnet, proxying the existing service on port 8012. Certificate issuance
succeeded on September 7 at 04:30 UTC. Earlier ACME orders failed because the
certificate authority received NXDOMAIN for the DNS challenge record; issuance
succeeded on a later retry after DNS became available. Tailscale manages renewal.
The access key is unchanged but needs entering on the HTTPS origin once.
The existing HTTP preview remains available, with microphone capture disabled
for non-localhost HTTP origins.

The conversation page follows `knowl-theme`, falls back to the system color
scheme, and provides its own light/dark toggle.

Validation: `node tests/conversation_smoke.mjs` exercises authenticated real
history at 320/390/1440px, mock message submission, required knowl context for
flags, and the shared theme preference. `node tests/dictation_smoke.mjs` uses
Chromium’s synthetic microphone to record a real WebM clip, transcribe it
through the running Parakeet instance, and verify the editable draft. Python tests check history filtering and preserve the production
gate and existing feedback validation.
