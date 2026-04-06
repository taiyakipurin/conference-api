from flask import jsonify, current_app
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        current_app.logger.warning(
            f"{error.code} {error.name}: {error.description}"
        )
        response = {
            "status": "error",
            "error": error.name,
            "message": error.description
        }

        return jsonify(response), error.code

    @app.errorhandler(Exception)
    def handle_unexcpected_error(error):
        current_app.logger.exception("Unhandled exception occurred")
        response = {
            "statis": "error",
            "error": "Internal Server Error",
            "Message": "Something went wrong"
        }

        return jsonify(response), 500