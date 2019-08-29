TESTARGS := ${testargs}

SHELL := /bin/bash

.PHONY: docs

all: format mypy test

format:
	venv/bin/black algoneer/
	venv/bin/black examples/

mypy:
	venv/bin/mypy algoneer/

test:
	venv/bin/py.test algoneer_tests ${TESTARGS}

docs:
	source venv/bin/activate && cd docs && make html

serve-docs:
	venv/bin/python -m http.server -d docs/build/html

setup: virtualenv requirements

docs-setup: virtualenv docs-requirements

teardown:
	rm -rf venv
	rm -rf docs/build/*

virtualenv:
	virtualenv --python python3 venv

docs-requirements:
	venv/bin/pip install -r docs/requirements.txt

requirements:
	venv/bin/pip install -r requirements.txt
	venv/bin/pip install -r requirements-optional.txt
	venv/bin/pip install -r requirements-test.txt

update:
	venv/bin/pip install pur
	venv/bin/pur -r requirements.txt
	venv/bin/pur -r requirements-test.txt

release:
	venv/bin/pip install twine
	venv/bin/python setup.py sdist
	venv/bin/twine upload --skip-existing dist/* -u ${TWINE_USER} -p ${TWINE_PASSWORD}
