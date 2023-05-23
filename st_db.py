import sqlite3
import os


def main():
    while True:
        os.system('cls')
        print("To add an employee, type 1")
        print("To view an employee, type 2")
        print("To update an employee, type 3")
        print("To delete an employee, type 4")
        print("To exit, type 5")
        user_choice = input("Please enter your choice: ")
        return user_choice


def db_connection():
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS employee(employeeID INTEGER PRIMARY KEY NOT NULL,
     employeeName TEXT, contact TEXT, salary INTEGER)'''
    cur.execute(query)
    conn.commit()
    cur.close()


def db_cursor():
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    return conn, cur


def search_by_id(search):
    conn, cur = db_cursor()
    search_query = '''SELECT * FROM employee WHERE employeeID = ?'''
    cur.execute(search_query, search)
    row = cur.fetchone()
    while row != None:
        print(f"{row[0]: 30} {row[1]:5} {row[2]:5} {row[3]:5}")
        row = cur.fetchone()


def search_by_name(search):
    conn, cur = db_cursor()
    search = "%" + search + "%"
    search_query = '''SELECT * FROM employee WHERE employeeName LIKE ?'''
    cur.execute(search_query, [search])
    row = cur.fetchone()
    while row != None:
        print(f"{row[0]: 30} {row[1]:5} {row[2]:5} {row[3]:5}")
        row = cur.fetchone()


def view_employee():
    '''This method views an employee record from the database'''
    print("Do you want to search by ID or Name?\n---> Type '1' for ID\n---> Type '2' for Name")
    user_choice = input("PLease enter your choice: ")
    if user_choice == "1":
        print("Call search by ID method")
        search = input("Please enter Employee ID: ")
        search_by_id(search)
    if user_choice == "2":
        print("Call search by Name method")
        search = input("Please enter Employee Name: ")
        search_by_name(search)


def add_employee(fname, lname, contact, salary):
    '''This method adds an employee to the database'''
    conn, cur = db_cursor()
    name = fname + " " + lname
    query = '''INSERT INTO employee(employeeName, Contact, Salary) VALUES (?, ?, ?)'''
    cur.execute(query, (name, contact, salary))
    conn.commit()


def get_employee_details():
    '''This method gets input from user'''
    first_name = str(input("Please enter first name: "))
    last_name = str(input("Please enter last name: "))
    contact = str(input("Please enter contact number: "))
    salary = int(input("Please enter salary: "))
    add_employee(first_name, last_name, contact, salary)


def update_employee():
    '''This method updates an existing record of an employee'''
    print("You can update employee salary by Employee ID")
    emp_id = int(input("Please enter employee ID: "))
    new_salary = int(input("Please enter the updated salary: "))
    update_by_id(emp_id, new_salary)


def update_by_id(emp_id, new_salary):
    conn, cur = db_cursor()
    query = '''UPDATE employee SET salary = ?
               WHERE employeeID = ?'''
    cur.execute(query, (new_salary, emp_id))
    conn.commit()


def delete_employee():
    print("Do you want to delete employee record using ID or Name"
          "\nTo delete using ID type '1'\nTo delete using Name type '2'")
    user_choice = input("Please enter your choice: ")
    if user_choice == "1":
        print("Call delete by ID method")
        user_id = input("Please enter Employee ID to delete the record: ")
        delete_by_id(user_id)
    elif user_choice == "2":
        print("Call delete by Name method")
        user_name = input("Please enter Employee Name to delete the record: ")
        delete_by_name(user_name)


def delete_by_id(user_id):
    conn, cur = db_cursor()
    query = '''DELETE FROM employee WHERE employeeID = ?'''
    cur.execute(query, user_id)
    conn.commit()


def delete_by_name(user_name):
    conn, cur = db_cursor()
    query = '''DELETE FROM employee WHERE employeeName = ?'''
    cur.execute(query, [user_name])
    conn.commit()


if __name__ == "__main__":
    while True:
        option = main()
        if option == "1":
            get_employee_details()
            print("Employee added")
            print("")
        elif option == "2":
            view_employee()
            print("Employee Viewed")
            print("")
            os.system('cls')
        elif option == "3":
            update_employee()
            print("Employee Updated")
            print("")
        elif option == "4":
            delete_employee()
            print("Employee Deleted")
            print("")
        elif option == "5":
            print("Good bye!")
            exit()
        else:
            print("You have entered the wrong value")
