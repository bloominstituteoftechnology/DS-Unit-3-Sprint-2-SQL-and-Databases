import sqlite3

nw_conn = sqlite3.connect('northwind_small.sqlite3')

nw_curs = nw_conn.cursor()

### Part 2 Querying with Join

query = """SELECT Product.ProductName from Product ORDER BY Product.UnitPrice DESC LIMIT 10"""
print('The 10 most expensive items are ', nw_curs.execute(query).fetchall())


query = """SELECT AVG(date(Employee.HireDate) - date(Employee.BirthDate)) FROM Employee"""

print('The Average age of employees at hireing date is ',nw_curs.execute(query).fetchall())


### Part 3 Querying with Join

query = """SELECT Product.ProductName, Supplier.CompanyName
from Supplier LEFT JOIN Product
ON Supplier.Id = Product.SupplierId
ORDER BY Product.UnitPrice DESC
LIMIT 10
"""

print('The 10 most expensive items and their supplier are ', nw_curs.execute(query).fetchall())

query = """SELECT Category.CategoryName
FROM Product JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY Product.CategoryID
ORDER BY COUNT(*) DESC
LIMIT 1
"""

print('The largest category of unique items is ', nw_curs.execute(query).fetchall())
