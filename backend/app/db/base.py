"""Declarative base + model registry for Alembic autogenerate.

Import every model module here so `Base.metadata` knows about all tables.
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models below so Alembic detects them:
# from app.models.user import User  # noqa: F401
# from app.models.order import Order  # noqa: F401
