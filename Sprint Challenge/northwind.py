#!/usr/bin/env/ python

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Fetchall data
curs.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;""").fetchall()

# Query to see schema behind the table
curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()

# Ten most expensive items per unit price with descending order
top_ten_query = """
SELECT prod.ProductName, prod.UnitPrice
FROM Product AS prod
ORDER BY prod.UnitPrice DESC
LIMIT 10;"""

#What is the average age of an employee at the time of their hiring?
avg_age_query = """
SELECT AVG(HireDate - BirthDate) as avg_age
FROM Employee;"""

# (*Stretch*) How does the average age of employee at hire vary by city?

#PART 3

# What are the ten most expensive items (per unit price) in the
# database *and*their suppliers?
top_ten_and_suppliers = """
SELECT prod.ProductName, prod.UnitPrice, sup.CompanyName
FROM Product AS prod
JOIN Supplier AS sup ON sup.ID = prod.SupplierID
ORDER BY prod.UnitPrice DESC
LIMIT 10;"""

# What is the largest category (by number of products in it)?
largest_category_query = """
SELECCT cat.CategoryName, COUNT(prod.CategoryID)
FROM Product AS prod
INNER JOIN Category AS cat
ON prod.CategoryID = cat.ID
GROUP BY prod.CategoryID
ORDER BY COUNT(prod.CategoryID) DESC
LIMIT 1;"""

# (*Stretch*) What is the top territory (by number of employees),
# andhow many employees does it have?
# top_territory_query = """
# SELECT Territory.TerritoryDescription, COUNT()
# FROM EmployeeTerritory as et
# JOIN
# GROUP BY
# ORDER BY
# LIMIT 1;"""

def part_three(x):
    print(curs.execute(x).fetchall())