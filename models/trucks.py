from models.truck_status import TruckStatus

class Trucks:
    truck_id = 1
    def __init__(self, vehicle_id: int, name: str, capacity: float, max_range: float):
        self.truck_id = Trucks.truck_id
        Trucks.truck_id += 1

        self.vehicle_id = vehicle_id
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.status = TruckStatus.FREE
        self.current_loc = None
        self.route = None
        self.packages = []

    def work(self):
        if self.status == TruckStatus.FREE:
            self.status= TruckStatus.ON_THE_WAY
            return True
        return False

    def info(self):
        return (
            f"Truck #{self.vehicle_id} - {self.name}\n"
            f"Location: {self.current_loc} | Capacity: {self.capacity:}kg| Max Range: {self.max_range:}km | Status: {self.status}"
        )
