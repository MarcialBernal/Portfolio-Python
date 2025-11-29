from .gateways import UsersGateway

API_URL = "http://localhost:8000"

# ============================================================
#                    USERS (GYM ASSISTANT)
# ============================================================
class UsersUsecase:
    def __init__(self):
        self.gateway = UsersGateway(base_url=API_URL)

    def list_users(self):
        return self.gateway.get_users()

    def get_user(self, name: str):
        return self.gateway.get_user_by_name(name)

    def get_user_by_name_and_age(self, name: str, age: int):
        return self.gateway.get_user_by_name_and_age(name, age)

    def add_user(self, user_data: dict):
        return self.gateway.create_user(user_data)

    def modify_user(self, user_id: int, user_data: dict):
        return self.gateway.update_user(user_id, user_data)

    def remove_user(self, user_id: int):
        return self.gateway.delete_user(user_id)