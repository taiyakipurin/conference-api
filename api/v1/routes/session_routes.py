from flask import request, jsonify, Blueprint
from pydantic import ValidationError

from schemas.session import SessionCreate
from services.session_service import SessionService

session_bp = Blueprint('sessions', __name__)

@session_bp.route('/sessions', methods=['POST'])
def add_session():
    data = request.get_json()
    
    try: 
        session_data = SessionCreate(**data)
        session = SessionService.create_session(session_data)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify ({"error": str(e)}), 400
    
    return jsonify(session), 201
