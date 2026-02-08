from flask import Flask
from .config import Config
from .extensions import db
from .routes import main_bp
from .health import health_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(health_bp)

    with app.app_context():
        db.create_all()

    return app