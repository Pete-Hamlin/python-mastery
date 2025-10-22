import sys

from ex3_3 import read_csv_as_instances
from ex3_5 import create_formatter, print_table
from util import Stock


class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
        self.out_file.close()


if __name__ == "__main__":
    goog = Stock("GOOG", 100, 490.10)
    repr(goog)

    portfolio = read_csv_as_instances("Data/portfolio.csv", Stock)
    print(portfolio)

    formatter = create_formatter("text")
    with redirect_stdout(open("out.txt", "w")) as file:
        print_table(["name", "shares", "price"], portfolio, formatter)
