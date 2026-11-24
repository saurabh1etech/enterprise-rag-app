
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root: enterprise-rag-chatbot/
PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4.1-mini"

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
