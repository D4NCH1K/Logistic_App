from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData
from models.package_status import PackageStatus

class NotAssignedPackages(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        package_info = []

        for package in self.app_data.package:
            if package.status == PackageStatus.TODO:
                package_info.append(
                    f"Package ID: {package.delivery_id} | From {package.start_location} to {package.end_location}"
                )
        if not package_info:
            return "No unassigned packages found"

        return "\n\n".join(package_info)

