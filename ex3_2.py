from ex3_1 import read_portfolio


def print_table(headers: list[str], rows: list[object]):
    print(*("%10s" % (header) for header in headers))
    print(("-" * 10 + " ") * len(headers))
    for row in rows:
        print(*("%10s" % (getattr(row, header)) for header in headers))


if __name__ == "__main__":
    headers, portfolio = read_portfolio("Data/portfolio.csv")
    print_table(headers, portfolio)
    print_table(["shares", "name"], portfolio)
