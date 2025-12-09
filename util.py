import csv
from abc import ABC, abstractmethod


def read_portfolio(csv_file):
    portfolio = []
    with open(csv_file) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            portfolio.append(Stock(row[0], int(row[1]), float(row[2])))
    return headers, portfolio


class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row) -> None:
        pass


class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row) -> dict:
        return {name: func(val) for name, func, val in zip(headers, self.types, row)}


class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)


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
