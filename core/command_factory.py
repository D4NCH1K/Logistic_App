from core.application_data import ApplicationData
from comands.create_route import CreateRoute
from comands.find_route import FindRoute
from comands.remove_route import RemoveRoute
from comands.view_route import ViewRoute
from comands.create_package import CreatePackage
from comands.find_package import FindPackage
from comands.remove_package import RemovePackage
from comands.view_package import ViewPackage
from comands.view_truck import ViewTruck

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "createroute":
            return CreateRoute(params, self._app_data)

        if cmd.lower() == "createpackage":
            return CreatePackage(params, self._app_data)

        if cmd.lower() == "findroute":
            return FindRoute(params, self._app_data)

        if cmd.lower() == "findpackage":
            return FindPackage(params, self._app_data)

        if cmd.lower() == "removeroute":
            return RemoveRoute(params, self._app_data)

        if cmd.lower() == "removepackage":
            return RemovePackage(params, self._app_data)

        if cmd.lower() == "viewroute":
            return ViewRoute(params, self._app_data)

        if cmd.lower() == "viewpackage":
            return ViewPackage(params, self._app_data)

        if cmd.lower() == "viewtruck":
            return ViewTruck(params, self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')