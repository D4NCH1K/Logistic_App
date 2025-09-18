from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class ViewTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        truck_info = [t.info() for t in self._app_data.trucks]
        output = "\n\n".join(truck_info)
        print(output)
        return ""