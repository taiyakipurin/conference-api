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
    
    return jsonify(session), 200

@session_bp.route('/sessions', methods=['GET'])
def list_sessions():
    sessions = SessionService.get_all()

    return jsonify({"sessions": sessions}), 200

@session_bp.route('/sessions/<int:session_id>', methods=['GET'])
def get_session(session_id: int):
    session = SessionService.get_session_by_id(session_id)

    if session is None:
        return jsonify({"error": f"Session with id {session_id} not found"}), 404

    return jsonify(session.to_dict()), 200