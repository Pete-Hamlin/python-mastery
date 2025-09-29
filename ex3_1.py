import csv


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount: int):
        self.shares -= amount


def read_portfolio(csv_file) -> tuple[list, list]:
    portfolio = []
    with open(csv_file) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            portfolio.append(Stock(row[0], int(row[1]), float(row[2])))
    return headers, portfolio


def print_portfolio(headers: list[str], rows: list[Stock]):
    print("%10s %10s %10s" % (headers[0], headers[1], headers[2]))
    print(("-" * 10 + " ") * len(headers))
    for s in rows:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))


if __name__ == "__main__":
    headers, portfolio = read_portfolio("Data/portfolio.csv")
    print_portfolio(headers, portfolio)
