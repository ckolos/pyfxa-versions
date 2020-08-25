DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Available rules:"
	@fgrep -h "##" Makefile | fgrep -v fgrep | sed 's/\(.*\):.*##/\1:/'

.PHONY: clean
clean:  ## Clean build artifacts
	rm -rf build dist *.egg-info .pytest-cache
	find . -name __pycache__ | xargs rm -rf
	find . -name '*.pyc' | xargs rm -rf

.PHONY: build
build: clean  ## Build sdist
	python setup.py sdist
