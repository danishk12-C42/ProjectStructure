# Onboarding — New Developer Setup

Target: productive within half a day.

## 1. Prerequisites

- Python 3.12+, Node.js 20+, Docker Desktop, Git
- VS Code extensions: Python, Pylance, Ruff, ESLint, Prettier, EditorConfig

## 2. Clone & install

```bash
git clone <repo-url>
cd <repo>

# Backend
cd backend
python -m venv .venv
.venv\Scripts\activate            # Windows (source .venv/bin/activate on mac/linux)
pip install -r requirements/dev.txt
copy .env.example .env            # fill in local values

# Frontend
cd ../frontend
npm install                       # also installs husky git hooks
copy .env.example .env

# Repo-level hooks (from repo root)
pip install pre-commit
pre-commit install
```

## 3. Database (local)

Run SQL Server in Docker (defined in `infra/docker-compose.yml`), then apply
migrations:

```bash
docker compose -f infra/docker-compose.yml up -d db
cd backend
alembic upgrade head
```

## 4. Run

```bash
# Terminal 1
cd backend && uvicorn app.main:app --reload      # http://localhost:8000/docs

# Terminal 2
cd frontend && npm run dev                        # http://localhost:5173
```

## 5. Read before coding

1. [architecture.md](./architecture.md) — where code belongs (layers & features)
2. [git-workflow.md](./git-workflow.md) — branching, commits, PRs
3. [api-conventions.md](./api-conventions.md) — endpoint & error rules
4. The `README.md` inside each folder you work in — every convention folder
   documents what belongs there and what does NOT.

## 6. Your first task

Pick a `good-first-issue`, create `feature/<ticket>-<desc>` from `main`, and
follow the PR checklist. Ask questions early — the docs should answer most;
if they don't, improve the docs in the same PR.
