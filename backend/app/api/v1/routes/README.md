# app/api/v1/routes/

**One router file per feature** (e.g. `orders.py`, `users.py`).

Belongs here:
- FastAPI `APIRouter` definitions, path operations, dependency injection
- Parsing/validating requests via schemas, returning response schemas
- Calling a service function and translating its result to HTTP

Does NOT belong here:
- Business logic → `app/services/`
- Database queries → `app/repositories/`
- Data shapes → `app/schemas/`

Register new routers in `app/main.py`.
