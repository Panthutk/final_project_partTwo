# import database module
import database as db
import csv
import os

# define a function called initializing
my_db = db.DB()


def initializing():
    # create a 'persons' table
    persons_table = db.Table('persons', [])

    if "project" not in persons_table.table:
        persons_table.add_column("project", [])
    if "detail" not in person_table.table:
        persons_table.add_column("detail", [])
    if "lead" not in persons_table.table:
        persons_table.add_column("lead", [])
    if "member" not in persons_table.table:
        persons_table.add_column("member", [])
    if "advisor" not in persons_table.table:
        persons_table.add_column("advisor", [])
    if "status" not in persons_table.table:
        persons_table.add_column("status", [])

    # add the 'persons' table into the database
    csv_file_path = os.path.join(os.getcwd(), 'persons.csv')
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            persons_table.insert_entry(row)

    # create a 'login table' table
    login_table = db.Table('login', [])

    # add the login table into the database
    csv_file_path = os.path.join(os.getcwd(), 'login.csv')
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            login_table.insert_entry(row)

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
person_table, login_table = initializing()
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
            print(person_table.table["project"])
        elif choice == '2':
            temp = []
            for i in range(len(person_table.table)):
                temp.append(person_table.table[i]['student'])
            print(temp)
        elif choice == '3':
            table_name = input("Enter the table name: ")
            key = input("Enter the key: ")
            new_value = input("Enter the new value: ")
            person_table.update_entry(table_name, key, new_value)
        elif choice == '4':
            process = True
        else:
            print("Invalid choice. Please try again.")
    exit()

elif role == 'student':
    # see and do student related activities
    print("Welcome to the student menu!")
    print("1. View invitation from lead")
    print("2. Accept or reject invitation")
    print("3. View project details")
    print("4. Create new project")
    print("5. Exit")

elif role == 'member':
    # see and do member related activities
    pass
elif role == 'lead':
    # see and do lead related activities
    pass
elif role == 'faculty':
    # see and do faculty related activities
    pass
elif role == 'advisor':
    # see and do advisor related activities
    pass

# once everything is done, make a call to the exit function
exit()
