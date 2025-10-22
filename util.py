import csv


def read_portfolio(csv_file) -> tuple[list, list]:
    portfolio = []
    with open(csv_file) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            portfolio.append(Stock(row[0], int(row[1]), float(row[2])))
    return headers, portfolio


class Stock:
    _types = (str, int, float)
    __slots__ = ["_shares", "_price", "name"]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self._shares}, {self._price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and (
            (self.name, self.shares, self.price) == (other.name, other.shares, other.price)
        )

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Shares must be an {self._types[1].__name__}")
        if value >= 0:
            self._shares = value
        else:
            raise ValueError("shares must be >= 0")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Shares must be a {self._types[2].__name__}")
        if float(value) >= 0.0:
            self._price = value
        else:
            raise ValueError("price must be >= 0.0")

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amount: int):
        self.shares -= amount

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
