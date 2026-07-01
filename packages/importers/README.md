# Importers

Importers convert existing source collections into knowlpack source.

## Knowlpedia Content Import

```bash
make import-content
```

This reads `../knowlpedia-content` and writes `imports/knowlpedia-content`.

The importer:

- preserves every markdown file, including section `_index.md` files and root
  pages
- converts Hugo knowl shortcodes to semantic wikilinks
- keeps the original body markdown
- writes TOML-front-matter `.knowl.md` files
- writes `import-report.json` with counts and conversion details

Compile the imported package with:

```bash
make build-imported
```

The imported corpus may contain pre-existing dangling links. The build records
those in `public-imported/reports/validation.json` while still producing
comparison output.
