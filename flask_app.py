from flask import Flask

from blueprints.core import core_bp
from blueprints.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(core_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    return app

app = create_app()



if __name__ == "__main__":
    app.run(debug=True)
