# app/models/

**SQLAlchemy ORM models — one file per domain entity** (e.g. `user.py`, `order.py`).

Belongs here:
- Table definitions (columns, indexes, relationships) inheriting from `app.db.base.Base`

Does NOT belong here:
- Business logic → `app/services/`
- Request/response shapes → `app/schemas/`

After adding/changing a model:
1. Import it in `app/db/base.py` so Alembic can see it.
2. Generate a migration: `alembic revision --autogenerate -m "describe change"`.
