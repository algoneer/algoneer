TESTARGS := ${testargs}

all: mypy test

mypy:
	mypy algoneer/

test:
	py.test tests ${TESTARGS}