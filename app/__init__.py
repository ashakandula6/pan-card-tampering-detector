from flask import Flask
import os

app = Flask(__name__)

# Load config based on environment
env = os.getenv("FLASK_ENV", "development").lower()

if env == "production":
    app.config.from_object("app.config.ProductionConfig")
elif env == "testing":
    app.config.from_object("app.config.TestingConfig")
elif env == "debug":
    app.config.from_object("app.config.DebugConfig")
else:
    app.config.from_object("app.config.DevelopmentConfig")

# Ensure required directories exist
os.makedirs(app.config.get('INITIAL_FILE_UPLOADS', 'app/static/uploads'), exist_ok=True)
os.makedirs(app.config.get('EXISTNG_FILE', 'app/static/original'), exist_ok=True)
os.makedirs(app.config.get('GENERATED_FILE', 'app/static/generated'), exist_ok=True)

# Import views (routes)
from app import views