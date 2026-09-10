"""Application entry point — app factory and router registration.

Keep this file thin: it only wires things together. Logic lives in the layers
(routes → services → repositories).
"""
from fastapi import FastAPI

from app.api.v1.routes import health
from app.core.config import get_settings
from app.middleware.cors import add_cors


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version="0.1.0")

    add_cors(app, settings)

    # Register one router per feature under the versioned prefix.
    app.include_router(health.router, prefix="/api/v1", tags=["health"])
    # app.include_router(orders.router, prefix="/api/v1", tags=["orders"])

    return app


app = create_app()
