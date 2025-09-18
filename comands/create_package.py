from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class CreatePackage(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        start_location = self._params[0]
        end_location = self._params[1]
        weight = float(self._params[2])
        contact_info = self._params[3]

        package = self.app_data.create_package(start_location, end_location, weight, contact_info)

        return f"Package with ID {package.delivery_id} was created"