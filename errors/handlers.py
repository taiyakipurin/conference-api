from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        response = {
            "status": "error",
            "error": error.name,
            "message": error.description
        }

        return jsonify(response), error.code

    @app.errorhandler(Exception)
    def handle_unexcpected_error(error):
        response = {
            "statis": "error",
            "error": "Internal Server Error",
            "Message": "Something went wrong"
        }

        return jsonify(response), 500