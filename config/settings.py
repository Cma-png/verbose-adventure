import os

class Settings:
    PROJECT_NAME: str = "Document Search Tool"
    MODEL_NAME: str = os.getenv("MODEL_NAME", "default_model")

settings = Settings()