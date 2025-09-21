from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from models.package_status import PackageStatus
from models.truck_status import TruckStatus

class CompleteAllPackages(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if not self._params:
            return f"Packages not found"

        completed = []

        for package in self.app_data.package:
            if package.status == PackageStatus.IN_PROGRES:
                package.status = PackageStatus.DONE
                completed.append(package)

        for truck in self.app_data.trucks:
            if truck.status == TruckStatus.ON_THE_WAY:
                truck.status = TruckStatus.FREE
                if truck.route:
                    truck.current_loc = truck.route.end_location
                    truck.route = None


        if not completed:
            return "No packages were in progress."
        return f"Completed {len(completed)} packages."

