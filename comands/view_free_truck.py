from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from models.truck_status import TruckStatus

class ViewFreeTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if len(self._params) < 1:
            raise ValueError("Please, enter the city to view trucks")
        if len(self._params) > 1:
            raise ValueError("You can use one city for this command")

        city = self._params[0]
        free_truck = []

        for truck in self.app_data.trucks:
            if truck.current_loc == city and (truck.status == TruckStatus.FREE or truck.status == TruckStatus.ON_THE_WAY):
                free_truck.append(truck)

        if not free_truck:
            return f"Not free truck available in {city}"


        count = len(free_truck)
        output_lines = [truck.info() for truck in free_truck]
        return f"Free trucks in {city}: {count}\n\n" + "\n\n".join(output_lines)