import requests

# ============================================================
#                     USERS (GYM ASSISTANT)
# ============================================================

class UsersGateway:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_users(self):
        r = requests.get(f"{self.base_url}/gym/users")
        r.raise_for_status()
        return r.json()

    def get_user_by_name(self, name: str):
        r = requests.get(f"{self.base_url}/gym/users/{name}")
        r.raise_for_status()
        return r.json()

    def get_user_by_name_and_age(self, name: str, age: int):
        r = requests.get(f"{self.base_url}/gym/users/{name}/{age}")
        r.raise_for_status()
        return r.json()

    def create_user(self, data: dict):
        r = requests.post(f"{self.base_url}/gym/users", json=data)
        r.raise_for_status()
        return r.json()

    def update_user(self, user_id: int, data: dict):
        r = requests.put(f"{self.base_url}/gym/users/{user_id}", json=data)
        r.raise_for_status()
        return r.json()

    def delete_user(self, user_id: int):
        r = requests.delete(f"{self.base_url}/gym/users/{user_id}")
        r.raise_for_status()
        return {"detail": "User deleted successfully"}