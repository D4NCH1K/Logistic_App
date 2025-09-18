from datetime import datetime, timedelta
from models.country_map import *

class DeliveryRoute:
    route_id = 1
    truck_km = 87
    def __init__(self, location: list[str], departure_time: datetime):
        if len(location) < 2:
            raise ValueError("Route must contain at least two locations.")

        self.route_id = DeliveryRoute.route_id
        DeliveryRoute.route_id += 1

        self.location = location
        self.start_location = location[0]
        self.end_location = location[-1]
        self.departure_time = departure_time or datetime.now()
        self.truck = []

    def calculate_km(self):
        total = 0
        for x in range(len(self.location) - 1):
            a = self.location[x]
            b = self.location[x + 1]
            total += country_routes[a][b]
        return total

    def arrival_time(self):
        curr = self.departure_time
        arrival_time = []
        for x in range(len(self.location) - 1):
            a = self.location[x]
            b = self.location[x + 1]
            dist = country_routes[a][b]
            total_hours = dist / DeliveryRoute.truck_km
            curr += timedelta(hours = total_hours)
            arr_t = curr.strftime('%b %dth, %H:%M, %Y')
            arrival_time.append((b, arr_t))
        return arrival_time

    def info(self):
        arrival_lines = []
        for location, time in self.arrival_time():
            arrival_lines.append(f"Arrival in {location}: {time}")

        arrival_text = "\n".join(arrival_lines)

        return (
            f"Route ID: {self.route_id}\n"
            f"Departure from: {self.start_location} to {self.end_location} at {self.departure_time.strftime('%b %dth, %H:%M, %Y')}\n"
            f"{arrival_text}\n"
            f"Total distance: {self.calculate_km()}km"
        )