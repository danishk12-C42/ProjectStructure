# app/services/

**Business logic layer — one file per feature** (e.g. `orders.py`).

Belongs here:
- Business rules, validations spanning multiple entities, orchestration
- Raising domain exceptions from `app/core/exceptions.py`
- Calling repositories for data access

Does NOT belong here:
- HTTP objects (Request/Response) → `app/api/v1/routes/`
- SQL / ORM queries → `app/repositories/`

This is the layer unit tests target most — keep it free of framework code so
it stays trivially testable.
