from flask import Blueprint, request, jsonify, abort
from services.registration_service import RegistrationService
from schemas.registration import RegistrationCreate

register_bp = Blueprint('registrations', __name__)

@register_bp.route('/registrations', methods=['POST'])
def create_registration():
    data = request.get_json()

    if not data:
        abort(400, description="JSON body required")

    registration_data = RegistrationCreate(**data)
    new_registration = RegistrationService.create_registration(registration_data)

    return jsonify(new_registration.to_dict()), 201

@register_bp.route('/registrations', methods=['GET'])
def list_registrations():
    registrations = RegistrationService.get_all()

    return jsonify({"registrations": [registration.to_dict() for registration in registrations]}), 200

@register_bp.route('/registrations/<int:registation_id>', methods=['GET'])
def get_registration(registration_id: int):
    registration = RegistrationService.get_registration_by_id(registration_id)

    return jsonify(registration.to_dict())

@register_bp.route('/registrations/<int:registration_id>', methods=['DELETE'])
def delete_registration(registration_id: int):
    result = RegistrationService.delete_registration_by_id(registration_id)

    return jsonify(result), 200

@register_bp.route('/registrations/<int:registration_id>', methods=['PUT'])
def update_conference(registration_id: int):
    data = request.get_json()

    if not data:
        abort(400, description="JSON body required")
    try:
        updated_registration = RegistrationService.update_registration(registration_id, data)

        if not updated_registration:
            abort(404, description="Registration not found")

        return jsonify({"success": updated_registration.to_dict()}), 200
    except Exception as e:
        abort(400, description=e.errors())

