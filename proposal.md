# DMSP(Data Management System Proposal)
## Execute Summary
This is proposal design from the basic DMSP in python that we sturdy in class with Aj.Paruj . The system will provide user basic solution for
managing data through CSV files. The DMSP include basic functions such as reading data from CSV files, inserting tables,searching for tables 
inserting entires to table,update entire table ,adding columns to table and saving tables back to CSV files.

## Objective
This is the main objective for this DMSP:
1. `Efficient management` The efficient management of data through CSV files.
2. `Flexibility` Allow users to dynamically insert tables, search for tables, insert entries, update entries, add columns, and save tables.
3. `Ease of used` User-friendly system for basic python user

## Functionalities
1. `Reading CSV files` The read_csv method in the *DatabaseManager* class reads data from a specified CSV file and returns it as a list of dictionaries.
2. `Inserting table` The `insert_table method `in the `DatabaseManager` class inserts a new table into the system by reading data from a CSV file and creating a corresponding Table object.
3. `3. Searching for Tables` The *search_table* method in the *DatabaseManager* class searches for a table by name and returns the corresponding Table object.
4. `Insert Entire Tables` The *insert_entry* method in the Table class adds a new entry to the table.
5. `Updating Entries`
The *update_entry* method in the Table class updates a specific entry in the table based on a key-value pair.
6. `Adding Columns`
The *add_column* method in the Table class adds a new column to the table if it does not already exist.
7. `Saving Tables`
The *save_table* method in the Table class saves the table back to a CSV file.

---

# Project Management System Proposal
The following Python script, `project_manage.py`, implements a basic project management system. It import from a database module (`database.py`) that provides functionality for managing tables and entries. as `bd_manager`


## Initializing
1. `Inserting table` read and insert table to `db_manager`
    * persons_table = persons.csv
    * login_table = login.csv
2. `Check the persons.csv` if it have all the column that the system need to used it not it will add automatically by call `add_column` functions then return as `person_table` and *login_table*

## Login
`login()` is method used for login and used data from login.csv if the user and password match in login_table username and password it will return `person_id and role` but it will remove last two character from person_id for further used in other function . Else it will Invalid and need to repeat again

## Exiting program
`exit_program()` is function that is the last thing that will call in this program this method used for exit while loop and save the csv by calling `save_table()` that from DMSP

## Functionalities for Different Roles
* Admin:
    * View all projects
    * View all students
    * Update a table
    * Exit
* Lead:
    * Create project
    * View project
    * Modify project
    * Send request to advisor
    * Exit
* Student:
    * See invitation from leader
    * Accept or deny invitation
    * Become leader of a project
    * Exit
* Faculty:
    * View all requests
    * Add message or approve the project
    * Exit

# Conclusion
The Project Management System aims to streamline project-related tasks, providing a user-friendly interface for efficient data management. With functionalities tailored to different roles, the system enhances collaboration and communication within the project management workflow.