from flask import Flask, Blueprint
import os

from core.extensions import db
from config.config import Config

from api.v1.routes.auth_routes import auth_bp
from api.v1.routes.session_routes import session_bp
from api.v1.routes.conference_routes import conf_bp
from api.v1.routes.user_routes import user_bp
from api.v1.routes.registration_routes import register_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_dir = os.path.join(base_dir, 'data')

    if not os.path.exists(db_dir):
        os.mkdir(db_dir)

    db.create_all()

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

@api_v1_bp.route('/')
def hello():
    return {
        "message": "The server is on"
    }

api_v1_bp.register_blueprint(auth_bp, url_prefix='auth')
api_v1_bp.register_blueprint(session_bp)
api_v1_bp.register_blueprint(conf_bp)
api_v1_bp.register_blueprint(user_bp)
api_v1_bp.register_blueprint(register_bp)
app.register_blueprint(api_v1_bp)

if __name__ == '__main__':
    print('\n', app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)
