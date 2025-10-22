from decimal import Decimal

from util import Stock


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
