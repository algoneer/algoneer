TESTARGS := ${testargs}

all: format mypy test

format:
	black algoneer/
	black examples/

mypy:
	mypy algoneer/

test:
	py.test algoneer_tests ${TESTARGS}

update:
	pip3 install pur
	pur -r requirements.txt
	pur -r requirements-test.txt

release:
	python3 setup.py sdist
	twine upload --skip-existing dist/* -u ${TWINE_USER} -p ${TWINE_PASSWORD}
