from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

# app_data = ApplicationData()
# cmd_factory = CommandFactory(app_data)
# engine = Engine(cmd_factory)
#
# engine.start()

def main():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)
    while True:
        print("Logistics App Main Menu")
        print("1. Packages")
        print("2. Routes")
        print("3. Trucks")
        print("0. Exit")

        choice = input("Please, select an option:").strip()

        if choice == "1":
            menu_packages(cmd_factory)
        elif choice == "2":
            menu_routes(cmd_factory)
        elif choice == "3":
            menu_trucks(cmd_factory)
        elif choice == "0":
            print("See ya")
            break
        else:
            print("Invalid option!")

def menu_packages(cmd_factory):
    while True:
        print("Logistics App Package Menu")
        print("1. Create Package")
        print("2. Find Package")
        print("3. Remove Package")
        print("4. Assign Package")
        print("5  Choose Route For Package")
        print("6. View All Packages")
        print("0  Back To Main Menu")

        choice = input("Please, select an option:").strip()
        cmd = None

        if choice == "0":
            break
        elif choice == "1":
            info = input("Enter package info (start_loc, end_loc, weight, contact_info): ").strip()
            cmd = cmd_factory.create(f"createpackage {info}")
        elif choice == "2":
            package_id = input("Enter package ID: ").strip()
            cmd = cmd_factory.create(f"findpackage {package_id}")
        elif choice == "3":
            package_id = input("Enter package ID to remove: ").strip()
            cmd = cmd_factory.create(f"removepackage {package_id}")
        elif choice == "4":
            package_ids = input("Enter package IDs to assign (space-separated): ").strip()
            cmd = cmd_factory.create(f"assigneepackages {package_ids}")
        elif choice == "5":
            package_id = input("Enter package ID to choose route: ").strip()
            cmd = cmd_factory.create(f"routeforpackage {package_id}")
        elif choice == "6":
            cmd = cmd_factory.create("viewpackage")
        else:
            print("Invalid option!")
            continue

        if cmd:
            print(cmd.execute())


def menu_routes(cmd_factory):
    while True:
        print("\n--- Routes Menu ---")
        print("1. Create Route")
        print("2. Find Route")
        print("3. Remove Route")
        print("4. View All Routes")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").strip()
        cmd = None

        if choice == "0":
            break
        elif choice == "1":
            info = input("Enter route info (start_loc, stops, end_loc): ").strip()
            cmd = cmd_factory.create(f"createroute {info}")
        elif choice == "2":
            route_id = input("Enter route ID: ").strip()
            cmd = cmd_factory.create(f"findroute {route_id}")
        elif choice == "3":
            route_id = input("Enter route ID to remove: ").strip()
            cmd = cmd_factory.create(f"removeroute {route_id}")
        elif choice == "4":
            cmd = cmd_factory.create("viewroute")
        else:
            print("Invalid option!")
            continue

        if cmd:
            print(cmd.execute())

def menu_trucks(cmd_factory):
    while True:
        print("\n--- Trucks Menu ---")
        print("1. View All Trucks")
        print("2. View Free Trucks in City")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").strip()
        cmd = None

        if choice == "0":
            break
        elif choice == "1":
            cmd = cmd_factory.create("viewtruck")
        elif choice == "2":
            city = input("Enter city code: ").strip()
            cmd = cmd_factory.create(f"viewfreetruck {city}")
        else:
            print("Invalid option!")
            continue

        if cmd:
            print(cmd.execute())

if __name__ == "__main__":
    main()