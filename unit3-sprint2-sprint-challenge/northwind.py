import sqlite3

""" Connect to northwind_small.sqlite3 database """
conn = sqlite3.connect('northwind_small.sqlite3')

""" Make a cursor to read database """
curs = conn.cursor()
conn.commit()

"""### Part 2 - The Northwind Database"""

""" What are the ten most expensive items (per unit price) in the database? """
print(curs.execute('SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;').fetchall())

""" What is the average age of an employee at the time of their hiring? """
print(curs.execute('SELECT ROUND(AVG(HireDate - BirthDate), 2)FROM Employee;').fetchone())

"""(Stretch) How does the average age of employee at hire vary by city?"""
print(curs.execute('SELECT City, AVG(HireDate - BirthDate) FROM Employee GROUP BY City;').fetchall())

conn.commit()

"""### Part 3 - Sailing the Northwind Seas"""

""" What are the ten most expensive items (per unit price) in the database and their suppliers? """
print(curs.execute('SELECT Product.ProductName, Product.UnitPrice ,Supplier.CompanyName FROM Supplier INNER JOIN Product ON SupplierID ORDER BY UnitPrice DESC LIMIT 10;').fetchall())

""" What is the largest category (by number of unique products in it)? """
print(curs.execute('SELECT CategoryID, COUNT(Product.ProductName) FROM Category INNER JOIN Product ON CategoryID GROUP BY CategoryID ORDER BY COUNT(Product.ProductName) DESC LIMIT 1;').fetchone())

conn.commit()
