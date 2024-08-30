#!/usr/bin/env just -S --justfile

# SPDX-FileCopyrightText: 2024 Tomodachi94 and contributors
#
# SPDX-License-Identifier: MIT

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
