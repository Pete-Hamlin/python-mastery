import csv
from collections.abc import Sequence
from sys import intern


def read_csv_as_dicts(file: str, types: list):
    with open(file) as f:
        rows = csv.reader(f)
        headers = next(rows)
        return [
            {name: func(val) for name, func, val in zip(headers, types, row)}
            for row in rows
        ]


def read_csv_as_cols(file: str, types: list):
    with open(file) as f:
        rows = csv.reader(f)
        headers = next(rows)
        collection = DataCollection(headers, types)
        for row in rows:
            collection.append({name: val for name, val in zip(headers, row)})
        return collection


class DataCollection(Sequence):
    def __init__(self, headers, types):
        # Each value is a list with all of the values (a column)
        self.headers = headers
        self.types = types
        for col in headers:
            setattr(self, col, [])

    def __len__(self):
        # All lists assumed to have the same length
        # Grab the first column
        return len(getattr(self, self.headers[0]))

    def __getitem__(self, index):
        if isinstance(index, slice):
            slice_data = DataCollection(self.headers, self.types)
            indices = range(*index.indices(len(self)))
            for i in indices:
                slice_data.append(
                    {name: getattr(self, name)[i] for name in self.headers}
                )
            return slice_data
        return {name: getattr(self, name)[index] for name in self.headers}

    def append(self, d):
        for col, func in zip(self.headers, self.types):
            getattr(self, col).append(func(d[col]))


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    for method in [read_csv_as_dicts, read_csv_as_cols]:
        tracemalloc.clear_traces()
        print(f"__{method.__name__}__")
        port = method("Data/portfolio.csv", [str, int, float])
        print(len(port))
        print(port[0])
        print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())

        tracemalloc.clear_traces()
        buses = method("Data/ctabus.csv", [str, str, str, int])
        print(len(buses))
        print(buses[0:10])
        print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())

        tracemalloc.clear_traces()
        buses = method("Data/ctabus.csv", [intern, str, str, int])
        print(len(buses))
        print(buses[0:10])
        print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())

        tracemalloc.clear_traces()
        buses = method("Data/ctabus.csv", [intern, intern, str, int])
        print(len(buses))
        print(len(buses[0:10]))
        print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
