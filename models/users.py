from models.user_role import UserRole

class User:
    def __init__(self, login: str):
        self.login = login
        self._user_role = UserRole.username(login)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        if len(login) == 0:
            raise ValueError("Login must include at least one symbol")
        self._login = login

    @property
    def user_role(self):
        return self._user_role

    def info(self):
        return f"Login: {self.login}, Role: {self.user_role}"
