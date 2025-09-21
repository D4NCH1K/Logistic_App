from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from models.package_status import PackageStatus
from models.truck_status import TruckStatus

class AssigneePackages(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if not self._params:
            return "Please, select a package to assign"

        assigned = []
        passed = []

        for delivery_id in self._params:
            delivery_id = int(delivery_id)
            package = self.app_data.find_package(delivery_id)

            if package is None:
                passed.append((delivery_id, "Package not found"))
                continue

            if package.truck or package.route:
                passed.append((delivery_id, f"Already assigned to Route ID {package.route.route_id}, Truck ID {package.truck.vehicle_id}"))
                continue

            suitable_route = None
            truck_to_use = None

            for route in self.app_data.routs:
                if package.start_location in route.location and package.end_location in route.location:
                    trucks_on_route = [route.truck] if route.truck else []

                    for truck in trucks_on_route:
                        current_load = sum(p.weight for p in truck.packages)
                        if current_load + package.weight <= truck.capacity and route.truck_km <= truck.max_range:
                            truck_to_use = truck
                            suitable_route = route
                            break

                    if not truck_to_use:
                        for free_truck in self.app_data.trucks:
                            if (free_truck.current_loc == route.start_location and
                                    free_truck.status == TruckStatus.FREE and
                                    free_truck.capacity >= package.weight and
                                    route.truck_km <= free_truck.max_range):

                                truck_to_use = free_truck
                                suitable_route = route
                                route.truck = free_truck
                                free_truck.route = route
                                free_truck.status = TruckStatus.ON_THE_WAY
                                break

                    if truck_to_use and suitable_route:
                        break

            if not truck_to_use or not suitable_route:
                passed.append((delivery_id, "No route was found"))
                continue

            truck_to_use.packages.append(package)
            package.truck = truck_to_use
            package.route = suitable_route
            package.status = PackageStatus.IN_PROGRES
            package.expected_arrival = self._app_data.expected_time(package, suitable_route)

            assigned.append((delivery_id, suitable_route.route_id, truck_to_use.vehicle_id))

        if not assigned:
            if all(reason == "Package not found" for _, reason in passed):
                return "Package not found\n"
            if all(reason == "No route was found" for _, reason in passed):
                return "No route was found\n"

        result_lines = []
        if assigned:
            result_lines.append(f"Assigned {len(assigned)} packages:")
            for delivery_id, route_id, vehicle_id in assigned:
                result_lines.append(f"  #Package ID {delivery_id} > Route ID {route_id} > Truck ID {vehicle_id}")

        if passed:
            result_lines.append(f"Skipped {len(passed)} packages:")
            for delivery_id, reason in passed:
                result_lines.append(f"  #Package ID {delivery_id}: {reason}")

        return "\n".join(result_lines)




