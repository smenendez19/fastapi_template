# Configuration file

# Imports
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App settings
    app_name: str = "Template API"
    debug: bool = False

    # Database settings (PostgreSQL)
    postgres_host: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_port: int

    # API settings
    api_host: str = "0.0.0.0"
    api_port: int = 8080

    @property
    def database_url(self) -> str:
        """Construct database URL from individual components."""
        return f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
