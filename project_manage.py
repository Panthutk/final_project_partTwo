# import database module

from database import Table, DB
import csv
import os

# define a function called initializing
my_db = DB()


def initializing():
    # create a 'persons' table
    persons_table = Table('persons', 'persons.csv')

    if "project" not in persons_table.table:
        persons_table.add_column("project", [])
    if "detail" not in persons_table.table:
        persons_table.add_column("detail", [])
    if "member1" not in persons_table.table:
        persons_table.add_column("member1", [])
    if "member2" not in persons_table.table:
        persons_table.add_column("member2", [])
    if "advisor" not in persons_table.table:
        persons_table.add_column("advisor", [])
    if "status1" not in persons_table.table:
        persons_table.add_column("status1", [])
    if "status2" not in persons_table.table:
        persons_table.add_column("status2", [])
    if "submit" not in persons_table.table:
        persons_table.add_column("submit", [])

    # add the 'persons' table into the database
    my_db.insert(persons_table)

    # create a 'login table' table
    login_table = Table('login', 'login.csv')

    # add the login table into the database
    my_db.insert(login_table)

    return persons_table, login_table


# define a function called login
def login():
    access = False
    while not access:
        person_id = input("Enter your username: ")
        password = input("Enter your password: ")
        if person_id and password != " " or "":
            for i in range(len(login_table.table)):
                if login_table.table[i]['username'] == person_id and login_table.table[i]['password'] == password:
                    access = True
                    print("Login successful!")
                    person_id = person_id[:-2]
                    return person_id, login_table.table[i]['role']
        elif person_id == 'exit' or password == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid username or password. Please try again.")


# define a function called exit
def exit():
    pass


# make calls to the initializing and login functions defined above
persons_table, login_table = initializing()
print(login_table.table)
person_id, role = login()
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id
process = False
if role == 'admin':
    # see and do admin related activities
    while not process:
        print("Welcome to the admin menu!")
        print("1. View all projects")
        print("2. View all students")
        print("3. update a table")
        print("4. exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print(persons_table.table["project"])
        elif choice == '2':
            temp = []
            for i in persons_table.table["type"] == "student":
                temp.append(persons_table.table[i])
            print(temp)
        elif choice == '3':
            table_name = input("Enter the table name: ")
            key = input("Enter the key: ")
            new_value = input("Enter the new value: ")
            persons_table.update_entry(table_name, key, new_value)
        elif choice == '4':
            process = True
        else:
            print("Invalid choice. Please try again.")


elif role == 'student':
    # see and do student related activities
    print("Welcome to the student menu!")
    print("1. View invitation from lead")
    print("2. Accept or reject invitation")
    print("3. Create project")
    print("4. Exit")

    while not process:
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Invitation from lead:")
            for count in range(len(persons_table.table)):
                if persons_table.table[count]['member1'] == person_id or persons_table.table[count]['member2'] == person_id:
                    print(
                        f"Project name: {persons_table.table[count]['project']} from {persons_table.table[count]['first']}")
        elif choice == "2":
            print("Accept or reject invitation:")
            for count in range(len(persons_table.table)):
                if persons_table.table[count]['member1'] == person_id:
                    print("Accept or Reject?")
                    status_choice = input("Enter your choice: ")
                    if status_choice == "Accept":
                        persons_table.table[count]['status1'] = "accept"
                        persons_table.table[count]['type'] = "member"
                    elif status_choice == "Reject":
                        persons_table.table[count]['status1'] = "reject"
                        persons_table.table[count]['type'] = "student"
                    else:
                        print("Invalid choice. Please try again.")
                elif persons_table.table[count]['member2'] == person_id:
                    print(
                        f"Project name: {persons_table.table[count]['project']} from {persons_table.table[count]['lead']}")
                    print("Accept or Reject?")
                    status_choice = input("Enter your choice: ")
                    if status_choice == "Accept":
                        persons_table.table[count]['status2'] = "accept"
                    elif status_choice == "Reject":
                        persons_table.table[count]['status2'] = "reject"
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Creating new project...")
            project_name = input("Enter the project name: ")
            project_detail = input("Enter the project detail: ")
            project_member1 = input("Enter the project member username: ")
            project_member2 = input("Enter the project member username: ")
            for count in range(len(persons_table.table)):
                if persons_table.table[count]["first"] == person_id:
                    persons_table.table[count]['project'] = project_name
                    persons_table.table[count]['detail'] = project_detail
                    persons_table.table[count]['member1'] = project_member1
                    persons_table.table[count]['member2'] = project_member2
                    persons_table.table[count]['status1'] = "pending"
                    persons_table.table[count]['status2'] = "pending"
                    persons_table.table[count]['submit'] = "not submitted"
                    persons_table.table[count]['type'] = "lead"
                    print("Project created!")
                    break
        elif choice == "4":
            process = True
        else:
            print("Invalid choice. Please try again.")

elif role == 'member':
    # see and do member related activities
    pass
elif role == 'lead':
    # see and do lead related activities
    print("Welcome to the lead menu!")
elif role == 'faculty':
    # see and do faculty related activities
    pass
elif role == 'advisor':
    # see and do advisor related activities
    pass

# once everything is done, make a call to the exit function
exit()
