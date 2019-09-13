import query_func

# Part 2 - The Northwind Database
# db to connect to
db = 'northwind_small (2).sqlite3'

# What are the ten most expensive items in the db?
query = """SELECT ProductName, UnitPrice
           FROM product
           ORDER BY UnitPrice DESC
           LIMIT 10;"""
print(run_query(db, query))

# What is the avg age of an employee at the time of hiring?
query = """SELECT ROUND(AVG(HireDate - BirthDate), 1) FROM Employee;"""
print(run_query(db, query))

# (Stretch) How does avg age of employee hire vary by city?
query = """SELECT City, ROUND(AVG(HireDate - BirthDate), 1) AS avg_age
           FROM Employee
           GROUP BY City
           ORDER BY avg_age;"""
print(run_query(db, query))

# Part 3 - Sailing the Northwind Seas
# What are the ten most expensive items in the database and their suppliers?
query = """SELECT DISTINCT (p.ProductName), s.CompanyName
           FROM Product AS p JOIN Supplier AS s
           ON SupplierId = SupplierId
           ORDER BY p.UnitPrice DESC
           LIMIT 10;"""
# NOT SURE THIS IS RIGHT
print(run_query(db, query))

# What is the largest category?
query = """SELECT c.CategoryName, COUNT(DISTINCT p.ProductName) as count
           FROM Category as c JOIN Product as p
           ON c.Id=p.CategoryId
           GROUP BY CategoryName
           ORDER BY count DESC
           LIMIT 1;"""

# Who's the employee with the most territories?
query = """SELECT EmployeeId, e.FirstName, e.LastName, COUNT(et.TerritoryId) as count
           FROM Employee as e JOIN EmployeeTerritory as et
           ON et.EmployeeId=e.Id
           GROUP BY e.Id
           ORDER BY count DESC
           LIMIT 1;"""
print(run_query(db, query))
