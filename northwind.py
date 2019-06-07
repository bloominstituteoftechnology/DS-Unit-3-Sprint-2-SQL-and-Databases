import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

query1 = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""

print(curs.execute(query1).fetchall())
conn.commit()

query2 = """
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""

query3 = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product, Supplier
WHERE Product.SupplierID = Supplier.ID
ORDER BY UnitPrice DESC
LIMIT 10
"""

print(curs.execute(query3).fetchall())
conn.commit()

query4 = """
SELECT COUNT(CategoryId)
FROM Product
ORDER BY COUNT(CategoryId) DESC
LIMIT 1
"""

print(curs.execute(query4).fetchall())
conn.commit()
