from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class LoginUser(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        login = self._params[0]
        user = self.app_data.login(login)

        return f"User {user.login} logged successfully. Role: {user.user_role}"