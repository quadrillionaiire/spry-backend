# app/routes/__init__.py
def register_routes(app):
    from .auth_routes import auth_bp
    from .event_routes import event_bp
    from .messaging_routes import messaging_bp
    from .user_routes import user_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(event_bp, url_prefix='/events')
    app.register_blueprint(messaging_bp, url_prefix='/messages')
    app.register_blueprint(user_bp, url_prefix='/users')
