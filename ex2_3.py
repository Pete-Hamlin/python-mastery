import csv
import tracemalloc

from ex2_1 import as_dicts, read_rides


def read_as_dicts():
    tracemalloc.start()
    rows = read_rides("Data/ctabus.csv", as_dicts)
    rt22 = [row for row in rows if row["route"] == "22"]
    print(max(rt22, key=lambda row: row["rides"]))
    tracemalloc.get_traced_memory()


def read_as_iter():
    f = open("Data/ctabus.csv")
    f_csv = csv.reader(f)
    headers = next(f_csv)
    rows = (dict(zip(headers, row)) for row in f_csv)
    rt22 = (row for row in rows if row["route"] == "22")
    print(max(rt22, key=lambda row: int(row["rides"])))
    tracemalloc.get_traced_memory()


if __name__ == "__main__":
    tracemalloc.start()
    for method in [read_as_dicts, read_as_iter]:
        tracemalloc.reset_peak()
        method()
        print("%s" % method.__name__)
        print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
