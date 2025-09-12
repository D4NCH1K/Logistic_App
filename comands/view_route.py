from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class ViewRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if not self.app_data.routs:
            return f"Route not found."

        route_info = []
        for route in self.app_data.routs:
            route_info.append(route.info())
        return "\n".join(route_info)