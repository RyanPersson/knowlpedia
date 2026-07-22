VENV_PYTHON := .venv/bin/python
VENV_STAMP := .venv/.deps-installed
NODE_MODULES_STAMP := node_modules/.deps-installed
PYTHON ?= $(VENV_PYTHON)
CONTENT_PACKAGE ?= ../knowlpedia-content
EXTRA_CONTENT_SOURCES ?= ../conjectures-catalog
COMPOSED_CONTENT_PACKAGE ?= .knowl-cache/content-package
PRODUCTION_CONTENT_PACKAGE ?= .knowl-cache/production-content-package
CONTENT_SOURCE_ARGS = $(foreach source,$(EXTRA_CONTENT_SOURCES),--source $(source))
KNOWLPEDIA_PROFILE ?= development
DIAGRAM_CACHE_DIR ?= .knowl-cache/diagrams
PREBUILT_DIAGRAM_DIR ?= prebuilt/diagrams
DIAGRAM_SOURCE ?= ../knowlpedia-content/testing/algebra-category-theory/tikz-lab-whiskering-coherence.knowl.md
DIAGRAM_INDEX ?= 1
DIAGRAM_PREVIEW_OUT ?= tmp/tikz-preview
PAGE ?= algebra-category-theory/tikz-lab-whiskering-coherence
PREVIEW_URL ?= http://127.0.0.1:8001
PREVIEW_PATH ?= /algebra-groups/group/
SCREENSHOT ?= tmp/screenshots/page.png

.PHONY: deps build build-production serve clean screenshot test test-ui test-local-sources-ui audit-sections refresh-prebuilt-diagrams
.PHONY: compose-content compose-production-content build-content serve-content build-page preview-diagram
.PHONY: preview-start preview-status preview-stop preview-restart preview-scan preview-adopt
.PHONY: check-rendering check-rendering-knowls check-rendering-content

$(VENV_STAMP): requirements.txt
	python3 -m venv .venv
	$(VENV_PYTHON) -m pip install -r requirements.txt
	touch $(VENV_STAMP)

$(NODE_MODULES_STAMP): package.json package-lock.json
	npm install
	touch $(NODE_MODULES_STAMP)

deps: $(VENV_STAMP) $(NODE_MODULES_STAMP)

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py'

test-ui:
	PREVIEW_URL=$(PREVIEW_URL) node tests/runtime_smoke.mjs

test-local-sources-ui:
	PREVIEW_URL=$(PREVIEW_URL) node tests/local_sources_smoke.mjs

audit-sections:
	$(PYTHON) scripts/audit_section_split.py $(CONTENT_PACKAGE)/content
	@if [ -d "$(CONTENT_PACKAGE)/testing" ]; then $(PYTHON) scripts/audit_section_split.py $(CONTENT_PACKAGE)/testing; fi

compose-content:
	$(PYTHON) scripts/compose_content.py --primary $(CONTENT_PACKAGE) $(CONTENT_SOURCE_ARGS) --out $(COMPOSED_CONTENT_PACKAGE)

# Production deliberately composes only the GitHub-backed primary package. The
# exact-source guard prevents local-only contributors from leaking into Pages.
compose-production-content:
	$(PYTHON) scripts/compose_content.py --primary $(CONTENT_PACKAGE) --out $(PRODUCTION_CONTENT_PACKAGE) --expect-source $(CONTENT_PACKAGE)

build: build-content

serve: serve-content

build-content: deps compose-content
	$(PYTHON) packages/compiler/knowl_compile.py $(COMPOSED_CONTENT_PACKAGE) --profile $(KNOWLPEDIA_PROFILE) --out public-imported --allow-validation-errors --diagram-cache-dir $(DIAGRAM_CACHE_DIR) --prebuilt-diagram-dir $(PREBUILT_DIAGRAM_DIR)

build-production: deps compose-production-content
	$(PYTHON) packages/compiler/knowl_compile.py $(PRODUCTION_CONTENT_PACKAGE) --profile production --out public-imported --allow-validation-errors --no-diagram-cache --prebuilt-diagram-dir $(PREBUILT_DIAGRAM_DIR) --prebuilt-only-diagrams
	$(PYTHON) scripts/check_rendering_errors.py public-imported --require-rendered-diagrams --require-profile production

refresh-prebuilt-diagrams: deps compose-content
	$(PYTHON) packages/compiler/knowl_compile.py $(COMPOSED_CONTENT_PACKAGE) --profile development --out public-imported --allow-validation-errors --no-diagram-cache --prebuilt-diagram-dir $(PREBUILT_DIAGRAM_DIR) --refresh-prebuilt-diagrams

build-page: deps compose-content
	$(PYTHON) packages/compiler/knowl_compile.py $(COMPOSED_CONTENT_PACKAGE) --profile $(KNOWLPEDIA_PROFILE) --out public-imported --allow-validation-errors --only $(PAGE) --diagram-cache-dir $(DIAGRAM_CACHE_DIR) --prebuilt-diagram-dir $(PREBUILT_DIAGRAM_DIR)

preview-diagram: deps
	$(PYTHON) packages/compiler/preview_diagram.py $(DIAGRAM_SOURCE) --index $(DIAGRAM_INDEX) --out $(DIAGRAM_PREVIEW_OUT) --diagram-cache-dir $(DIAGRAM_CACHE_DIR)

serve-content: build-content
	python3 -m http.server 8001 --directory public-imported

preview-start: build-content
	$(PYTHON) scripts/preview_server.py start

preview-status:
	$(PYTHON) scripts/preview_server.py status --scan

preview-stop:
	$(PYTHON) scripts/preview_server.py stop

preview-adopt:
	$(PYTHON) scripts/preview_server.py adopt

preview-restart: build-content
	$(PYTHON) scripts/preview_server.py restart

preview-scan:
	$(PYTHON) scripts/preview_server.py scan

check-rendering:
	$(PYTHON) scripts/check_rendering_errors.py public-imported

check-rendering-knowls:
	$(PYTHON) scripts/check_rendering_errors.py public-imported --fragments-only

check-rendering-content: build-content check-rendering

screenshot:
	mkdir -p tmp/screenshots
	firefox --headless --screenshot $(abspath $(SCREENSHOT)) --window-size 1440,1200 $(PREVIEW_URL)$(PREVIEW_PATH)

clean:
	rm -rf public-imported
	rm -rf $(COMPOSED_CONTENT_PACKAGE)
	rm -rf $(PRODUCTION_CONTENT_PACKAGE)
