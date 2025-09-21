from models.delivery_route import DeliveryRoute
from models.delivery_package import DeliveryPackage
from models.trucks import Trucks
from models.country_map import truck
from datetime import datetime
from models.users import User

class ApplicationData:
    def __init__(self):
        self._routs: list[DeliveryRoute] = []
        self._packages: list[DeliveryPackage] = []
        self._trucks: list[Trucks] = truck
        self._users: list[User] = []
        self._logged_user = None

    @property
    def routs(self):
        return tuple(self._routs)

    @property
    def package(self):
        return tuple(self._packages)

    @property
    def trucks(self):
        return tuple(self._trucks)

    @property
    def users(self):
        return tuple(self._users)

    @staticmethod
    def expected_time(package, route):
        arrival_time = route.arrival_time()
        for city, arrival in arrival_time:
            if city == package.end_location:
               package.expected_arrival = arrival
               return arrival
        package.expected_arrival = None
        return None

    def create_route(self, location: list[str], departure_time: datetime):
        route = DeliveryRoute(location, departure_time)
        self._routs.append(route)
        return route

    def create_package(self, start_location, end_location, weight, contact_info):
        package = DeliveryPackage(start_location, end_location, weight, contact_info)
        self._packages.append(package)
        return package

    def login(self, login):
        user = User(login)
        self._users.append(user)
        self._logged_user = user
        return user

    @property
    def logged_in_user(self):
        if self.has_logged_in_user:
            return self._logged_user
        else:
            raise ValueError('There is no logged in user.')

    @property
    def has_logged_in_user(self):
        return self._logged_user is not None

    def logout(self):
        self._logged_user = None

    def remove_route(self, route_id):
        route = self.find_route(route_id)
        if route:
            self._routs.remove(route)

    def remove_package(self, delivery_id):
        package = self.find_package(delivery_id)
        if package:
            self._packages.remove(package)

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
