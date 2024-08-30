#!/usr/bin/env just -S --justfile

test:
	poetry install --with test
	poetry run python -m pokemon_images.tests

ruff:
	ruff check .

mypy:
	poetry install
	poetry run mypy -m pokemon_images

lint: ruff mypy

publish:
	poetry build
	poetry publish
