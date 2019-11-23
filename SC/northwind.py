import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

query1 = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""

res1 = cur.execute(query1)
print(res1.fetchall())

query2 = """
SELECT AVG(Age)
FROM
(
    SELECT HireDate - BirthDate
    AS Age
    FROM Employee
)
"""

res2 = cur.execute(query2)
print(res2.fetchall())

query3 = """
SELECT p.ProductName, s.CompanyName
FROM Product p
LEFT JOIN Supplier s
ORDER BY p.UnitPrice
LIMIT 10
"""

res3 = cur.execute(query3)
print(res3.fetchall())

query4 = """
SELECT COUNT(*), c.CategoryName
FROM Product p
INNER JOIN Category c
WHERE p.CategoryId = c.Id
ORDER BY p.CategoryId
"""

res4 = cur.execute(query4)
print(res4.fetchall())
