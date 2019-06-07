import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
query = 'SELECT ProductName, UnitPrice from Product order by UnitPrice DESC limit 10;'
result = curs.execute(query)
result.fetchall()

# What is the average age of an employee at the time of their hiring?
query = 'SELECT AVG(DATE(HireDate)-DATE(BirthDate)) FROM Employee;'
result = curs.execute(query)
result.fetchall()

# How does the average age of employee at hire vary by city?
query = 'SELECT city, AVG(DATE(HireDate)-DATE(BirthDate)) FROM Employee GROUP BY City;'
result = curs.execute(query)
result.fetchall()

# Part 3 sailing the seas

# What are the ten most expensive items (per unit price) in the database and their suppliers?
query = '''SELECT ProductName, CompanyName FROM Product 
INNER JOIN Supplier ON Product.SupplierId = supplier.Id
ORDER BY UnitPrice DESC limit 10;'''
result = curs.execute(query)
result.fetchall()

# What is the largest category (by number of unique products in it)?
query = '''SELECT ProductName, CompanyName FROM Product 
INNER JOIN Supplier ON Product.SupplierId = supplier.Id
ORDER BY UnitPrice DESC limit 10;'''
result = curs.execute(query)
result.fetchall()

# Who's the employee with the most territories?
query = '''SELECT FirstName, LastName, COUNT(TerritoryId) FROM Employee
INNER JOIN EmployeeTerritory ON EmployeeTerritory.EmployeeId = Employee.Id
GROUP BY EmployeeId ORDER BY COUNT(TerritoryId) DESC;'''
result = curs.execute(query)
result.fetchall()

# Part 4 Questions

# In the Northwind database, what is the type of relationship between
# the Employee and Territory tables?
answer_one = """Well, first of all, it doesn't look like the two tables 
have a direct relationship. The two tables are only connected by a third
table, EmployeeTerritory. Table Employee joins EmployeeTerritory on Id 
EmployeeId while Territory joins EmployeeTerritory on TerritoryId. 
Because one employee can have more than one territory, as I demonstrated 
above, this would be called a many to one relationship where there are 
many territories to one employee."""

# What is a situation where a document store (like MongoDB) is appropriate,
# and what is a situation where it is not appropriate?
answer_two = """SQL databases are highly structured and vertically scalable.
On the other hand, NoSQL databases are flexible and you don't need to predefine
a schema beforehand. A relational SQL database would be more useful to larger companies
because the ease of access to the relative data makes large transactions quicker,
such as in an accounting or banking system. A NoSQL database may be better for a 
tech startup where it may have many different projects that don't need to inherently 
relate but still need one place to be stored.
"""
# What is "NewSQL", and what is it trying to achieve?
answer_three = """NewSQL are subsection of databases that want to combine the ease of access
of SQL (easy queries) with horizontal scalability. If SQL and NoSQL are on the ends of the 
database spectrum, the NewSQL database systems are all points in between. Different types will
give you different levels of access to traditional SQL tooling while giving you NoSQL-style 
clustering. Basically, NewSQL evens the scales by redistributing the weights. 
"""