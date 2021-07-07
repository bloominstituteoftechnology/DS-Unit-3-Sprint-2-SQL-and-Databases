import sqlite3

# connect to northwind_small.sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')

# create a cursor
cur = conn.cursor()

# explore tables in database
tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
print(tables)

# explore customer table and value types
suppler_table = cur.execute("SELECT sql FROM sqlite_master WHERE name='Product';").fetchall()
print(suppler_table)

""" PART 2 - Sailing the Northwind SeasThe Northwind Database """

# find the ten most expensive items (per unit price)
query = """
SELECT ProductName
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
most_expensive = cur.execute(query).fetchall()
print(most_expensive)

# what is the average age of an employee at time of hiring
query = """
SELECT ROUND(AVG (HireDate - BirthDate)) as AverageAgeWhenHired
FROM Employee;
"""
avg_age_when_hired = cur.execute(query).fetchall()
print(avg_age_when_hired)

# average age of employee by city
query = """
SELECT City, ROUND(AVG (HireDate - BirthDate)) as AverageAgeWhenHired
FROM Employee
GROUP BY City;
"""
avg_age_by_city = cur.execute(query).fetchall()
print(avg_age_by_city)

""" PART 3 - Sailing the Northwind Seas """

# find the ten most expensive items w/suppliers
query = """
SELECT p.ProductName, s.CompanyName 
FROM Product p
INNER JOIN Supplier s
ON s.ID = p.SupplierID
ORDER BY p.UnitPrice DESC
LIMIT 10;
"""
expensive_with_supplier = cur.execute(query).fetchall()
print(expensive_with_supplier)

# largest category by number of unique products
query = """
SELECT DISTINCT COUNT(p.ProductName) as Number_of_products, c.CategoryName
FROM Product p
JOIN Category c 
ON c.ID = p.CategoryID
GROUP BY c.CategoryName
ORDER BY Number_of_products DESC
LIMIT 1;
"""
category_with_most_products = cur.execute(query).fetchall()
print(category_with_most_products)

