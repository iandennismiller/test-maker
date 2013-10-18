SHELL=/bin/bash

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info *.pyc

test:
	fswatch tests:TestMaker 'PYTHONDONTWRITEBYTECODE=1 nosetests tests -a "!slow,!skip,!online" --with-snort'

.PHONY: clean install test
