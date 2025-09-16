from flask import Flask
from .routes import register_routes
from .config import get_settings

def create_app():
    """Flask application factory."""
    app = Flask(__name__)
    app.config.from_mapping(get_settings())
    register_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host=app.config["HOST"], port=int(app.config["PORT"]))
