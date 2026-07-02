VENV_PYTHON := .venv/bin/python
NODE_MODULES_KATEX := node_modules/katex/dist/katex.js
PYTHON ?= $(VENV_PYTHON)
CONTENT_PACKAGE ?= ../knowlpedia-content
LEGACY_CONTENT_SOURCE ?= ../knowlpedia-content-legacy
LEGACY_IMPORT_OUT ?= imports/knowlpedia-content
PREVIEW_URL ?= http://127.0.0.1:8001
PREVIEW_PATH ?= /algebra-groups/group/
SCREENSHOT ?= tmp/screenshots/imported-group.png

.PHONY: deps build serve clean screenshot-imported
.PHONY: build-content serve-content import-legacy-content import-content
.PHONY: build-imported serve-imported build-legacy-imported

$(VENV_PYTHON): requirements.txt
	python3 -m venv .venv
	$(VENV_PYTHON) -m pip install -r requirements.txt

$(NODE_MODULES_KATEX): package.json package-lock.json
	npm install

deps: $(VENV_PYTHON) $(NODE_MODULES_KATEX)

build: deps
	$(PYTHON) packages/compiler/knowl_compile.py examples/basic --out public

serve: build
	python3 -m http.server 8000 --directory public

build-content: deps
	$(PYTHON) packages/compiler/knowl_compile.py $(CONTENT_PACKAGE) --out public-imported --allow-validation-errors

serve-content: build-content
	python3 -m http.server 8001 --directory public-imported

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
