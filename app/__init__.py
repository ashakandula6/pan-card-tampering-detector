from flask import Flask

app = Flask(__name__)

env = app.config.get("ENV", "development")  # Default to development if not set

if env == "production":
    app.config.from_object("config.ProductionConfig")
elif env == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app import views