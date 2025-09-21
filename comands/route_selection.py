from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from models.truck_status import TruckStatus
from models.package_status import PackageStatus

class PackageForRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):

        if len(self._params) < 1:
            raise ValueError("Please, enter the provided ID for package")
        if len(self._params) > 1:
            raise ValueError("You can use one ID for this command")

        delivery_id = int(self._params[0])
        package = self.app_data.find_package(delivery_id)

        if package is None:
            return f"Package with ID {delivery_id} not found"

        if package.truck is not None:
            return f"Package with ID {delivery_id} already assigned to route"

        available_routes = []
        for route in self._app_data.routs:
            route.distance = route.calculate_km()

            if package.start_location in route.location and package.end_location in route.location:
                start_index = route.location.index(package.start_location)
                end_index = route.location.index(package.end_location)

                if start_index < end_index:
                    start_city = route.location[0]

                    if route.truck:
                        truck = route.truck
                        current_cap = sum(p.weight for p in truck.packages)

                        conditions = [
                            truck.status == TruckStatus.ON_THE_WAY,
                            current_cap + package.weight <= truck.capacity,
                            route.distance <= truck.max_range]

                        if all(conditions):
                            expected_arrival = self.app_data.expected_time(package, route)
                            available_routes.append((route, expected_arrival))

                    else:
                        free_trucks = [
                            t for t in self.app_data.trucks
                            if t.current_loc == start_city and t.status == TruckStatus.FREE]

                        for truck in free_trucks:
                            current_cap = sum(p.weight for p in truck.packages)

                            conditions = [
                                current_cap + package.weight <= truck.capacity,
                                route.distance <= truck.max_range]

                            if all(conditions):
                                expected_arrival = self.app_data.expected_time(package, route)
                                route.truck = truck
                                truck.status = TruckStatus.ON_THE_WAY
                                available_routes.append((route, expected_arrival))
                                break

        if not available_routes:
            return f"No routes found for Package ID {delivery_id}"

        print(f"Routes for Package ID {delivery_id}: {package.start_location} to {package.end_location}")
        i = 1
        for route, arrival in available_routes:
            path = " > ".join(route.location)
            print(f"{i}. Route ID: {route.route_id} / {path} / Arrival to {package.end_location}: {arrival}")
            i += 1

        choice = input("Select route number to assign package: ")
        selected_index = int(choice.strip()) - 1
        selected_route, arrival = available_routes[selected_index]

        truck = selected_route.truck
        current_cap = sum(p.weight for p in truck.packages)

        if current_cap + package.weight > truck.capacity:
            return f"Cannot assign Package ID {delivery_id}: truck {truck.truck_id} is overloaded."

        truck.packages.append(package)
        package.truck = truck
        package.route = selected_route
        package.expected_arrival = arrival
        package.status = PackageStatus.IN_PROGRES

        return f"Package ID {delivery_id} successfully assigned to Route ID {selected_route.route_id}"

