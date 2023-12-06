# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

persons = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        persons.append(dict(r))
print(persons)

# add in code for a Database class


class DB:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None
# add in code for a Table class


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    # modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary
    def insert_entry(self, entry):
        self.table.append(entry)
    # modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated

    def update_entry(self, key, new_value):
        for entry in self.table:
            if key in entry:
                entry[key] = new_value
                break

    def add_column(self, column_name, default_value):
        for entry in self.table:
            entry[column_name] = default_value
