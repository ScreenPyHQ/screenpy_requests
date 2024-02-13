# shortcuts to help manage flipping between branches with different dependencies
sync:
	poetry install --extras dev_all --sync

update_lock_only:
	poetry update --lock

update: update_lock_only
	poetry install --extras dev_all

check:
	poetry check

trunk_screenpy:
	poetry add screenpy git+ssh://git@github.com:ScreenPyHQ/screenpy.git#trunk

local_screenpy:
	pip uninstall screenpy
	pip install -e ~/projects/screenpy

requirements:
	poetry export --without-hashes --with dev -f requirements.txt > requirements.txt

.PHONY: sync update trunk_screenpy local_screenpy, requirements

black-check:
	black --check .

black-fix:
	black .

isort-check:
	isort . --check

isort-fix:
	isort .

ruff-check:
	ruff check .

ruff-fix:
	ruff check . --fix --show-fixes

mypy:
	mypy .

.PHONY: black-check black-fix isort-check isort-fix ruff-check ruff-fix mypy

pre-check-in: black-check ruff-check mypy

pre-check-in-fix: black-fix ruff-fix mypy

.PHONY: pre-check-in pre-check-in-fix
