# Development and checks

## Find the right checkout

Run `pwd`, `git branch --show-current`, and `git status --short` in both the application and content repositories. Several copies exist on this machine. Changes in one do not automatically change another, and the persistent live copy is not necessarily the development preview.

The Makefile normally uses sibling `knowlpedia-content` as the public source package, optionally composes local reference sources, and discovers sibling `knowlification-cache` for development reading copies.

## Build and inspect

```bash
make build
make check-rendering
```

A full build compiles the development site, docs and private library. Reuse the existing service that serves this checkout's output. Verify its working directory and served directory; do not guess a preview port from an old note or start another service for the same files. Report direct page URLs after a visible change.

```bash
make build-production
```

This creates and checks the production artifact locally. It does not publish it. It excludes the private cache, these documentation pages, library navigation, testing fixtures and local-only reference sources. Both standard targets currently write `public-imported/`; rebuild development after inspecting production if the shared preview should expose development features again.

To validate a separate output without replacing the active preview, use `make build-production OUTPUT_DIR=tmp/production-check` or `make build OUTPUT_DIR=tmp/development-check`. Pass the same `OUTPUT_DIR` to `make check-rendering` when checking that development output.

GitHub Pages publication is configured in `.github/workflows/pages.yml`. A push to the application repository's `main` branch can run the deployment workflow. Publishing is separate from producing a local build.

## Required verification

The broad checks in the content-batch workflow are intentional. Keep them even when a model appears more capable or a local change seems small. For a content batch, follow the full active `workflows/create-knowl-batch.md`, including semantic review, source and structure audits, development and production builds, browser inspection, and review evidence.

```bash
make test
make audit-sections
make audit-external-links
make audit-scope
```

`audit-scope` produces findings for mathematical judgment; a clean process exit is not a substitute for reviewing those findings. Compare known baseline findings with new failures, and repair regressions caused by the change. Do not silently weaken a gate to get a passing result.

For runtime changes, use the browser checks in `tests/`. Private-library verification should open a document, expand a public knowl, expand a prerequisite inside it, and test desktop and narrow screens. Production checks should establish absence of private text in all output, including JSON indexes and fragments, rather than merely hiding the header button.

## Useful ways to request a change

Describe the page, the mathematical or reading problem, and the result you want. For example: “When this definition opens inside my reading copy, I lose the hypothesis above the formula. Keep the full statement visible and inspect it on a phone-sized screen.” That gives an implementation agent an observable outcome without prescribing an architecture.

For content questions, identify the concept, convention, missing prerequisite, or source passage. For a code change, ask for its effect, appropriate tests, a rendered inspection, and a direct preview link. Fewer changes across successive refactors can suggest convergence, but passing checks and a usable reading experience are stronger evidence than an agent's preference for or against refactoring.
