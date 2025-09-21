from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from models.truck_status import TruckStatus

class ViewRouteInProgress(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        routes_in_progress = []

        for route in self.app_data.routs:
            truck = route.truck
            if truck.status == TruckStatus.ON_THE_WAY:
                stop = route.location.index(truck.current_loc)
                if stop + 1 < len(route.location):
                    next_stop = route.location[stop + 1]
                    stop_info = f"On the way from {truck.current_loc} to {next_stop}"
                else:
                    stop_info = f"Arrived to {truck.current_loc}"

                routes_in_progress.append(
                    f"Route ID: {route.route_id} | From: {route.start_location} to {route.end_location}\n"
                    f"Stops: {" ".join(route.location[1:])}\n"
                    f"Weight: {sum(p.weight for p in truck.packages)}\n"
                    f"Expected current stop: {stop_info}"
                )

        if not routes_in_progress:
            return "No routes currently in progress."

        return "\n\n".join(routes_in_progress)