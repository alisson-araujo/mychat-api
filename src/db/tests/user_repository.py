

class MockUserRepository:
    def __init__(self):
        self.insert_user_attributes = {}

    def insert_user(self, username: str, phone: str, password: str) -> int:
        self.insert_user_attributes["username"] = username
        self.insert_user_attributes["phone"] = phone
        self.insert_user_attributes["password"] = password
        return 1