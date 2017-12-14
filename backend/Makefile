FLASK_APP ?= main.py

.DEFAULT_GOAL: help
.PHONY: help dev setup dev-setup shell test

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


setup: ## Install reqs
	pip install -r requirements.txt
	pip install -e .

dev-setup: setup  ## Install dev reqs
	pip install -r requirements-dev.txt

test-setup: setup ## Install testing reqs
	pip install -r requirements-test.txt

dev: ## Run dev server
	export FLASK_APP=${FLASK_APP} && flask run

shell: ## Run flash shell
	export FLASK_APP=${FLASK_APP} && flask shell

test: test-setup ## Run tests
	find . -name "*.pyc" -delete
	py.test
