import sqlite3

# Database Connection
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary REAL
)
""")
conn.commit()

# Add Employee
def add_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    cursor.execute(
        "INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)",
        (name, age, department, salary)
    )
    conn.commit()
    print("Employee Added Successfully!")

# View Employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("\nEmployee Records")
    print("-" * 50)

    for emp in employees:
        print(f"ID: {emp[0]}")
        print(f"Name: {emp[1]}")
        print(f"Age: {emp[2]}")
        print(f"Department: {emp[3]}")
        print(f"Salary: {emp[4]}")
        print("-" * 50)

# Search Employee
def search_employee():
    emp_id = int(input("Enter Employee ID: "))
    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    emp = cursor.fetchone()

    if emp:
        print(emp)
    else:
        print("Employee Not Found!")

# Update Employee
def update_employee():
    emp_id = int(input("Enter Employee ID: "))
    salary = float(input("Enter New Salary: "))

    cursor.execute(
        "UPDATE employees SET salary=? WHERE id=?",
        (salary, emp_id)
    )
    conn.commit()
    print("Employee Updated Successfully!")

# Delete Employee
def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    print("Employee Deleted Successfully!")

# Main Menu
while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid Choice!")

conn.close()
