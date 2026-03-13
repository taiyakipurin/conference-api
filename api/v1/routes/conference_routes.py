from flask import Blueprint, request, jsonify, abort
from pydantic import ValidationError

from services.conference_service import ConferenceService

conf_bp = Blueprint('conferences', __name__)

@conf_bp.route('/conferences', methods=['GET'])
def list_conferences():
    conferences = ConferenceService.get_all()

    return jsonify({"conferences": conferences}), 201

@conf_bp.route('/conferences', methods=['POST'])
def create_conference():
    data = request.get_json()

    if not data:
        abort(400, description="JSON body required")

    try:    
        conference = ConferenceService.create_conference(data)
        return jsonify({"success": conference.to_dict()}), 201
    except ValidationError as e:
        abort(400, description=e.errors())


@conf_bp.route('/conferences/<int:conference_id>', methods=['GET'])
def get_conference(conference_id: int):
    conference = ConferenceService.get_conference_by_id(conference_id)

    return jsonify(conference.to_dict()), 200

@conf_bp.route('/conferences/<int:conference_id>', methods=['DELETE'])
def delete_conference(conference_id: int):
    result = ConferenceService.delete_conference_by_id(conference_id)

    return jsonify(result), 200

        
    
    
    