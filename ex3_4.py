from decimal import Decimal


class Stock:
    _types = (str, int, float)
    __slots__ = ["_shares", "_price", "name"]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

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


class DStock(Stock):
    _types = (str, int, Decimal)


if __name__ == "__main__":
    s = Stock("GOOG", 100, 490.10)
    print(s.name)
    print(s.shares)
    print(s.cost)
    s.shares = 50
    # Shares
    for i in (-50, "foo", "50"):
        try:
            s.shares = i
            print("Validation failed!")
        except (ValueError, TypeError) as e:
            print(e)
    # Price
    for i in (-50.0, "foo", "50.0", 50):
        try:
            s.price = i
            print("Validation failed!")
        except (ValueError, TypeError) as e:
            print(e)
    try:
        s.foo = "bar"
        print(s.foo)
    except AttributeError as e:
        print(e)
    d = DStock("GOOG", 100, Decimal("490.10"))
    try:
        d.price = 92.3
    except TypeError as e:
        print(e)
