.PHONY: help
help:             ## Show the help.
		@echo "Usage: make <target>"
		@echo ""
		@echo "Targets:"
		@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: install
install:          
		@poetry install

.PHONY: show
show:             ## Show the current environment.
		@echo "Current environment:"
		@poetry env info

.PHONY: clean
clean:            ## Clean unused files.
		@find . -name '*.pyc' -exec rm -f {} \;
		@find . -name '__pycache__' -exec rm -rf {} \;
		@find . -name 'Thumbs.db' -exec rm -f {} \;
		@find . -name '*~' -exec rm -f {} \;
		@rm -rf .cache
		@rm -rf .pytest_cache
		@rm -rf .mypy_cache
		@rm -rf build
		@rm -rf dist
		@rm -rf *.egg-info
		@rm -rf htmlcov
		@rm -rf .tox/
		@rm -rf docs/_build
