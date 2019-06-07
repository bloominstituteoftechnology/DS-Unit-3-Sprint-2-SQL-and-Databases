import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive products?
answer_1 = """
SELECT ProductName
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
print(curs.execute(answer_1).fetchall())

# What is the average age of an employee at the time 
# of their hiring? (Hint: a lot of arithmetic works with dates.)
answer_2 = """
SELECT ROUND(AVG(HireDate - BirthDate))
FROM Employee;
"""

print(curs.execute(answer_2).fetchone()[0])

# (Stretch) How does the average age of employee at hire vary by city?


# What are the ten most expensive items (per unit price) in the database 
# and their suppliers?
answer_3 = """
SELECT p.ProductName, s.CompanyName
FROM Product AS p, Supplier AS s
WHERE p.SupplierID = s.Id
ORDER BY p.UnitPrice DESC
LIMIT 10;
"""

print(curs.execute(answer_3).fetchall())

# What is the largest category (by number of unique products in it)?
answer_4 = """
SELECT DISTINCT COUNT(*), Product.CategoryID, Category.CategoryName
FROM Product JOIN Category ON Product.CategoryID = Category.Id
GROUP BY Product.CategoryID
ORDER BY COUNT(*) DESC
"""

print(curs.execute(answer_4).fetchone())


# (Stretch) Who's the employee with the most territories? Use 
# TerritoryId (not name, region, or other fields) as the unique 
# identifier for territories.

