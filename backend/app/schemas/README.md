# app/schemas/

**Pydantic request/response schemas — one file per feature**, mirroring `models/`.

Belongs here:
- `XxxCreate`, `XxxUpdate`, `XxxRead` Pydantic models used by routes
- Validation rules on incoming data

Does NOT belong here:
- ORM/table definitions → `app/models/`
- Logic beyond field validation → `app/services/`

Rule: routes always accept and return schemas — **never expose ORM models
directly** (prevents leaking DB fields to the external client).
