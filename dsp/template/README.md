# Template pattern

The template pattern is useful for removing duplicate code; it's an implementation
to support the Don't Repeat Yourself principle

It is designed for situations where we have several different tasks to accomplish that have some, but not all, steps in common.
The common steps are implemented in a base class, and the distinct steps are overridden
in subclasses to provide custom behavior.

In some ways, it's like a generalized
strategy pattern, except similar sections of the algorithms are shared using a base class.

# Problem to solve
A car sales reporter

We have two common tasks we need to perform:

• Select all sales of new vehicles and output them to the screen in a
comma-delimited format

• Output a comma-delimited list of all salespeople with their gross sales
and save it to a file that can be imported to a spreadsheet

These seem like quite different tasks, but they have some common features. In both
cases, we need to perform the following steps:
1. Connect to the database.
2. Construct a query for new vehicles or gross sales.
3. Issue the query.
4. Format the results into a comma-delimited string.
5. Output the data to a file or e-mail.

The query construction and output steps are different for the two tasks, but the
remaining steps are identical. We can use the template pattern to put the common
steps in a base class, and the varying steps in two subclasses.

Each step gets its own method (to make it easy to selectively override any one step)

# Implementation

```python
class QueryTemplate:
    def connect(self):
        pass

    def construct_query(self):
        pass

    def do_query(self):
        pass

    def format_result(self):
        pass

    def output_result(self):
        pass

    def process_format(self):
        """Abstract steps to do our job"""
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_result()
        self.output_result()
```
The process_format method is the primary method to be called by an outside
client. It ensures each step is executed in order, but it does not care if that step is
implemented in this class or in a subclass

# Common methods are implemented in base class

```python
import sqlite3


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

```
# Define concrete subclasses extends the varying methods of the Template

```python
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
```