from abc import ABC, abstractmethod

from util import read_portfolio


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join("%10s" % h for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        print(" ".join("%10s" % d for d in rowdata))


class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join(h for h in headers))

    def row(self, rowdata):
        print(",".join(str(d) for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>{}</tr>".format(" ".join("<th>%s</th>" % h for h in headers)))

    def row(self, rowdata):
        print("<tr>{}</tr>".format(" ".join("<td>%s</td>" % h for h in rowdata)))


def create_formatter(formatter):
    match formatter:
        case "html":
            return HTMLTableFormatter()
        case "csv":
            return CsvTableFormatter()
        case _:
            return TextTableFormatter()


def print_table(headers: list[str], rows: list[object], formatter: TableFormatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(headers)
    for r in rows:
        rowdata = [getattr(r, header_name) for header_name in headers]
        formatter.row(rowdata)


if __name__ == "__main__":
    headers, portfolio = read_portfolio("Data/portfolio.csv")
    for formatter in [TextTableFormatter(), CsvTableFormatter(), HTMLTableFormatter()]:
        print_table(headers, portfolio, formatter)
        print_table(["shares", "name"], portfolio, formatter)
