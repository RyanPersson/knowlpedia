VENV_PYTHON := .venv/bin/python
NODE_MODULES_KATEX := node_modules/katex/dist/katex.js
PYTHON ?= $(VENV_PYTHON)
PREVIEW_URL ?= http://127.0.0.1:8001
PREVIEW_PATH ?= /algebra-groups/group/
SCREENSHOT ?= tmp/screenshots/imported-group.png

.PHONY: deps build serve clean screenshot-imported
.PHONY: import-content build-imported serve-imported

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

import-content: deps
	$(PYTHON) packages/importers/import_knowlpedia_content.py ../knowlpedia-content imports/knowlpedia-content

build-imported: import-content
	$(PYTHON) packages/compiler/knowl_compile.py imports/knowlpedia-content --out public-imported --allow-validation-errors

serve-imported: build-imported
	python3 -m http.server 8001 --directory public-imported

screenshot-imported:
	mkdir -p tmp/screenshots
	firefox --headless --screenshot $(abspath $(SCREENSHOT)) --window-size 1440,1200 $(PREVIEW_URL)$(PREVIEW_PATH)

clean:
	rm -rf public public-imported
