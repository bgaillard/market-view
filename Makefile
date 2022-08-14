MODULE := marketview
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

# Vars

POETRY := poetry
PYTHON := python

clear:  ## Clear local env
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -Rf .mypy_cache
	rm -Rf .pytest_cache

install: ## Install dependencies
	$(POETRY) install

update: ## Update dependencies
	$(POETRY) update

lint: lint-fix typecheck  ## Run linting (local)
	$(POETRY) run black --check .
	$(POETRY) run isort --check-only **/*.py
	$(POETRY) run flake8 .
	$(POETRY) run pydocstyle .

lint-fix:  ## Run autoformatters (local)
	$(POETRY) run black .
	$(POETRY) run isort --atomic **/*.py

run:
	ENV=local $(POETRY) run $(PYTHON) $(MODULE)/main.py

test:  ## Run tests
ifdef K
	DOTENV=.env.test $(POETRY) run pytest -k "${K}"
else
	DOTENV=.env.test $(POETRY) run pytest $(MODULE)
endif

test-cov:  ## Run tests locally
	DOTENV=.env.test $(POETRY) run pytest --cov=. --cov-report=html $(MODULE)
	@echo "Coverage report has been written to htmlcov"
	python -m webbrowser -t "file://$(abspath htmlcov)/index.html"

typecheck:  ## Run typechecking (local)
	DOTENV=.env.test $(POETRY) run mypy --show-error-codes --pretty $(MODULE)

.PHONY: clear docker-build install lint lint-fix run test test-cov typecheck update

#
# File based recipes (advanced usage)
#

.DEFAULT_GOAL := help
help: Makefile
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m## /[33m/'

