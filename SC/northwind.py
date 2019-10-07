
import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Top 10 most expensive products by unit price
query = """SELECT ProductName, UnitPrice FROM product
ORDER BY UnitPrice DESC LIMIT 10;"""

curs.execute(query)
results = curs.fetchall()
print("-------------------ANSWERS---------------")
print("Top 10 most expensive products:\n", results)

# What is the average age of an employee at the time of their hiring?
query = """SELECT AVG(HireDate-BirthDate) FROM Employee;"""

curs.execute(query)
results = curs.fetchall()
print("\nAverage age of employee at Hire Date:\n", results[0][0])

# *Stretch* How does the average age of employee at hire vary by city?
query = """SELECT City, AVG(HireDate-BirthDate) FROM Employee
GROUP BY City;"""
curs.execute(query)
results = curs.fetchall()
print("\nAverage age of employee by city:\n", results)

# 10 most expensive items and their suppliers
query = """SELECT ProductName, CompanyName FROM product, Supplier
WHERE Product.SupplierId = Supplier.id
ORDER BY UnitPrice DESC LIMIT 10;"""

curs.execute(query)
results = curs.fetchall()
print('10 Most expensive items and their suppliers', results)

# What is the largest category (by number of unique products in it)?
query = """SELECT CategoryName, COUNT(DISTINCT ProductName) AS count
FROM Product, Category
WHERE Product.CategoryId = Category.id
GROUP BY CategoryName
ORDER BY count DESC
LIMIT 1;"""

curs.execute(query)
results = curs.fetchall()
print('\nLargest category:\n', results[0][0])

