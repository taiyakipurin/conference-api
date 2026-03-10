from flask import Flask, jsonify, request, Blueprint
from flask_restful import Api

from database import db
from config import Config

from api.v1.routes.auth_routes import auth_bp
from api.v1.routes.session_routes import session_bp
from api.v1.routes.conference_routes import conf_bp

from resources.user_resource import UserListResource 


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1 = Api(api_v1_bp)

@api_v1_bp.route('/')
def hello():
    return {
        "message": "The server is on"
    }

api_v1_bp.register_blueprint(auth_bp, url_prefix='auth')
api_v1_bp.register_blueprint(session_bp)
api_v1_bp.register_blueprint(conf_bp)
app.register_blueprint(api_v1_bp)

api_v1.add_resource(UserListResource, '/users')

if __name__ == '__main__':
    print('\nAvailable routes:')
    print('[POST] /api/v1/auth/register: register user')
    print('[POST] /api/v1/auth/login: log in exist account')
    
    print('\n', app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)
