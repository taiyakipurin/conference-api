from flask import Blueprint, request, jsonify
from services.registration_service import RegistrationService
from schemas.registration import RegistrationCreate
from models.registration import Registration

register_bp = Blueprint('registrations', __name__)

@register_bp.route('/registrations', methods=['POST'])
def create_registration():
    data = request.get_json()
    registration_data = RegistrationCreate(**data)
    new_registration = RegistrationService.create_registration(registration_data)
    if isinstance(new_registration, Registration):
        return jsonify(new_registration.to_dict()), 201
    else:
        return jsonify(new_registration), 400


@register_bp.route('/registrations', methods=['GET'])
def list_registrations():
    registrations = RegistrationService.get_all()

    return jsonify({"registrations": [registration.to_dict() for registration in registrations]}), 200

@register_bp.route('/registrations/<int:registation_id>', methods=['GET'])
def get_registration(registration_id: int):
    registration = RegistrationService.get_registration_by_id(registration_id)

    if registration is None:
        return jsonify({"Error": f"Registration with id {registration_id} not found"}), 404

    return jsonify(registration.to_dict())

@register_bp.route('/registrations/<int:registration_id>', methods=['DELETE'])
def delete_registration(registration_id: int):
    result = RegistrationService.delete_registration_by_id(registration_id)

    if result is None:
        return jsonify({"Error": f"Registration with id {registration_id} not found"}), 404

    return jsonify(result), 200

