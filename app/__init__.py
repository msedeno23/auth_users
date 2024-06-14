from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_session import Session
from .config import Config
from .routes import api
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, supports_credentials=True, resources={r"/*": {"origins": Config.CORS_ORIGINS}})
    Session(app)

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    app.register_blueprint(api, url_prefix='/')

    @app.errorhandler(Exception)
    def handle_exception(e):
        logger.error("An error occurred: %s", str(e), exc_info=True)
        return jsonify({"error": "Internal Error"}), 500

    @app.before_request
    def before_request():
        logger.info("Request: %s %s", request.method, request.url)

    @app.after_request
    def after_request(response):
        logger.info("Response: %s", response.status_code)
        return response

    return app
