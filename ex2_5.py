import collections
import csv


def read_rides_as_columns(filename):
    """
    Read the bus ride data as a list of dicts
    """
    records = RideData()  # <--- CHANGE THIS
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {"route": route, "date": date, "daytype": daytype, "rides": rides}
            records.append(record)
    return records


class RideData(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            slice_data = RideData()
            indices = range(*index.indices(len(self)))
            print(indices)
            for i in indices:
                slice_data.append(
                    {
                        "route": self.routes[i],
                        "date": self.dates[i],
                        "daytype": self.daytypes[i],
                        "rides": self.numrides[i],
                    }
                )
            return slice_data
        return {
            "route": self.routes[index],
            "date": self.dates[index],
            "daytype": self.daytypes[index],
            "rides": self.numrides[index],
        }

    def __iter__(self):
        return

    def append(self, d):
        self.routes.append(d["route"])
        self.dates.append(d["date"])
        self.daytypes.append(d["daytype"])
        self.numrides.append(d["rides"])


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rides = read_rides_as_columns("Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
    r = rides[0:10]
