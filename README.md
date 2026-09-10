# Product Monorepo

Web product for external clients — React frontend + FastAPI backend + SQL Server, deployed to Azure.

## Repository layout

| Path | Purpose |
|---|---|
| `frontend/` | React (Vite + TypeScript) web client |
| `backend/` | FastAPI REST API (Python) |
| `infra/` | Docker Compose + Azure (Bicep) deployment files |
| `docs/` | Architecture, API conventions, git workflow, onboarding |
| `.github/` | CI pipelines (GitHub Actions), PR template, CODEOWNERS |

## Quick start

```bash
# Backend
cd backend
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements/dev.txt
copy .env.example .env                            # then fill in values
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
copy .env.example .env
npm run dev
```

Or run everything with Docker:

```bash
docker compose -f infra/docker-compose.yml up --build
```

## Before your first commit

1. Read [docs/git-workflow.md](./docs/git-workflow.md) — branch naming, commit format, PR rules.
2. Install pre-commit hooks: `pip install pre-commit && pre-commit install` (repo root).
3. Frontend hooks are installed automatically by `npm install` (husky).

## Documentation

- [Architecture](./docs/architecture.md)
- [API conventions](./docs/api-conventions.md)
- [Git workflow](./docs/git-workflow.md)
- [Onboarding](./docs/onboarding.md)
