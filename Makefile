TESTARGS := ${testargs}

all: format mypy test

format:
	black algoneer/
	black examples/

mypy:
	mypy algoneer/

test:
	py.test tests ${TESTARGS}
