import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
query = """SELECT ProductName
           FROM Product
           ORDER BY UnitPrice DESC
           LIMIT 10;"""
result = curs.execute(query)
print(result.fetchall())

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
query = """SELECT AVG(HireDate - BirthDate) as 'Average Worker Age at Hire'
           FROM Employee"""
result = curs.execute(query)
print(result.fetchall())

# How does the average age of employee at hire vary by city?
query = """SELECT City, AVG(HireDate - BirthDate) as 'Average Worker Age at Hire'
           FROM Employee
           GROUP BY City"""
result = curs.execute(query)
print(result.fetchall())

# What are the ten most expensive items (per unit price) in the database and
# their suppliers?
query = """SELECT Product.ProductName, Supplier.CompanyName as 'Supplier Name'
            FROM Product, Supplier
            WHERE Product.ProductName IN (
                    SELECT ProductName
                    FROM Product
                    ORDER BY UnitPrice DESC
                    LIMIT 10
                    )
            ORDER BY Product.UnitPrice DESC"""
result = curs.execute(query)
print(result.fetchall())

# What is the largest category (by number of unique products in it)?
query = """SELECT category.CategoryName as 'Category w/ Most Unique Products'
            FROM Product
            JOIN category ON product.CategoryId = Category.Id
            GROUP BY CategoryId
            ORDER BY COUNT(CategoryId) DESC
            LIMIT 1;"""
result = curs.execute(query)
print(result.fetchall())

# Who's the employee with the most territories? Use TerritoryId (not name,
# region, or other fields) as the unique identifier for territories.
query = """SELECT Employee.FirstName, Employee.LastName
            FROM EmployeeTerritory
            JOIN Employee ON EmployeeTerritory.EmployeeId = Employee.Id
            GROUP BY EmployeeId
            ORDER BY COUNT(TerritoryId) DESC
            LIMIT 1;"""
result = curs.execute(query)
print(result.fetchall())