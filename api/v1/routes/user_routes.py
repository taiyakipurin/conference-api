from flask import Blueprint, jsonify, request, abort

from services.user_service import UserService

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = UserService.get_all_users()

    return jsonify(users), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    user = UserService.get_user_by_id(user_id)

    return jsonify(user.to_dict()), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    result = UserService.delete_user_by_id(user_id)

    return jsonify(result), 200

@user_bp.route('/users/<int:users_id>', methods=['PUT'])
def update_conference(users_id: int):
    data = request.get_json()

    if not data:
        abort(400, description="JSON body required")
    try:
        updated_user = UserService.update_user(users_id, data)

        if not updated_user:
            abort(404, description="User not found")

        return jsonify({"success": updated_user.to_dict()}), 200
    except Exception as e:
        abort(400, description=e.errors())