"""Shared pytest fixtures.

Add here: test client fixture, test DB session (SQLite in-memory or a
disposable SQL Server container), factory helpers.
"""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> TestClient:
    # Imported lazily so env vars can be set by test config first.
    from app.main import app

    return TestClient(app)
