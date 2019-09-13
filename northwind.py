# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('northwind_small(1).sqlite3')
c = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
query1 = 'SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
c.execute(query1)
print(c.fetchall())
'''
Côte de Blaye
Thüringer Rostbratwurst
Mishi Kobe Niku
Sir Rodney's Marmalade
Carnarvon Tigers
Raclette Courdavault
Manjimup Dried Apples
Tarte au sucre
Ipoh Coffee
Rössle Sauerkraut
'''

# What is the average age of an employee at the time of their hiring?
query2 = 'SELECT AVG(HireDate - BirthDate) From Employee;'
c.execute(query2)
print(c.fetchone())
# Answer = 37.2 years old

# What are the ten most expensive items (per unit price) in the database
# and their suppliers?
query3 =
'''
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier ON (SupplierID = SupplierID)
GROUP BY ProductName
ORDER BY UnitPrice DESC LIMIT 10
'''
c.execute(query3)
print(c.fetchall())
'''
Côte de Blaye	263.5	Exotic Liquids
Thüringer Rostbratwurst	123.79	Exotic Liquids
Mishi Kobe Niku	97	Exotic Liquids
Sir Rodney's Marmalade	81	Exotic Liquids
Carnarvon Tigers	62.5	Exotic Liquids
Raclette Courdavault	55	Exotic Liquids
Manjimup Dried Apples	53	Exotic Liquids
Tarte au sucre	49.3	Exotic Liquids
Ipoh Coffee	46	Exotic Liquids
Rössle Sauerkraut	45.6	Exotic Liquids
'''
# Alternative Solution
'''
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier ON (SupplierID = SupplierID)
ORDER BY UnitPrice DESC LIMIT 290
'''
# Or isolate top ten products using WHERE IN to list top 10

# What is the largest category (by number of unique products in it)?
query4 = '''
SELECT CategoryName, COUNT(ProductName)
FROM Product
JOIN Category ON (CategoryId = CategoryId)
GROUP BY CategoryName
ORDER BY COUNT(ProductName) DESC
'''
# Multiple columns with the same number, otherwise you could isolate
# top product
c.execute(query4)
print(c.fetchall())
'''
Beverages	77
Condiments	77
Confections	77
Dairy Products	77
Grains/Cereals	77
Meat/Poultry	77
Produce	77
Seafood	77
'''

"""
Q1: In the Northwind database, what is the type of relationship between
    the Employee and Territory tables?

A1: The relationship focuses on which employees work in which territory
    to keep a geographical count of employees. This relationship can
    be considered a one-to-many, where multiple employees can have the
    same territory ID.
    In cases where employees travel to other sites for work, some
    relationships can be considered many-to-many, where many employees
    can be assigned to multiple territory IDs.

Q2: What is a situation where a document store (like MongoDB) is
    appropriate, and what is a situation where it is not appropriate?

A2: Using a document store like MongoDB would be appropriate to use when
    a lot of data with low transaction value needs to be stored. Because
    of its horizontal scalability and key indexing, MongoDB makes data
    readily available with high performance. One would not use MongoDB
    with financial transactions, so banks and other financial institutions
    would use another type of data store.

Q3: What is "NewSQL", and what is it trying to achieve?

A3: NewSQL is a type of relational database that combines scalability of
    NoSQL systems with the ability of processing online transactions
    within ACID standards of traditional database systems. The shortcoming
    to process financial transactions discussed with MongoDB would be
    remediated with NewSQL while still utilizing its scalability benefits.
    It is trying to achieve higher availability and scalability with better
    consistency to increase profits for whichever institution chooses to
    utilize it.
"""
