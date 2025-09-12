class TruckStatus:
    FREE = "FREE"
    ON_THE_WAY = "OnTheWay"

    @classmethod
    def from_string(cls, status_string):
        if status_string not in [cls.FREE, cls.ON_THE_WAY]:
            raise ValueError(f"Wrong status {status_string}")
        return status_string