from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from datetime import datetime
from models.country_map import *

class CreateRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if len(self._params) < 2:
            raise ValueError("Please, enter at least 2 location")

        location = self._params
        departure_time = datetime.now()
        route = self.app_data.create_route(location, departure_time)

        for loc in self._params:
            if loc not in country_routes:
                raise ValueError(f"Wrong location!")
        if self._params[0] == self._params[1]:
            raise ValueError(f"Start and Stop location must be different!")


        return f"Route with ID {route.route_id} was created!"



