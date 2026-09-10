"""Health check endpoint — used by Azure, Docker and CI to verify the app is up."""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
