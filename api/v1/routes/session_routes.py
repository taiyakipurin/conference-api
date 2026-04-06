from flask import request, jsonify, Blueprint, abort

from services.session_service import SessionService

session_bp = Blueprint('sessions', __name__)

@session_bp.route('/sessions', methods=['POST'])
def add_session():
    data = request.get_json()

    if not data:
        abort(400, description="JSON body required")

    session = SessionService.create_session(data)

    return jsonify(session), 200

@session_bp.route('/sessions', methods=['GET'])
def list_sessions():
    sessions = SessionService.get_all()

    return jsonify({"sessions": sessions}), 200

@session_bp.route('/sessions/<int:session_id>', methods=['GET'])
def get_session(session_id: int):
    session = SessionService.get_session_by_id(session_id)

    return jsonify(session.to_dict()), 200

@session_bp.route('/sessions/<int:session_id>', methods=['DELETE'])
def delete_session(session_id: int):
    result = SessionService.delete_session_by_id(session_id)

    return jsonify(result)

@session_bp.route('/sessions/<int:session_id>', methods=['PUT'])
def update_conference(session_id: int):
    data = request.get_json()

    if not data:
        abort(400, description="JSON body required")
    try:
        updated_session = SessionService.update_session(session_id, data)

        if not updated_session:
            abort(404, description="Registration not found")

        return jsonify({"success": updated_session.to_dict()}), 200
    except Exception as e:
        abort(400, description=e.errors())