import csv


class DatabaseManager:
    def __init__(self):
        self.database = []

    def read_csv(self, filename):
        data = []
        with open(filename, 'r') as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return data

    def insert_table(self, table_name, filename):
        table_data = self.read_csv(filename)
        table = Table(table_name, table_data)
        self.database.append(table)
        return table

    def search_table(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def insert_entry(self, entry):
        self.table.append(entry)

    def update_entry(self, key, new_value):
        for entry in self.table:
            if key in entry:
                entry[key] = new_value
                break

    def add_column(self, column_name, default_value):
        # Check if the column_name already exists in any entry of the table
        if not any(column_name in entry for entry in self.table):
            # If not, add the new column to all entries
            for entry in self.table:
                entry[column_name] = default_value
