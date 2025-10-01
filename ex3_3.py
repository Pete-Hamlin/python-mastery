import csv

from ex3_1 import Stock


def read_csv_as_instances(filename, cls):
    """
    Read a CSV file into a list of instances
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        # Remove headers
        _ = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records


if __name__ == "__main__":
    portfolio = read_csv_as_instances("Data/portfolio.csv", Stock)
    print(portfolio)
