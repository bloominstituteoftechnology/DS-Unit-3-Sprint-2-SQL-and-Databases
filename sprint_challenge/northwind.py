"""
You can see all the tables available to SQLite as follows:
"""
# curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY
# name;").fetchall()
# [('Category',), ('Customer',), ('CustomerCustomerDemo',),
# ('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
# ('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
# ('Territory',)]
"""
Warning: unlike the diagram, the tables in SQLite are singular and not plural (do not end in s).
And you can see the schema (CREATE TABLE statement) behind any given table with:
"""
# curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
# [('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n
# "CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n
# "ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"
# VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"
# VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000)
# NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]

# import sqlite3

# open a connection to the nw database. SQL queries must be done in text
# also creating cursor
import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
r = conn.cursor()


# What are the ten most expensive items (per unit price) in the database?
q1 = ''' SELECT ProductName, UnitPrice, CompanyName FROM Product
LEFT JOIN Supplier ON SupplierID
ORDER BY UnitPrice DESC LIMIT 10;
'''
q1a = r.execute(q1).fetchall()
# What is the average age of an employee at the time of their hiring?
# (Hint: a lot of arithmetic works with dates.)

print(r.execute("""SELECT AVG(HireDate - BirthDate) from Employee;""").fetchall())

# PART 3
print(r.execute("""SELECT Category.CategoryName, COUNT(distinct Product.Id) \
FROM Product \
INNER JOIN Category on Product.CategoryID=Category.Id \
ORDER BY count(distinct Product.Id) DESC \
LIMIT 1;""").fetchall())

# print 10 most expensive products and their respective suppliers
print(r.execute("""SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName \
FROM Product \
INNER JOIN Supplier on Product.SupplierID=Supplier.Id \
ORDER BY UnitPrice DESC \
limit 10;""").fetchall())

# print the name of the category with the most products
print(r.execute("""SELECT Category.CategoryName, COUNT(DISTINCT Product.Id)\
FROM Product INNER JOIN Category on Product.CategoryID=Category.Id \
ORDER BY count(distinct Product.Id) DESC LIMIT 1;""").fetchall())

conn.commit()
conn.close
