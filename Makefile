TESTARGS := ${testargs}

all: format mypy test

format:
	black algoneer/
	black examples/

mypy:
	mypy algoneer/

test:
	py.test tests ${TESTARGS}

release:
	python3 setup.py sdist
	twine upload dist/* -u ${TWINE_USER} -p ${TWINE_PASSWORD}
