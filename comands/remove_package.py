from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class RemovePackage(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        delivery_id = int(self._params[0])
        package = self.app_data.find_package(delivery_id)

        if not package:
            return f"Package with ID {delivery_id} not found!"
        self.app_data.remove_package(package)
        return f"Package with ID {delivery_id} was removed!"