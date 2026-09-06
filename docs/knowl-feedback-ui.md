# Knowl feedback preview

The recovered feedback UI is integrated on `knowl-feedback-ui`, based on develop at e516a40, in `ab-tests/knowlpedia`. Its sibling content repository remains on the merged develop revision 959d9768. The original checkout's uncommitted files and its September 4 stashes were left intact.

## Live service

[Open Knowlpedia with feedback](http://100.69.17.72:8012/). Use **Ask Codex** on a full page or an expanded knowl. Ask uses a read-only turn; Flag issue and Request change can edit this application and its sibling content repository. The current knowl ID, title, selected text and reviewer message are sent to the local bridge.

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
