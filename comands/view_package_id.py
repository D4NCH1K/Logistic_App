from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class ViewPackageID(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if len(self._params) < 1:
            raise ValueError("Please, enter the provided ID for package")
        if len(self._params) > 1:
            raise ValueError("You can use one ID for this command")

        delivery_id = int(self._params[0])
        package = self.app_data.find_package(delivery_id)

        if not package:
            return f"Package with ID {delivery_id} not found!"

        return package.info()