from flask import Blueprint, request, jsonify
from services.conference_service import ConferenceService
from schemas.conference_schema import ConferenceCreate

conf_bp = Blueprint('conferences', __name__)

@conf_bp.route('/conferences', methods=['GET'])
def show_conferences():
    conferences = ConferenceService.get_conferences()
    # result = conference_schema.dump(conference, many=True)
    
    # return jsonify(result)
    return jsonify({"code": 0})

@conf_bp.route('/conferences', methods=['POST'])
def create_conference():
    data = request.get_json()
    conf_data = ConferenceCreate(**data)
    
    result = ConferenceService.create_conference(conf_data)
    
    
    return jsonify(result), 201
    