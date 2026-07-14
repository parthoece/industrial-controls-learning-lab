.PHONY: install test labs check clean

install:
	python -m pip install -e ".[dev]"

test:
	pytest

labs:
	python -m industrial_controls_lab list
	python -m industrial_controls_lab run plant
	python -m industrial_controls_lab run pid
	python -m industrial_controls_lab run machine
	python -m industrial_controls_lab run motion
	python -m industrial_controls_lab run manufacturing

check:
	python -m compileall -q src tests scripts
	pytest
	python scripts/check_repo.py

clean:
	rm -rf .pytest_cache .coverage htmlcov build dist *.egg-info src/*.egg-info
