import marshmallow_dataclass

from user.model import User
from utils.web_client import WebClient


class UserService:
    @staticmethod
    def get_by_id(user_id: int):
        base_url = 'https://reqres.in/api/users'
        request_url = f'{base_url}/{user_id}'
        request_data, response_code = WebClient.get_json_from_request(request_url)

        if response_code == 200:
            UserSchema = marshmallow_dataclass.class_schema(User)
            user_data = request_data['data']
            user = UserSchema().load(user_data)
            print(user_data, user)
            return user, response_code
        else:
            return None, response_code