from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from models.country_map import *

class CreatePackage(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if len(self._params) < 4:
            raise ValueError("Please, enter: start_location, end_location, weight, contact_info")
        if len(self._params) > 4:
            raise ValueError("Sorry, but you cannot use more then 4 parameters. Try again")

        start_location = self._params[0]
        end_location = self._params[1]
        weight = float(self._params[2])
        contact_info = self._params[3]

        package = self.app_data.create_package(start_location, end_location, weight, contact_info)

        if start_location not in country_routes or end_location not in country_routes:
            raise ValueError("Wrong location!")
        if start_location == end_location:
            raise ValueError("Start and End location must be different!")
        if weight <= 0:
            raise ValueError("Weight cannot be zero or negative!")

        return f"Package with ID {package.delivery_id} was created"