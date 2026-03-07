from flask import Blueprint, request, jsonify

users_bp = Blueprint('conferences', __name__)

@users_bp.route()
def show_users():
    #show_users_list()
    