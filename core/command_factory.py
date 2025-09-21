from core.application_data import ApplicationData
from comands.create_route import CreateRoute
from comands.find_route import FindRoute
from comands.remove_route import RemoveRoute
from comands.view_route import ViewRoute
from comands.create_package import CreatePackage
from comands.find_package import FindPackage
from comands.remove_package import RemovePackage
from comands.view_package import ViewPackage
from comands.view_truck import ViewTruck
from comands.route_selection import PackageForRoute
from comands.view_free_truck import ViewFreeTruck
from comands.assignee_packages import AssigneePackages
from comands.complete_all_packages import CompleteAllPackages
from comands.login_user import LoginUser
from comands.logout_user import LogoutUser
from comands.not_assigned_package import NotAssignedPackages
from comands.view_package_id import ViewPackageID
from comands.view_route_in_progress import ViewRouteInProgress
from models.user_role import UserRole

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()
        role = self._app_data.logged_in_user.user_role if self._app_data.has_logged_in_user else None

        if cmd.lower() == "createroute":
            return CreateRoute(params, self._app_data)

        if cmd.lower() == "createpackage":
            return CreatePackage(params, self._app_data)

        if cmd.lower() == "login":
            return LoginUser(params, self._app_data)

        if cmd.lower() == "logout":
            return LogoutUser(params, self._app_data)

        if cmd.lower() == "findroute":
            return FindRoute(params, self._app_data)

        if cmd.lower() == "findpackage":
            return FindPackage(params, self._app_data)

        if cmd.lower() == "removeroute":
            return RemoveRoute(params, self._app_data)

        if cmd.lower() == "removepackage":
            return RemovePackage(params, self._app_data)

        if cmd.lower() == "routeforpackage":
            return PackageForRoute(params, self._app_data)

        if cmd.lower() == "viewfreetruck":
            return ViewFreeTruck(params, self._app_data)

        if cmd.lower() == "viewroute":
            return ViewRoute(params, self._app_data)

        if cmd.lower() == "viewrouteinprogress":
            if role != UserRole.Manager:
                raise ValueError("This command allowed only for manager!")
            return ViewRouteInProgress(params, self._app_data)

        if cmd.lower() == "viewpackage":
            return ViewPackage(params, self._app_data)

        if cmd.lower() == "viewpackageid":
            if role != UserRole.Employee:
                raise ValueError("This command allowed only for employee!")
            return ViewPackageID(params, self._app_data)

        if cmd.lower() == "viewtruck":
            return ViewTruck(params, self._app_data)

        if cmd.lower() == "assigneepackages":
            return AssigneePackages(params, self._app_data)

        if cmd.lower() == "finishpackage":
            return CompleteAllPackages(params, self._app_data)

        if cmd.lower() == "notassignedpackage":
            if role != UserRole.Supervisor:
                raise ValueError("This command allowed only for supervisor!")
            return NotAssignedPackages(params, self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')