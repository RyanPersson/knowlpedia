VENV_PYTHON := .venv/bin/python
VENV_STAMP := .venv/.deps-installed
NODE_MODULES_STAMP := node_modules/.deps-installed
PYTHON ?= $(VENV_PYTHON)
CONTENT_PACKAGE ?= ../knowlpedia-content
LEGACY_CONTENT_SOURCE ?= ../knowlpedia-content-legacy
LEGACY_IMPORT_OUT ?= imports/knowlpedia-content
DIAGRAM_CACHE_DIR ?= .knowl-cache/diagrams
DIAGRAM_SOURCE ?= ../knowlpedia-content/content/algebra-category-theory/tikz-lab-whiskering-coherence.knowl.md
DIAGRAM_INDEX ?= 1
DIAGRAM_PREVIEW_OUT ?= tmp/tikz-preview
PAGE ?= algebra-category-theory/tikz-lab-whiskering-coherence
PREVIEW_URL ?= http://127.0.0.1:8001
PREVIEW_PATH ?= /algebra-groups/group/
SCREENSHOT ?= tmp/screenshots/imported-group.png

.PHONY: deps build serve clean screenshot-imported test test-ui audit-sections
.PHONY: build-content serve-content import-legacy-content import-content
.PHONY: build-page preview-diagram build-imported serve-imported build-legacy-imported
.PHONY: preview-start preview-status preview-stop preview-restart preview-scan preview-adopt
.PHONY: check-rendering check-rendering-content

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

audit-sections:
	$(PYTHON) scripts/audit_section_split.py $(CONTENT_PACKAGE)/content

build: deps
	$(PYTHON) packages/compiler/knowl_compile.py examples/basic --out public

serve: build
	python3 -m http.server 8000 --directory public

build-content: deps
	$(PYTHON) packages/compiler/knowl_compile.py $(CONTENT_PACKAGE) --out public-imported --allow-validation-errors --diagram-cache-dir $(DIAGRAM_CACHE_DIR)

build-page: deps
	$(PYTHON) packages/compiler/knowl_compile.py $(CONTENT_PACKAGE) --out public-imported --allow-validation-errors --only $(PAGE) --diagram-cache-dir $(DIAGRAM_CACHE_DIR)

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

check-rendering-content: build-content check-rendering

import-legacy-content: deps
	$(PYTHON) packages/importers/import_knowlpedia_content.py $(LEGACY_CONTENT_SOURCE) $(LEGACY_IMPORT_OUT)

import-content: import-legacy-content

build-legacy-imported: import-legacy-content
	$(PYTHON) packages/compiler/knowl_compile.py $(LEGACY_IMPORT_OUT) --out public-imported --allow-validation-errors

build-imported: build-content

serve-imported: serve-content

screenshot-imported:
	mkdir -p tmp/screenshots
	firefox --headless --screenshot $(abspath $(SCREENSHOT)) --window-size 1440,1200 $(PREVIEW_URL)$(PREVIEW_PATH)

clean:
	rm -rf public public-imported
