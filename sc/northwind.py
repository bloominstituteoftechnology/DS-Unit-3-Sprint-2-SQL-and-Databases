import pandas as pd
import sqlite3
from pandas import DataFrame 

n_conn = sqlite3.connect('northwind_small.sqlite3')
n_curs = conn.cursor()


# What are the ten most expensive items (per unit price) in the database?
query = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""
n_curs.execute(query)
print(n_curs.fetchall())


# What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)

query = """
SELECT AVG(HireDate-BirthDate)
FROM Employee
"""
n_curs.execute(query)
print(n_curs.fetchall())

# answer: 37.22

# (*Stretch*) How does the average age of employee at hire vary by city?
query = ""SELECT City, AVG(HireDate-BirthDate)
FROM Employee
GROUP BY City
""
n_curs.execute(query)
print(n_curs.fetchall())

# What are the ten most expensive items (per unit price) 
# in the database *and* their suppliers?
query = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier
ON SupplierID=SupplierID
ORDER BY UnitPrice DESC
LIMIT 10
"""
n_curs.execute(query)
print(n_curs.fetchall())

# What is the largest category (by number of unique products in it)?
query = """
SELECT CategoryName, COUNT(CategoryName)
FROM Category as c
JOIN Product as p
ON c.ID=p.CategoryID
GROUP BY CategoryName
ORDER by COUNT(CategoryName) DESC
"""
n_curs.execute(query)
print(n_curs.fetchall())

# largest category is Confections 13

# (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
# (not name, region, or other fields) as the unique identifier for territories.