SHELL=/bin/bash

clean:
	rm -rf build dist *.egg-info *.pyc

install:
	python setup.py install

dep:
	pip install -r pip_req.txt

test:
	fswatch tests:TestMaker 'PYTHONDONTWRITEBYTECODE=1 nosetests tests -a "!slow,!skip,!online" --with-snort'

.PHONY: clean install test dep
