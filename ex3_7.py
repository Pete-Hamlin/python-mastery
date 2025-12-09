from ex3_5 import TableFormatter, print_table
from util import read_portfolio


class MyFormatter(TableFormatter):
    def headers(self, headers):
        pass

    def row(self, rowdata):
        pass


if __name__ == "__main__":
    _, portfolio = read_portfolio("Data/portfolio.csv")
    print_table(["name", "shares", "price"], portfolio, MyFormatter())
