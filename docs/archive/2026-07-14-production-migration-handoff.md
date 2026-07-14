# Production Migration Handoff

Date: 2026-07-14

## Production State

The refactored Knowlpedia is live at <https://knowlpedia.com/>. The canonical
public source and GitHub Pages deployment repository is now:

```text
RyanPersson/knowlpedia
/Users/ryanpersson/anki/code/knowlpedia-root/knowlpedia
branch: main
```

The compiler consumes the sibling content repository. The Pages workflow pins
the content checkout so production builds are reproducible:

```text
RyanPersson/knowlpedia-content
/Users/ryanpersson/anki/code/knowlpedia-root/knowlpedia-content
commit: 2c31f58de4c25b3bb05fdc9a149624ffeac720c6
```

`.github/workflows/pages.yml` tests and builds every pull request. Pushes to
`main` additionally deploy the artifact to GitHub Pages. The custom domain and
HTTPS settings remain attached to the `knowlpedia` repository.

## Migration And History

The production repository retains both independent histories:

- Legacy Hugo production tip: `1bf7251`
- Imported refactor tip: `71de925`
- Two-parent history-preserving migration commit: `52950a5`
- GitHub merge of migration PR #1: `5a90361`

The former private `RyanPersson/knowl-system-refactor` repository is no longer
the deployment source. Its refactor history is reachable from `knowlpedia/main`;
retain it until its archival or redirect policy is decided.

Rollback references in `RyanPersson/knowlpedia` preserve the pre-refactor site:

```text
branch: legacy-hugo
tag: pre-refactor-2026-07-14
```

## Build And Test

Install dependencies and run the normal checks:

```bash
make deps
make test
make build-production
```

`make build-production` compiles the sibling corpus with production-only UI
settings, requires checked-in diagram fragments, and runs the strict rendered
HTML checker.

The migration validation recorded:

- 22 tests passed locally and in GitHub Actions.
- 2,140 knowls compiled in the production build.
- The strict rendered-output check passed.
- 27 TikZ-like diagrams used checked-in prebuilt fragments.
- A basic full-history secret scan found no recognized credentials, private
  keys, suspicious credential filenames, or blobs larger than 20 MiB.

## TikZ And Diagram Workflow

GitHub Actions does not install TeX. Diagram source is compiled locally and the
portable rendered fragments are committed under `prebuilt/diagrams/`.

After changing diagram source, use a machine with the local TeX/ImageMagick
toolchain:

```bash
make refresh-prebuilt-diagrams
make build-production
```

Commit the updated source and prebuilt fragments together. CI's prebuilt-only
mode fails if a required diagram fragment is missing, which prevents source
fallbacks from silently reaching production.

## URL Compatibility

A fresh route comparison found 2,083 exact matches among the 2,088 legacy
routes. Normal knowl URLs such as `/algebra-groups/group/` retain their original
paths. The compiler lowercases generated paths so the four imported Shale-paper
IDs containing capital letters also retain their Hugo-era public URLs.

The five removed legacy-only routes are:

```text
/categories/
/posts/
/preview/
/tags/
/tags/needs-review/
```

These currently return no replacement page. Add redirects only if traffic or
search data makes them worthwhile.

## Operational Notes

- A knowl trigger is an inline disclosure control, not a hyperlink or
  navigation fallback.
- `knowlpedia-content` remains the canonical content source; generated HTML,
  JSON, SQLite, and search output remain build artifacts.
- Production hides the local testing panel.
- The legacy `{{< euler-diagram >}}` source is still an explicit checker
  exception in the semigroup/quasigroup article.
- Local preview management remains available through `make preview-status`,
  `make preview-start`, and `make preview-stop`.

## Follow-up Decisions

- Decide whether to archive the private `knowl-system-refactor` repository or
  leave it read-only with a pointer to `RyanPersson/knowlpedia`.
- Decide whether the five removed legacy-only routes merit redirects.
- Continue corpus, accessibility, mobile, search, and recursive-proof work from
  `RyanPersson/knowlpedia`, not the former refactor repository.

This is a dated operational snapshot. It is not a perpetually current project
status document; use a new dated handoff for later transitions.
