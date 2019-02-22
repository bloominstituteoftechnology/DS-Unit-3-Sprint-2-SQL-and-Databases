#!/usr/bin/env python
"""Northwind"""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#Part 2

# Question 1

query1 = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

curs.execute(query1)
curs.fetchall()

# Question 2

query2 = """
SELECT AVG(HireDate - BirthDate) as AgeOfHire
FROM Employee;


"""

curs.execute(query2)
curs.fetchall()

query3 = """
SELECT City, AVG(HireDate - BirthDate) as AgeOfHire
FROM Employee
GROUP BY City;

"""

curs.execute(query3)
curs.fetchall()

# Part 3

# Question 1
query4 = """
SELECT p.ProductName, s.CompanyName, p.UnitPrice
FROM Product AS p, Supplier AS s
WHERE p.SupplierId = s.Id
ORDER BY p.UnitPrice DESC
LIMIT 10
"""

curs.execute(query4)
curs.fetchall()

# Question 2
query5 = """
SELECT c.CategoryName, p.CategoryId, COUNT(p.CategoryId) as total
FROM Product AS p, Category AS c
WHERE p.CategoryId = c.Id
GROUP BY p.CategoryId
ORDER BY total DESC
LIMIT 1
"""

curs.execute(query5)
curs.fetchall()

conn.commit()