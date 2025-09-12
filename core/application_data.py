from models.delivery_route import DeliveryRoute
from models.delivery_package import DeliveryPackage
#from models.package_status import PackageStatus
from models.trucks import Trucks
from models.country_map import truck
from models.truck_status import TruckStatus
from datetime import datetime

class ApplicationData:
    def __init__(self):
        self._routs: list[DeliveryRoute] = []
        self._packages: list[DeliveryPackage] = []
        self._trucks: list[Trucks] = truck

    @property
    def routs(self):
        return tuple(self._routs)

    @property
    def package(self):
        return tuple(self._packages)

    @property
    def trucks(self):
        return tuple(self._trucks)

    @staticmethod
    def expected_time(package, route):
        arrival_time = route.arrival_time()
        for city, arrival in arrival_time:
            if city == package.end_location:
                package.expected_arrival = arrival
                break

    @staticmethod
    def best_route_for_package(start, end):
        pass

    def create_route(self, location: list[str], departure_time: datetime):
        route = DeliveryRoute(location, departure_time)
        self._routs.append(route)

        for t in self._trucks:
            if t.status == TruckStatus.FREE:
                t.route = route
                t.status = TruckStatus.ON_THE_WAY
                route.truck = t
                break
        return route

    def create_package(self, start_location, end_location, weight, contact_info):
        package = DeliveryPackage(start_location, end_location, weight, contact_info)
        self._packages.append(package)

        for route in self._routs:
            if start_location in route.location and end_location in route.location:
                t = route.truck
                t_cap = sum(p.weight for p in t.packages)
                dist = route.calculate_km()
                if t_cap + weight <= t.capacity and dist <= t.max_range:
                    t.packages.append(package)
                    package.truck = t
                    self.expected_time(package, route)
                    break
        return package

    def remove_route(self, route_id):
        route = self.find_route(route_id)
        if route:
            self._routs.remove(route)

    def remove_package(self, delivery_id):
        self._packages.remove(delivery_id)

    def find_route(self, route_id: int):
        for route in self._routs:
            if route.route_id == route_id:
                return route
        return None

    def find_package(self, delivery_id: int):
        for package in self._packages:
            if package.delivery_id == delivery_id:
                return package
        return None

    def view_routes(self):
        return [route.info() for route in self._routs]

    def view_package(self):
        return [package.info() for package in self._packages]

    def view_trucks(self):
        return [t.info() for t in self._trucks]
