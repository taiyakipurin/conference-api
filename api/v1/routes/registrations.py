from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user
from schemas.user import UserRegisterSchema
from pydantic import ValidationError

register_bp = Blueprint('registrations', __name__)

@register_bp.route('/registrations', methods=['POST'])
def create_registration():
    pass

@register_bp.route('/registrations', methods=['GET'])
def get_registrations():
    pass

@register_bp.route('/registrations/<int:registation_id>', methods=['GET'])
def get_registration(registration_id):
    pass

