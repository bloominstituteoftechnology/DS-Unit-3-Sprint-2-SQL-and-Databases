import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

curs.execute(''' SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;''')
print('10 most expensive items:')
print(curs.fetchall())

curs.execute('''SELECT AVG(HireDate - BirthDate) FROM Employee;''')
print('Average Employee Age at hire: ')
print(curs.fetchall())

# Stretch Goal: Average hire age by city


# What are the ten most expensive items (per unit price) in the database *and* their suppliers?
curs.execute('''SELECT ProductName, UnitPrice, CompanyName FROM Product LEFT JOIN Supplier ORDER BY UnitPrice DESC LIMIT 10;''')
print('10 Most Expensive Items With Company Name')
print(curs.fetchall())

# What is the largest category (by number of unique products in it)?
curs.execute('''SELECT CategoryName, COUNT(CategoryName) FROM Product LEFT JOIN Category GROUP BY CategoryName LIMIT 5;''')
print(curs.fetchall())