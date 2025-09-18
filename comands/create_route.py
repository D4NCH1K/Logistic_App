from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from datetime import datetime

class CreateRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        location = self._params
        departure_time = datetime.now()
        route = self.app_data.create_route(location, departure_time)

        return f"Route with ID {route.route_id} was created!"



