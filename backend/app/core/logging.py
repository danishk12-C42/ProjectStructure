"""Structured logging configuration.

Call setup_logging() once at startup. Use `logging.getLogger(__name__)`
everywhere — never print().
"""
import logging


def setup_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
