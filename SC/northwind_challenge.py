import query_func

# Part 2 - The Northwind Database
# db to connect to
db = 'northwind_small (1).sqlite3'

# What are the ten most expensive items in the db?
query = """SELECT ProductName, UnitPrice
           FROM product
           ORDER BY UnitPrice DESC
           LIMIT 10;"""
print(run_query(db, query))

# What is the avg age of an employee at the time of hiring?
query = """SELECT ROUND(AVG(HireDate - BirthDate), 1) FROM Employee"""
print(run_query(db, query))

# (Stretch) How does avg age of employee hire vary by city?
query = """SELECT City, ROUND(AVG(HireDate - BirthDate), 1) AS avg_age
           FROM Employee
           GROUP BY City
           ORDER BY avg_age"""
print(run_query(db, query))
