import os


class Config:
    APP_ENV = os.getenv("APP_ENV", "dev")
    DEBUG = APP_ENV != "production"
