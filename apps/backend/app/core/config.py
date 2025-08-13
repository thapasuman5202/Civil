from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "secret"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
