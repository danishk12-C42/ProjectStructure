"""Central application configuration.

All settings come from environment variables (12-factor). Locally they are
loaded from .env; in Azure they come from App Service settings / Key Vault.
Never hardcode secrets or environment-specific values anywhere else.
"""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str = "local"
    app_name: str = "product-backend"
    log_level: str = "INFO"

    database_url: str

    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    cors_origins: list[str] = ["http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
