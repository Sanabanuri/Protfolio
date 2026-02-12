import os

class Settings:
    PROJECT_NAME: str = "Sanaullah Farooq Portfolio"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./portfolio.db")

settings = Settings()
