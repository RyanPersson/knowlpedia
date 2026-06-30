.PHONY: build serve clean

build:
	python3 packages/compiler/knowl_compile.py examples/basic --out public

serve: build
	python3 -m http.server 8000 --directory public

clean:
	rm -rf public

