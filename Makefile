SERVICE_NAME ?= 'insuratech'

.DEFAULT_GOAL: help
.PHONY: help setup test backend clean

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


setup: ## Install reqs
	docker-machine create -d virtualbox ${SERVICE_NAME}
	eval $(docker-machine env ${SERVICE_NAME})


backend: ## Run the backend service
	docker-compose build backend
	docker-compose up -d backend
	docker-compose run --rm backend alembic upgrade head

test-setup: ## Setup for tests
	docker-compose -f docker-compose.test.yml build

test: test-setup ## Run tests
	docker-compose -f docker-compose.test.yml run test

clean: ## Clean docker-compose
	docker-compose stop
	docker-compose rm
	docker volume prune
