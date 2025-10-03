.PHONY: help install dev up down logs restart clean migrate migration shell test

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies locally
	pip install -r requirements.txt

dev: ## Start development server locally
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

up: ## Start all services with Docker
	docker-compose up -d
	@echo "✅ Services started!"
	@echo "📚 API Docs: http://localhost:8000/docs"

down: ## Stop all services
	docker-compose down

logs: ## Show logs from all services
	docker-compose logs -f

logs-api: ## Show API logs only
	docker-compose logs -f api

logs-db: ## Show database logs only
	docker-compose logs -f postgres

restart: ## Restart all services
	docker-compose restart

restart-api: ## Restart API service only
	docker-compose restart api

clean: ## Stop and remove all containers, volumes, and images
	docker-compose down -v
	docker system prune -f

migrate: ## Run database migrations
	alembic upgrade head

migrate-docker: ## Run migrations in Docker
	docker-compose exec api alembic upgrade head

migration: ## Create a new migration (use MSG="description")
	alembic revision --autogenerate -m "$(MSG)"

migration-docker: ## Create a new migration in Docker (use MSG="description")
	docker-compose exec api alembic revision --autogenerate -m "$(MSG)"

shell: ## Open a shell in the API container
	docker-compose exec api /bin/bash

db-shell: ## Open PostgreSQL shell
	docker-compose exec postgres psql -U postgres -d robert_portfolio

test: ## Run tests (to be implemented)
	pytest

format: ## Format code with black
	black app/

lint: ## Lint code with ruff
	ruff check app/

build: ## Build Docker images
	docker-compose build

rebuild: ## Rebuild Docker images from scratch
	docker-compose build --no-cache

ps: ## Show running containers
	docker-compose ps

health: ## Check API health
	@curl -s http://localhost:8000/health | python -m json.tool || echo "API is not responding"

