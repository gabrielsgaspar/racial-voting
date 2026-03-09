.PHONY: bootstrap download_anes build_dictionary clean_anes figures test lint

bootstrap:
	python scripts/00_bootstrap.py

download_anes:
	python scripts/01_download_anes.py

build_dictionary:
	python scripts/02_build_dictionary.py

clean_anes:
	python scripts/03_clean_anes.py

figures:
	python scripts/04_make_figures.py

test:
	pytest -q

lint:
	ruff check .
