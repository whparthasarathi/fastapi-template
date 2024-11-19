from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Template"
    debug: bool = True
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
