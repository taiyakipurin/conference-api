from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from services.conference_service import ConferenceService
from schemas.conference_schema import ConferenceCreate

conf_bp = Blueprint('conferences', __name__)

# @conf_bp.route('/conferences', methods=['GET'])
# def show_conferences():
    # conferences = ConferenceService.get_conferences()

    # return jsonify({"code": conferences})

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
   
        
    
    
    