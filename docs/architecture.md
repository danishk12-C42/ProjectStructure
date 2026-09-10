# Architecture

## Overview

```
[React SPA]  --HTTPS/JSON-->  [FastAPI /api/v1]  --SQLAlchemy-->  [SQL Server]
   frontend/                      backend/                          (Azure SQL)
```

- **Frontend**: React + TypeScript SPA (Vite). Talks to the backend only through
  the single API client in `src/services/api-client.ts`.
- **Backend**: FastAPI, layered architecture (see below). Exposes versioned REST
  endpoints under `/api/v1`.
- **Database**: SQL Server. Schema is managed exclusively through Alembic
  migrations — never by hand.
- **Hosting**: Azure (App Service / Container Apps). Both apps are containerized
  (`Dockerfile` in each), composed locally via `infra/docker-compose.yml`.

## Backend layers

Request flow: `route → service → repository → DB`

| Layer | Folder | Responsibility | MUST NOT do |
|---|---|---|---|
| Routes | `app/api/v1/routes/` | HTTP concerns: parse request, call service, return schema | Business logic, SQL |
| Schemas | `app/schemas/` | Pydantic request/response contracts | ORM access |
| Services | `app/services/` | Business rules, orchestration | HTTP objects, raw SQL |
| Repositories | `app/repositories/` | All database queries | Business decisions |
| Models | `app/models/` | SQLAlchemy ORM table definitions | Logic |

Why: each layer is independently testable and replaceable; every developer knows
exactly where new code belongs, keeping the codebase consistent as the team grows.

## Feature-based modularity

Both apps are organized **by feature, not by file type** where it matters:

- Backend: one file per feature inside each layer (`services/orders.py`,
  `repositories/orders.py`, `routes/orders.py`).
- Frontend: `src/features/<feature>/` contains everything the feature needs
  (components, hooks, api calls, types).

Why: developers working on different features touch **different files**, which
drastically reduces merge conflicts, and a defect in one feature stays isolated.

## Cross-cutting concerns

- **Config**: `app/core/config.py` reads environment variables (12-factor).
  Local values go in `.env` (never committed); `.env.example` documents them.
- **Auth/security**: `app/core/security.py` (JWT helpers, password hashing).
- **Errors**: `app/core/exceptions.py` defines domain exceptions; middleware maps
  them to consistent HTTP error responses (see `docs/api-conventions.md`).
- **Logging**: structured logging configured in `app/core/logging.py`.

## Decisions log

Record significant decisions here (or adopt ADRs) so future team members
understand *why*, not just *what*.

| Date | Decision | Reason |
|---|---|---|
| 2026-09 | Monorepo | Atomic full-stack PRs; right-sized for 5–10 devs |
| 2026-09 | FastAPI + React + SQL Server | Team skills + client requirements |
