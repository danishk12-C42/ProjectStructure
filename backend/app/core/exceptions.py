"""Domain exceptions and their mapping to the uniform API error shape.

Services raise these; a single FastAPI exception handler converts them to the
JSON error format defined in docs/api-conventions.md. Routes never build error
responses by hand.
"""


class DomainError(Exception):
    """Base class for all business-rule errors."""

    code = "DOMAIN_ERROR"
    status_code = 400

    def __init__(self, message: str, details: object = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details


class NotFoundError(DomainError):
    code = "NOT_FOUND"
    status_code = 404


class ConflictError(DomainError):
    code = "CONFLICT"
    status_code = 409
