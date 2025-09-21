from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class FindRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if len(self._params) < 1:
            raise ValueError("Please, enter the provided ID for route")
        if len(self._params) > 1:
            raise ValueError("You can use one ID for this command")

        route_id = int(self._params[0])
        route = self.app_data.find_route(route_id)

        if not route:
            return f"Route with ID {route_id} not found!"
        return f"Route with ID {route.route_id} was found!"
