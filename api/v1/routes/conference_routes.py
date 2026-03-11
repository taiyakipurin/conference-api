from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from services.conference_service import ConferenceService
from schemas.conference import ConferenceCreate

conf_bp = Blueprint('conferences', __name__)

@conf_bp.route('/conferences', methods=['GET'])
def list_conferences():
    conferences = ConferenceService.get_all()

    return jsonify({"conferences": conferences}), 201

@conf_bp.route('/conferences', methods=['POST'])
def create_conference():
    data = request.get_json()
    
    if not data: 
        return {"error": "no data"}, 400
    
    try:    
        conf_data = ConferenceCreate(**data)
        result = ConferenceService.create_conference(conf_data)
        return jsonify(result), 201
    except ValidationError:
        return jsonify({"Error": "Incorrect data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@conf_bp.route('/conferences/<int:conference_id>', methods=['GET'])
def get_conference(conference_id: int):
    conference = ConferenceService.get_conference_by_id(conference_id)

    if conference is None:
        return jsonify({"error": f"conference with id {conference_id} not found"}), 404

    return jsonify(conference.to_dict()), 200

@conf_bp.route('/conferences/<int:conference_id>', methods=['DELETE'])
def delete_conference(conference_id: int):
    result = ConferenceService.delete_conference_by_id(conference_id)

    if result is None:
        return jsonify({"error": f"conference with id {conference_id} not found"}), 404

    return jsonify(result), 200

        
    
    
    