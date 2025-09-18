from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from models.truck_status import TruckStatus

class ViewFreeTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        city = self._params[0]
        free_truck = []

        for truck in self.app_data.trucks:
            if truck.current_loc == city and truck.status == TruckStatus.FREE:
                free_truck.append(truck)

        if not free_truck:
            print( f"Not free truck available in {city}\n")

        output_lines = [truck.info() for truck in free_truck]
        output = f"Free trucks in {city}:\n\n" + "\n\n".join(output_lines)
        print(output)

        return ""