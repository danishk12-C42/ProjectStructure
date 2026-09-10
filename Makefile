# Common developer tasks. Run from repo root.
# Windows users: use `make` via Git Bash/WSL, or run the underlying commands directly.

.PHONY: install lint test dev-backend dev-frontend up

install:
	cd backend && pip install -r requirements/dev.txt
	cd frontend && npm install
	pre-commit install

lint:
	cd backend && ruff check . && ruff format --check . && mypy app
	cd frontend && npm run lint && npm run typecheck

test:
	cd backend && pytest
	cd frontend && npm run test

dev-backend:
	cd backend && uvicorn app.main:app --reload

dev-frontend:
	cd frontend && npm run dev

up:
	docker compose -f infra/docker-compose.yml up --build
