import sqlite3


# Example class
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


# Datatypes
# NULL
# INTEGER
# REAL (FLOAT)
# TEXT (TEXT STORED USING UTF-8 ETC)
# BLOB (TEXT STPORED EXACTLY AS INPUT)


# How to make a db in memory.
conn = sqlite3.connect(':memory:')
# How to make a db in file
# conn = sqlite3.connect('employee.db')

# Create a cursor to execute SQL commands
c = conn.cursor()

# setup a SQL query (like staging changes)
c.execute("""CREATE TABLE employees (
    first text,
    last text,
    pay integer)
    """)

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

# Two correct methods of inserting .
# BB API placeholder method of inserting
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# using a dictionary
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_1.pay})
conn.commit()

# BAD WAY VULNERABLE TO INJECTION
# c.execute("INSERT INTO employees VALUES ('John', 'Smith', '60000')")
# conn.commit()

# Normal SQL Query (again not using raw SQL)
c.execute("SELECT * FROM employees WHERE last = :last", {'last': 'Doe'})

# Fetches first result
# print(c.fetchone())

# Fetch all results as list of lists
print(c.fetchall())

# commit the change (like commit-> push)
conn.commit()


# example functions. (Showing how to use WITH to not need conn.close())
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


# close connection
conn.close()
