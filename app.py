import os

from flask import Flask, jsonify, redirect, url_for
from flask_restx import Api
from flask_cors import CORS


def create_app(env=None):
    from config import config_by_name
    from routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="User API", version="0.1.0")
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    register_routes(api, app)

    @app.route("/health")
    def health():
        """For the microservice health check"""
        return jsonify("healthy")

    return app


app = create_app("test")
if __name__ == '__main__':
    app.run(debug=True)