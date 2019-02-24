#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sql

db = sql.connect("demo_data.sqlite3")


cursor = db.cursor()


db.execute("DROP TABLE demo")


t = db.execute(
    """
    CREATE TABLE demo(
      s TEXT,
      x INTEGER,
      y INTEGER
    )
    """
)


cursor.executemany(
    """
    INSERT INTO demo (s,x,y) VALUES(?,?,?)
    """,
    [
        ('s', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)
    ]
)


print(f'rows: {db.execute("SELECT COUNT(*) FROM demo").fetchone()[0]}')
# rows: 3

c = db.execute(
    "SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5").fetchone()[0]
print(f'number of x,y >= 5: {c}')
# number of x,y >= 5: 2


c = db.execute("SELECT COUNT(DISTINCT y) FROM demo").fetchone()[0]
print(f"How many unique values of `y` are there: {c}")
# How many unique values of `y` are there: 2


db = sql.connect('northwind_small.sqlite3')

c = db.execute(
    """
    SELECT p.ProductName FROM Product p ORDER BY p.UnitPrice LIMIT 10
    """
).fetchall()

print(
    f"What are the ten most expensive items (per unit price) in the database? {c}")

# What are the ten most expensive items (per unit price) in the database? [('Geitost',), ('Guaraná Fantástica',), ('Konbu',), ('Filo Mix',), ('Tourtière',), ('Rhönbräu Klosterbier',), ('Tunnbröd',), ('Teatime Chocolate Biscuits',), ('Rogede sild',), ('Zaanse koeken',)]


c = db.execute(
    """
    SELECT AVG(e.HireDate - e.BirthDate) FROM employee e
    """
).fetchone()[0]
print(
    f"What is the average age of an employee at the time of their hiring? {c}")
# What is the average age of an employee at the time of their hiring? 37.22222222222222


c = db.execute(
    """
    SELECT AVG(e.HireDate - e.BirthDate), City from employee e GROUP BY e.City
    """
).fetchall()

print(
    f"(*Stretch*) How does the average age of employee at hire vary by city? {c}")
# (*Stretch*) How does the average age of employee at hire vary by city? [(29.0, 'Kirkland'), (32.5, 'London'), (56.0, 'Redmond'), (40.0, 'Seattle'), (40.0, 'Tacoma')]


c = db.execute(
    """
    SELECT p.ProductName, s.CompanyName  FROM PRODUCT p JOIN Supplier s ON p.SupplierId = s.Id ORDER BY p.UnitPrice LIMIT 10
    """
).fetchall()
print(
    f"What are the ten most expensive items (per unit price) in the database *and* their suppliers? {c}")
# What are the ten most expensive items (per unit price) in the database *and* their suppliers? [('Geitost', 'Norske Meierier'), ('Guaraná Fantástica', 'Refrescos Americanas LTDA'), ('Konbu', "Mayumi's"), ('Filo Mix', "G'day, Mate"), ('Tourtière', 'Ma Maison'), ('Rhönbräu Klosterbier', 'Plutzer Lebensmittelgroßmärkte AG'), ('Tunnbröd', 'PB Knäckebröd AB'), ('Teatime Chocolate Biscuits', 'Specialty Biscuits, Ltd.'), ('Rogede sild', 'Lyngbysild'), ('Zaanse koeken', 'Zaanse Snoepfabriek')]

c = db.execute(
    """
    SELECT COUNT(*) AS Result FROM Product p GROUP BY p.CategoryId
    order by Result desc
    limit 1
    """
).fetchone()[0]

print(f"What is the largest category (by number of products in it?) {c}")
# What is the largest category (by number of products in it?) 13


c = db.execute(
    """
    SELECT t.TerritoryDescription,  COUNT(*) as Employees FROM employee AS e 
    JOIN EmployeeTerritory AS et ON e.Id = et.EmployeeId
    JOIN Territory t ON t.Id = et.TerritoryId
    GROUP BY et.EmployeeId
    ORDER BY Employees DESC
    LIMIT 1
    """
).fetchall()


print(
    f"(*Stretch*) What is the top territory (by number of employees), and how many employees do they have? {c}")
# (*Stretch*) What is the top territory (by number of employees), and how many employees do they have? [('Hoffman Estates', 10)]

c = db.execute(
    """
    SELECT  e.FirstName, e.LastName,  COUNT(*) as TID FROM employee AS e JOIN EmployeeTerritory AS et ON e.Id = et.EmployeeId
    JOIN Territory t ON t.Id = et.TerritoryId
    GROUP BY e.ID
    ORDER BY TID desc
    """
).fetchone()

print(
    f"Stretch #2 Who's the employee with the most territories? {c[0]} {c[1]}  {c[2]} Territories")
# Stretch #2 Who's the employee with the most territories? Robert King  10 Territories


# - In the Northwind database, what is the type of relationship between the
#   `Employee` and `Territory` tables?
# *  One to Many. There can be many  Territories for an Employees but each Territory has only one Employee.
# - What is a situation where a document store (like MongoDB) is appropriate, and
#   what is a situation where it is not appropriate?
# *  MongoDB is appropriate where a document per id is appropriate or there are unknown or varying schema. Because of document storage MongoDB can be extended (sharding) more easily, there isn't the dependence on shared tables that RDBMS has.   If the schema is known and fixed RDBMS can be faster.   There are many choices of RDBMS tools but only a limited of document storage choices
# - (*Stretch*) What is "NewSQL", and what is it trying to achieve?
# NewSQL is adding ACID (Atomicity, Consistency, Isolation, Durability) to nosql databases. Part of that is adding Transactions that do nothing to the database for failures and that can also be rolled back if necessary.
#
