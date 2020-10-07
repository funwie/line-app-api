import marshmallow_dataclass
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource, abort

from user import UserDemoSchema
from user.model import User
from user.service import UserService

api = Namespace('User', description="Get User Details")

@api.route("/<int:user_id>")
@api.param("user_id", "User Id")
class UserResource(Resource):
    UserSchema = marshmallow_dataclass.class_schema(User)
    @responds(schema=UserDemoSchema)
    def get(self, user_id: int) -> User:
        """Get Single User"""
        user, response_code = UserService.get_by_id(user_id)
        if response_code == 200:
            return user
        else:
            abort(response_code)