from flask import Blueprint, jsonify

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