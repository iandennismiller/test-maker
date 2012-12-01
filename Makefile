SHELL=/bin/bash

clean:
	rm -rf build dist *.egg-info *.pyc

install:
	python setup.py install

dep:
	pip install -r pip_req.txt

test:
	@echo test

.PHONY: clean install test dep
