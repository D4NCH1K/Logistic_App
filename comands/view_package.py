from comands.basecomand.base_comand import  BaseCommand
from core.application_data import ApplicationData

class ViewPackage(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if not self.app_data.package:
            return "Package not found"

        package_info = []
        for package in self.app_data.package:
            package_info.append(package.info())
        return "\n".join(package_info)