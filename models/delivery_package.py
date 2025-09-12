from models.package_status import PackageStatus
from datetime import datetime, timedelta

class DeliveryPackage:

    delivery_id = 1
    def __init__(self, start_location: str, end_location: str, weight: float, contact_info: str):

        self.delivery_id = DeliveryPackage.delivery_id
        DeliveryPackage.delivery_id += 1

        self.start_location = start_location
        self.end_location = end_location
        self._weight = weight
        self.contact_info = contact_info
        self.truck = None
        self.expected_arrival = None
        self.status = PackageStatus.TODO

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("")
        self._weight = value

    def info(self):
        return (
            f"Package ID: {self.delivery_id}\n"
            f"Truck ID: {self.truck.truck_id if self.truck else 'Not assigned'}\n"
            f"From: {self.start_location} to {self.end_location}\n"
            f"Weight: {self.weight}\n"
            f"Contact: {self.contact_info}\n"
            f"Status: {self.status}\n"
            f"Expected Arrival: {self.expected_arrival if self.expected_arrival else 'Not assigned'}\n"
        )

