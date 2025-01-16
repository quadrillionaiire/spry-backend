from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

# Initialize database and migration tools
db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Load configuration

    db.init_app(app)  # Initialize database with app
    migrate.init_app(app, db)  # Initialize migrations with app
    api.init_app(app)  # Initialize API with app

    # Register blueprints or routes
    from app import routes
    app.register_blueprint(routes.bp)

# Import the models so they are registered with SQLAlchemy
    with app.app_context():
        from . import models  # Ensure models are imported
        db.create_all()  # Create tables if they don't exist

    return app
