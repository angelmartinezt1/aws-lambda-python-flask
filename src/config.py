import os


class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"


app_config = Config()
