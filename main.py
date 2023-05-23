import os
import sqlite3


def main():
    while True:
        os.system('cls')
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        value = int(input("Please choose an option: "))
        return value


def dbConnection():
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS employee 
        (employeeID INTEGER PRIMARY KEY NOT NULL,
        employeeName TEXT, contact TEXT, salary INTEGER)"""
    cur.execute(query)
    conn.commit()
    cur.close()


def dbCursor():
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    return cur, conn


def search_by_id(search):
    cur, conn = dbCursor()
    search_query = '''SELECT * from employee WHERE employeeID = ?'''
    cur.execute(search_query, search)
    row = cur.fetchone()
    while (row != None):
        print(f"{row[0]: 30} {row[1]:5} {row[2]:5} {row[3]:5}")
        row = cur.fetchone()


def search_by_name(search):
    cur, conn = dbCursor()
    search = "%" + search + "%"
    search_query = '''SELECT * from employee WHERE employeeName LIKE ?'''
    cur.execute(search_query, [search])
    # cur.execute("SELECT * FROM employee WHERE employeeName LIKE '%{}%'".format(search))
    # search = "%" + search + "%"
    # cur.execute("SELECT * FROM employee WHERE employeeName LIKE '%s'" % search)
    row = cur.fetchone()
    while (row != None):
        print(f"{row[0]: 30} {row[1]:5} {row[2]:5} {row[3]:5}")
        row = cur.fetchone()


def view_employee():
    '''this function helps view an employee record'''
    print("Do you want to search by ID or Name?\na) ID\nb) Name")
    user_choice = input("Please enter your choice: ")
    if user_choice == "a":
        print("call search by id method")
        search = input("Please enter the Employee ID: ")
        search_by_id(search)
    elif user_choice == "b":
        print("call search by name method")
        search = input("Please enter the Employee Name: ")
        search_by_name(search)
    else:
        print("Enter a correct option. 'a for ID' or 'b for Name'")

def getEmployeeDetails():
    """this method gets user input"""
    first_name = str(input("Please enter the first name: "))
    last_name = str(input("Please enter the last name: "))
    contact = str(input("Please enter the contact: "))
    salary = int(input("Please enter the salary: "))
    addEmployeeDb(first_name, last_name, contact, salary)


def addEmployeeDb(fname, lname, cont, sal):
    cur, conn = dbCursor()
    name = fname + " " + lname
    insert1 = """INSERT INTO employee
        (employeeName, contact, salary)
        VALUES (?, ?, ?)"""
    cur.execute(insert1, (name, cont, sal))
    conn.commit()

if __name__ == '__main__':
    dbConnection()
    while True:
        option = main()
        if option == 1:
            getEmployeeDetails()
            print("Employee successfully added.")
        elif option == 2:
            view_employee()
            print("You pressed 2.")
        elif option == 3:
            print("You pressed 3.")
        elif option == 4:
            print("You pressed 4.")
        elif option == 5:
            print("Bye-bye.")
            exit()
        else:
            print("Wrong key pressed.")