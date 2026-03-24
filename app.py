from flask import Flask
from config import Config
from extensions import db, login_manager
from models import User

from routes.auth import auth_bp
from routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # INIT EXTENSIONS
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # USER LOADER
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # S3 INJECT TO FRONTEND
    @app.context_processor
    def inject_config():
        return {
            "S3_BASE_URL": app.config["S3_BASE_URL"]
        }

    # REGISTER BLUEPRINTS
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=80, debug=False)
