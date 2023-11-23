# import database module
import database as db
import csv
import os

# define a function called initializing
my_db = db.DB()


def initializing():
    # create a 'persons' table
    persons_table = db.Table('persons', [])

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

if role == 'admin':
    # see and do admin related activities
    pass
elif role == 'student':
    # see and do student related activities
    pass
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
