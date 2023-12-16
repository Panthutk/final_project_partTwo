# database.py
class DatabaseManager:
    def __init__(self):
        # Initialize an empty list to store tables
    def read_csv(self, filename):
        """
        Read data from a CSV file and convert it into a list of dictionaries.
        Each dictionary represents a row in the CSV file.
        """

    def insert_table(self, table_name, filename):
        """
        Create a new table and insert it into the database.
        The table is initialized with data from a CSV file.
        """

    def search_table(self, table_name):
        """
        Search for a table in the database by name.
        Return the table if found, otherwise return None.
        """

class Table:
    def __init__(self, table_name, table):
        """
        Initialize a table with a name and data (list of dictionaries).
        """

    def insert_entry(self, entry):
        """
        Insert a new entry (dictionary) into the table.
        """

    def update_entry(self, key, new_value):
        """
        Update an entry in the table based on a specified key.
        """

    def add_column(self, column_name, default_value):
        """
        Add a new column to the table if it doesn't already exist.
        """
    def save_table(self,new_table):
        """
        Save the modify table to it csv
        """
# project_manage.py
from database import DatabaseManager, Table

* Create a DatabaseManager instance
db_manager = DatabaseManager()

* Initialize function to create tables and add columns
def initializing():
    # Insert a 'persons' table into the database
    # Insert a 'login' table into the database
    # Add columns to the 'persons' table if they don't exist
    return persons_table, login_table

* Initialize tables
persons_table, login_table = initializing()

* Login function
def login():
    # login by using input person_id and password with login_table username and password
    then return person_id and that cut last 2 character to used it other function and it role in login_table


* Exit function
def exit_program():
    # Implement a save_table method in the Table class to save tables to CSV files.
    persons_table.save_table('persons.csv')
    login_table.save_table('login.csv')

    print("Exiting...")


* Make calls to the login function
person_id, role = login()

* Based on the return value for login, activate the code that performs activities according to the role defined for that person_id
  they can do the following command
* An admin
    Managing the database
    Can update all the tables there

* A student
    See an invitational message from the lead
    Accept or deny the invitation
    See and modify his project details

* A lead student
    Create a project
    Find members
    Send invitational messages to potential members
    Add members to the project and form a group
    See and modify his own project details
    Send request messages to potential advisors
    Submit the final project report

* A member student
    See and modify his project details

* A normal faculty who is not an advisor
    See request to be a supervisor
    Send response denying to serve as an advisor
    See details of all the project
    Evaluate projects (this is the missing step that you will explain in your proposal; see details in the tasks below)

* A advising faculty
    See request to be a supervisor
    Send accept response (for projects eventually serving as an advisor)
    Send deny response (for projects not eventually serving as an advisor)
    See details of all the project
    Evaluate projects (this is the missing step that you will explain in your proposal; see details in the tasks below)
    Approve the project

* Calling Exit method to exit and save all the work to csv