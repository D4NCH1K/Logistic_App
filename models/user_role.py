class UserRole:
    Employee = "Employee"
    Manager = "Manager"
    Supervisor = "Supervisor"

    @classmethod
    def from_string(cls, status_string):
        if status_string not in [cls.Employee, cls.Manager, cls.Supervisor]:
            raise ValueError(f"Wrong role {status_string}")
        return status_string

    @classmethod
    def username(cls, name: str):
        if name == "Daniil":
            return cls.Employee
        elif name == "Zdravko":
            return cls.Manager
        elif name == "Dragomir":
            return cls.Supervisor
        else:
            raise ValueError(f"You are not part of employee of the company {name}!")
