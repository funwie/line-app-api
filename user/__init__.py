from .model import User  # noqa
from .schema import UserDemoSchema  # noqa


def register_routes(api, app, root='api'):
    from flask import Blueprint
    from flask_restx import Api

    bp = Blueprint('user_api', __name__)
    api = Api(bp, title='API documentation', version='0.1.0')

    from .controller import api as user_api

    api.add_namespace(user_api, path='/users')
    app.register_blueprint(bp, url_prefix=f'/{root}/')