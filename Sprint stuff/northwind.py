import sqlite3

# connection and cursors
conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()

# Queries
Q_1 = """SELECT Product.UnitPrice
FROM Product
ORDER BY Product.UnitPrice DESC
LIMIT 10
;"""
Q_2 =  """select AVG(HireDate - BirthDate)
from Employee;
"""
Stretchg_1 = """"""

# Other Part

Q_3 = """SELECT Product.Id, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier
ON Product.id
ORDER BY Product.UnitPrice DESC
LIMIT 10
;"""
Q_4 = """SELECT COUNT(DISTINCT Category.CategoryName), Category.CategoryName
FROM Category
JOIN Product
ON Category.id
ORDER BY COUNT(Category.CategoryName) DESC
LIMIT 1
;"""
Stretchg_2 = """"""
