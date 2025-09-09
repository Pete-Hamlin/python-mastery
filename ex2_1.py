# readrides.py

import csv
from collections import namedtuple


# A class
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


# A named tuple
NamedRow = namedtuple("Row", ["route", "date", "daytype", "rides"])


# A class with __slots__
class SlotsRow:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides(filename, method):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = method(route, date, daytype, rides)
            records.append(record)
    return records


def as_tuples(route, date, daytype, rides):
    return (route, date, daytype, rides)


def as_dicts(route, date, daytype, rides):
    return {
        "route": route,
        "date": date,
        "daytype": daytype,
        "rides": rides,
    }


def as_class(route, date, daytype, rides):
    return Row(route, date, daytype, rides)


def as_named_tuple(route, date, daytype, rides):
    return NamedRow(route, date, daytype, rides)


def as_slots(route, date, daytype, rides):
    return SlotsRow(route, date, daytype, rides)


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    for method in [as_tuples, as_dicts, as_class, as_named_tuple, as_slots]:
        tracemalloc.clear_traces()
        rows = read_rides("Data/ctabus.csv", method)
        print("%s" % method.__name__)
        print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
