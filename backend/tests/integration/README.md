# tests/integration/

End-to-end API tests through the FastAPI TestClient, optionally against a real
(containerized) SQL Server. Slower — cover the critical flows, not every branch.

Naming: `test_api_<feature>.py`.
