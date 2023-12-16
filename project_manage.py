# project_manage.py

from database import DatabaseManager, Table

# Create a DatabaseManager instance
db_manager = DatabaseManager()

# Initialize function to create tables and add columns


def initializing():
    # Insert a 'persons' table into the database
    persons_table = db_manager.insert_table('persons', 'persons.csv')

    # Insert a 'login' table into the database
    login_table = db_manager.insert_table('login', 'login.csv')

    # Add columns to the 'persons' table if they don't exist
    persons_table.add_column("project", [])
    persons_table.add_column("detail", [])
    persons_table.add_column("member1", [])
    persons_table.add_column("member1_msg", [])
    persons_table.add_column("member2_msg", [])
    persons_table.add_column("member2", [])
    persons_table.add_column("advisor", [])
    persons_table.add_column("advisor_status", [])
    persons_table.add_column("advisor_msg", [])
    persons_table.add_column("status1", [])
    persons_table.add_column("status2", [])
    persons_table.add_column("submit", [])

    return persons_table, login_table


# Initialize tables
persons_table, login_table = initializing()
print(login_table.table)

# Login function


def login():
    while True:
        person_id = input("Enter your username: ")
        password = input("Enter your password: ")

        if person_id.lower() == 'exit' or password.lower() == 'exit':
            print("Exiting...")
            break

        for entry in login_table.table:
            if entry['username'] == person_id and entry['password'] == password:
                print("Login successful!")
                person_id = person_id[:-2]
                return person_id, entry['role']

        print("Invalid username or password. Please try again.")

# Exit function


def exit_program():
    # Save the tables to the csv files
    persons_table.save_table('persons.csv')
    login_table.save_table('login.csv')
    print("Exiting...")


# Make calls to the login function
person_id, role = login()

# Based on the return value for login, activate the code that performs activities according to the role defined for that person_id
process = False
while not process:
    if role == 'admin':
        # see and do admin related activities
        while not process:
            print("Welcome to the admin menu!")
            print("1. View all projects")
            print("2. View all students")
            print("3. Update a table")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                print(persons_table.table)
            elif choice == '2':
                temp = []
                for i in persons_table.table:
                    if i['type'] == "student":
                        temp.append(i)
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
    elif role == 'lead':
        # see and do student-related activities
        print("Welcome to the lead menu!")
        print("1. Create project")
        print("2. View project")
        print("3. Modify project")
        print("4. Send request to advisor")
        print("6. Exit")
        while not process:
            choice = input("Enter your choice: ")
            if choice == "1":
                print("Creating a new project...")
                project_name = input("Enter the project name: ")
                project_detail = input("Enter the project detail: ")
                while check < 2:
                    project_member1 = input(
                        "Enter the project member username: ")
                    project_member1_msg = input(
                        "Enter the project member1 message: ")
                    project_member2 = input(
                        "Enter the project member username: ")
                    project_member2_msg = input(
                        "Enter the project member2 message: ")
                    check = 0
                    for entry in login_table.table:
                        if entry['username'] == project_member1:
                            check += 1
                        if entry['username'] == project_member2:
                            check += 1
                    if check < 2:
                        print("Invalid username(s). Please try again.")
                for count in range(len(persons_table.table)):
                    if persons_table.table[count]["first"] == person_id:
                        persons_table.table[count]['project'] = project_name
                        persons_table.table[count]['detail'] = project_detail
                        persons_table.table[count]['member1'] = project_member1
                        persons_table.table[count]['member2'] = project_member2
                        persons_table.table[count]['status1'] = "pending"
                        persons_table.table[count]['status2'] = "pending"
                        persons_table.table[count]['submit'] = "not submitted"
                        persons_table.table[count]['member1_msg'] = project_member1_msg
                        persons_table.table[count]['member2_msg'] = project_member2_msg
                        persons_table.table[count]['type'] = "lead"
                        login_table.table[count]['role'] = "lead"
                        print("Project created!")
                        break
            elif choice == "2":
                print("Viewing project...")
                for entry in persons_table.table:
                    if entry['first'] == person_id:
                        print(entry)
            elif choice == "3":
                print("Modifying project...")
                print("1. Modify project name")
                print("2. Modify project detail")
                print("3. Modify project member1")
                print("4. Modify project member1_msg")
                print("5. Modify project member2")
                print("6. Modify project member2_msg")
                print("7. Exit")
                modify_choice = input("Enter your choice: ")
                modify_status = False
                while not modify_status:
                    if modify_choice == "1":
                        new_project_name = input(
                            "Enter the new project name: ")
                        for entry in persons_table.table:
                            if entry['first'] == person_id:
                                entry['project'] = new_project_name
                                print("Project name updated!")
                                modify_status = True
                    elif modify_choice == "2":
                        new_project_detail = input(
                            "Enter the new project detail: ")
                        for entry in persons_table.table:
                            if entry['first'] == person_id:
                                entry['detail'] = new_project_detail
                                print("Project detail updated!")
                                modify_status = True
                    elif modify_choice == "3":
                        new_project_member1 = input(
                            "Enter the new project member1: ")
                        for entry in persons_table.table:
                            if entry['first'] == person_id:
                                entry['member1'] = new_project_member1
                                print("Project member1 updated!")
                                modify_status = True
                    elif modify_choice == "4":
                        new_project_member1_msg = input(
                            "Enter the new project member1_msg: ")
                        for entry in persons_table.table:
                            if entry['first'] == person_id:
                                entry['member1_msg'] = new_project_member1_msg
                                print("Project member1_msg updated!")
                                modify_status = True
                    elif modify_choice == "5":
                        new_project_member2 = input(
                            "Enter the new project member2: ")
                        for entry in persons_table.table:
                            if entry['first'] == person_id:
                                entry['member2'] = new_project_member2
                                print("Project member2 updated!")
                                modify_status = True
                    elif modify_choice == "6":
                        new_project_member2_msg = input(
                            "Enter the new project member2_msg: ")
                        for entry in persons_table.table:
                            if entry['first'] == person_id:
                                entry['member2_msg'] = new_project_member2_msg
                                print("Project member2_msg updated!")
                                modify_status = True
                    elif modify_choice == "7":
                        modify_status = True
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "4":
                print("Sending request to advisor...")
                for entry in persons_table.table:
                    if entry['first'] == person_id:
                        entry['advisor_status'] = "pending"
                        entry['status'] = "pending"
                        print("Request sent!")
                        break
    elif role == "student":
        print("Welcome to the student menu!")
        print("1. See invitation from leader")
        print("2. Accept or Deny invitation")
        print("3. Become leader of a project")
        print("4. Exit")
        process = False
        while not process:
            choice = input("Enter your choice: ")
            if choice == "1":
                print("Viewing invitation...")
                for entry in persons_table.table:
                    if entry['member1'] or entry["member2"] == person_id:
                        print(entry)
                        key = True
            elif choice == "2" and key == True:
                print("Accepting or denying invitation...")
                print("1. Accept invitation")
                print("2. Deny invitation")
                print("3. Exit")
                accept_status = False
                while not accept_status:
                    accept_choice = input("Enter your choice: ")
                    if choice == 1:
                        for entry in len(persons_table.table):
                            if persons_table.table[entry]['member1'] == person_id:
                                persons_table.table[entry]['status1'] = "accepted"
                                persons_table.table[entry]['type'] = "member1"
                                login_table.table[entry]['role'] = "member1"
                                print("Invitation accepted!")
                                accept_status = True
                            elif persons_table.table[entry]['member2'] == person_id:
                                persons_table.table[entry]['status2'] = "accepted"
                                persons_table.table[entry]['type'] = "member2"
                                login_table.table[entry]['role'] = "member2"
                                print("Invitation accepted!")
                                accept_status = True
                        print("exit and login to see changes")
                    elif choice == 2:
                        for entry in len(persons_table.table):
                            if persons_table.table[entry]['member1'] == person_id:
                                persons_table.table[entry]['status1'] = "denied"
                                print("Invitation denied!")
                                accept_status = True
                            elif persons_table.table[entry]['member2'] == person_id:
                                persons_table.table[entry]['status2'] = "denied"
                                print("Invitation denied!")
                                accept_status = True

            elif choice == "3":
                print("Becoming leader of a project...")
                print("1. Become leader")
                print("2. Exit")
                become_choice = input("Enter your choice: ")
                become_status = False
                while not become_status:
                    if become_choice == "1":
                        for entry in persons_table.table:
                            if entry['first'] == person_id:
                                entry['type'] = "lead"
                                print("You are now the leader!")
                                print(
                                    "Exit and login again to see the change and used the lead menu.")
                                become_status = True
                    elif become_choice == "2":
                        become_status = True
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "4":
                process = True
            else:
                print("Invalid choice. Please try again.")
    elif role == "member1" or role == "member2":
        print("Welcome to the member menu!")
        print("1. View project")
        print("2. Exit")
        process = False
        while not process:
            choice = input("Enter your choice: ")
            if choice == "1":
                print("Viewing project...")
                for entry in len(persons_table.table[role]):
                    if persons_table.table[entry][role] == person_id:
                        print(persons_table.table[entry])
                        print("Do you want to modify your project detail?")
                        print("1. Yes")
                        print("2. No")
                        modify_choice = input("Enter your choice: ")
                        modify_status = False
                        while not modify_status:
                            if modify_choice == "1":
                                persons_table.table[entry]['detail'] = input(
                                    "Enter the new project detail: ")
                                print("Project detail updated!")
                                modify_status = True
                            elif modify_choice == "2":
                                modify_status = True
                                print("Exiting...")
                            else:
                                print("Invalid choice. Please try again.")
    elif role == "faculty":
        print("Welcome to the faculty menu!")
        print("1. View all requests")
        print("2. Add msg or approve the approve the project")
        print("3. Exit")
        process = False
        while not process:
            choice = input("Your choice: ")
            if choice == "1":
                print("Viewing all requests...")
                for entry in persons_table.table["advisor_status"]:
                    if entry["advisor_status"] == "pending":
                        print(entry)
                        print("Do you want to accept or deny the request?")
                        print("1. Accept")
                        print("2. Deny")
                        print("3. Exit")
                        accept_status = False
                        while not accept_status:
                            accept_choice = input("Enter your choice: ")
                            if accept_choice == "1":
                                entry["advisor"] = person_id
                                entry["advisor_status"] = "accepted"
                                print("Request accepted!")
                                accept_status = True
                            elif accept_choice == "2":
                                entry["advisor_status"] = "denied"
                                print("Request denied!")
                                accept_status = True
                            elif accept_choice == "3":
                                accept_status = True
                            else:
                                print("Invalid choice. Please try again.")
            elif choice == "2":
                select = input("Enter the project name: ")
                for entry in persons_table.table:
                    if entry["project"] == select:
                        print("1. Add msg")
                        print("2. Approve the project")
                        print("3. Exit")
                        modify_choice = input("Enter your choice: ")
                        modify_status = False
                        while not modify_status:
                            if modify_choice == "1":
                                entry["advisor_msg"] = input(
                                    "Enter the new message: ")
                                print("Message added!")
                                modify_status = True
                            elif modify_choice == "2":
                                entry["advisor_status"] = "approved"
                                print("Project approved!")
                                modify_status = True
                            elif modify_choice == "3":
                                modify_status = True
                            else:
                                print("Invalid choice. Please try again.")
            elif choice == "3":
                process = True

# Once everything is done, make a call to the exit_program function
if process == True:
    exit_program()
