from ex3_5 import CsvTableFormatter, HTMLTableFormatter, TextTableFormatter, print_table
from util import read_portfolio


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ["%s", "%d", "%0.2f"]


def create_formatter(formatter):
    match formatter:
        case "html":
            return HTMLTableFormatter()
        case "csv":
            return CsvTableFormatter()
        case _:
            return TextTableFormatter()


if __name__ == "__main__":
    headers, portfolio = read_portfolio("Data/portfolio.csv")
    formatter = PortfolioFormatter()
    print_table(["name", "shares", "price"], portfolio, formatter)
