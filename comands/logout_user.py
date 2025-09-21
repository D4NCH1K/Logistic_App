from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class LogoutUser(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if not self.app_data.has_logged_in_user:
            return f"No user is currently logged in!"

        name = self.app_data.logged_in_user.login
        self.app_data.logout()

        return f"{name} logged out!"
