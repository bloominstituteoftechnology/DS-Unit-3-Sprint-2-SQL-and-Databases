import sqlite3


# Test the connection, get names for all tables
q1 = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"

# The ten most expensive items per unit price
q2 = """SELECT ProductName, UnitPrice FROM Product
        ORDER BY UnitPrice DESC LIMIT 10"""

# Average age of an employee at the time of their hiring
q3 = """SELECT AVG(substr(HireDate, 1, 4) - substr(BirthDate, 1, 4))
        FROM Employee"""

# Stretch: how does the average age of an employee at hire vary by city?
q4 = """SELECT City, AVG(substr(HireDate, 1, 4) - substr(BirthDate, 1, 4))
        FROM Employee GROUP BY City"""

# What are the ten most expensive items in the db and their suppliers
q5 = """SELECT ProductName, UnitPrice, CompanyName FROM Product
        JOIN supplier
        ON Product.supplierId = Supplier.id
        ORDER BY UnitPrice DESC LIMIT 10;"""

# What is the largest category by number of unique products?
q6 = """SELECT CategoryName, COUNT(*)
        FROM Product JOIN Category
        ON Product.CategoryId = Category.Id
        GROUP BY CategoryName
        ORDER BY COUNT(*) DESC LIMIT 1"""

# Stretch: What is the name of the employee with the most territories?
# Use `TerritoryId`(not name, region, or other fields) as the unique identifier
# for territories.
q7 = """SELECT FirstName, LastName, COUNT(*)
        FROM Employee JOIN EmployeeTerritory
        ON Employee.Id = EmployeeTerritory.EmployeeId
        GROUP BY FirstName, LastName
        ORDER BY COUNT(*) DESC LIMIT 1"""

queries = [q1, q2, q3, q4, q5, q6, q7]


def execute_sql(queries, db_name):
    """Instantiate connection and cursor objects
       and execute SQL queries from queries list"""
    conn = sqlite3.connect(db_name)
    curs = conn.cursor()
    for q in queries:
        print('\n', curs.execute(q).fetchall())

execute_sql(queries, 'northwind_small.sqlite3')
