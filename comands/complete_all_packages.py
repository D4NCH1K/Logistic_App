from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class CompleteAllPackages(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        pass