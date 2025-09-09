from collections import Counter

from ex2_1 import as_dicts, read_rides


def count_routes(data: list):
    """Part 1: Count how many bus routes exist in Chicago.

    Args:
        data: data object to parse (bus routes CSV)
    """
    routes = {route["route"] for route in data}
    print(f"Found {len(routes)} routes in Chicago")


def route_head_count(data: list, route: str, date_str: str):
    """Part 2: Count number of riders on a given date for a given route.

    Args:
        data: data object to parse (bus routes CSV)
        date_str: Given route, provided as a string
        date_str: Date, in the format mm/dd/yyyy
    """
    rides = next(
        r["rides"] for r in data if (r["route"] == route and r["date"] == date_str)
    )
    print(f"{rides} rides for route {route} on {date_str}")


def total_rides(data: list):
    """Part 3: Count total rides taken on each route

    Args:
        data: data object to parse (bus routes CSV)
    """
    rides = Counter()
    for i in data:
        rides[i["route"]] += i["rides"]
    for key, value in rides.items():
        print(f"Route {key} has {value} total rides")


def _single_year_total(data: list, year: str):
    ride_count = Counter()
    rides = [ride for ride in data if ride["date"].endswith(year)]
    for i in rides:
        ride_count[i["route"]] += i["rides"]
    return ride_count


def max_increase(data: list):
    """Part 4: Find top 5 routes with greatest usage increase between 2001-2011

    Args:
        data: data object to parse (bus routes CSV)
    """
    rides_01 = _single_year_total(data, "2001")
    rides_11 = _single_year_total(data, "2011")
    ride_diff = Counter()
    for key, value in rides_01.items():
        ride_diff[key] = rides_11[key] - value
    for route, count in ride_diff.most_common(5):
        print(f"Route {route} has growth of {count}")


if __name__ == "__main__":
    data = read_rides("Data/ctabus.csv", as_dicts)
    print(data[0])
    count_routes(data)
    route_head_count(data, "22", "02/02/2011")
    total_rides(data)
    max_increase(data)
