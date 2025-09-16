import os

def get_settings():
    return {
        "HOST": os.getenv("HOST", "0.0.0.0"),
        "PORT": os.getenv("PORT", "5000"),
        "FLASK_ENV": os.getenv("FLASK_ENV", "development"),
    }
