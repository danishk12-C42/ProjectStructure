# app/repositories/

**Data-access layer — one file per feature** (e.g. `orders.py`).

Belongs here:
- All SQLAlchemy queries (select/insert/update/delete)
- Functions that take a `Session` and return ORM models or primitives

Does NOT belong here:
- Business decisions → `app/services/`
- HTTP concerns → `app/api/v1/routes/`

Rule: this is the ONLY place that talks to the database. If the DB ever
changes, only this layer changes.
