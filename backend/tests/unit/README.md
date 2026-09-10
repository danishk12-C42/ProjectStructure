# tests/unit/

Fast, isolated tests — **mirror the `app/` structure** (e.g. `test_services_orders.py`
tests `app/services/orders.py`). No real database, no network: mock repositories.

Naming: `test_<layer>_<feature>.py`.
