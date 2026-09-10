# API Conventions

All backend endpoints follow these rules so the API stays predictable for the
frontend team and the external client.

## URLs

- Versioned prefix: `/api/v1/...` — breaking changes go to `/api/v2`, never into v1.
- Resources are **plural nouns**, kebab-case: `/api/v1/purchase-orders`.
- No verbs in URLs. Actions map to HTTP methods:

| Method | Meaning | Example |
|---|---|---|
| GET | Read (list or single) | `GET /api/v1/orders`, `GET /api/v1/orders/{id}` |
| POST | Create | `POST /api/v1/orders` |
| PUT/PATCH | Full / partial update | `PATCH /api/v1/orders/{id}` |
| DELETE | Delete | `DELETE /api/v1/orders/{id}` |

## Requests & responses

- JSON only; field names in `snake_case` (Pydantic default).
- Every request/response shape is a Pydantic schema in `app/schemas/` —
  never return ORM models directly.
- List endpoints are paginated:
  `GET /api/v1/orders?page=1&size=20` →
  ```json
  { "items": [...], "total": 143, "page": 1, "size": 20 }
  ```

## Errors (uniform shape)

```json
{
  "error": {
    "code": "ORDER_NOT_FOUND",
    "message": "Order 42 does not exist.",
    "details": null
  }
}
```

- 400 validation, 401 unauthenticated, 403 forbidden, 404 not found,
  409 conflict, 422 semantic validation, 500 unexpected (never leak stack traces).
- Domain exceptions live in `app/core/exceptions.py`; a single handler converts
  them to this shape.

## Status codes for writes

- `POST` → `201 Created` with the created resource in the body.
- `DELETE` → `204 No Content`.

## Documentation

- FastAPI auto-generates OpenAPI docs at `/docs` (Swagger) and `/redoc`.
- The OpenAPI spec is the single source of truth for the frontend; consider
  generating TypeScript types from it as the API grows.
