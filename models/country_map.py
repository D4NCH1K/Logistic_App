from models.trucks import Trucks

country_routes = {
    "SYD": {"MEL": 877, "ADL": 1376, "ASP": 2762, "BRI": 909, "DAR": 3935, "PER": 4016},
    "MEL": {"SYD": 877, "ADL": 725, "ASP": 2255, "BRI": 1765, "DAR": 3752, "PER": 3509},
    "ADL": {"SYD": 1376, "MEL": 725, "ASP": 1530, "BRI": 1927, "DAR": 3027, "PER": 2785},
    "ASP": {"SYD": 2762, "MEL": 2255, "ADL": 1530, "BRI": 2993, "DAR": 1497, "PER": 2481},
    "BRI": {"SYD": 909, "MEL": 1765, "ADL": 1927, "ASP": 2993, "DAR": 3426, "PER": 4311},
    "DAR": {"SYD": 3935, "MEL": 3752, "ADL": 3027, "ASP": 1497, "BRI": 3426, "PER": 4025},
    "PER": {"SYD": 4016, "MEL": 3509, "ADL": 2785, "ASP": 2481, "BRI": 4311, "DAR": 4025},
}

cities = ["SYD", "MEL", "ADL", "ASP", "BRI", "DAR", "PER"]

truck = [
    *[Trucks(i, "Scania", 42000, 8000) for i in range(1001, 1011)],
    *[Trucks(i, "MAN", 37000, 10000) for i in range(1011, 1026)],
    *[Trucks(i, "Actros", 26000, 13000) for i in range(1026, 1041)],
]

truck_to_city = {
    "SYD":truck[0:1] + truck[10:14] + truck[25:27],
    "MEL":truck[1:3] + truck[14:16] + truck[27:29],
    "ADL":truck[3:4] + truck[16:19] + truck[29:33],
    "ASP":truck[4:5] + truck[19:21] + truck[33:36],
    "BRI":truck[5:7] + truck[21:22] + truck[36:38],
    "DAR":truck[7:8] + truck[22:24] + truck[38:39],
    "PER":truck[8:10] + truck[24:25] + truck[39:40],
}

for city, trucks_list in truck_to_city.items():
    for t in trucks_list:
        t.current_loc = city
