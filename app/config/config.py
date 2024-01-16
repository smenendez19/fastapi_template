# Configuration file

# Imports
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Template API"
    test_mode: str
    model_config = SettingsConfigDict(env_file=".env")
