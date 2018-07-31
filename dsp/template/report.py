import sqlite3
import datetime
import init_db


class QueryTemplate:
    def __init__(self):
        self.conn = None
        self.query = None
        self.result = None
        self.formatted_result = None

    def connect(self):
        self.conn = sqlite3.connect(database="sales.db")

    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        result = self.conn.execute(self.query)
        self.result = result.fetchall()

    def format_result(self):
        output = []
        for row in self.result:
            row = [str(i) for i in row]
            csv_line = ", ".join(row)
            output.append(csv_line)
        self.formatted_result = "\n".join(output)

    def output_result(self):
        raise NotImplementedError()

    def process_format(self):
        """Abstract steps to do our job"""
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_result()
        self.output_result()


class NewVehiclesQuery(QueryTemplate):
    def __init__(self):
        pass

    def construct_query(self):
        self.query = "select * from Sales where new='true'"

    def output_result(self):
        print(self.formatted_result)


class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = "select salesperson, sum(amt) from Sales group by salesperson"

    def output_result(self):
        filename = "gross_sales_{0}".format(
            datetime.date.today().strftime("%Y%m%m")
        )
        with open(filename, 'w') as file:
            file.write(self.formatted_result)

def test():
    init_db.initdata()
    a = NewVehiclesQuery()
    a.process_format()

    b = UserGrossQuery()
    b.process_format()


if __name__ == '__main__':
    test()