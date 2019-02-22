# connecting northwind_small.sqlite3 file
import sqlite3
conn = sqlite3.connect(
    '/home/mishraka/repos/manjulamishra/northwind_small.sqlite3')

# create a cursor
curs = conn.cursor()

curs.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
 ('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
 ('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
 ('Territory',)]

curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
[('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n "CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n "ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City" VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode" VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000) NULL, \n  "Fax" VARCHAR(8000) NULL \n)')]


# Question 1What are the ten most expensive
# items (per unit price) in the database?
most_expensive = """SELECT Id, ProductName, UnitPrice

FROM Product 
ORDER BY UnitPrice DESC LIMIT 10;"""
curs.execute(most_expensive)
print(curs.fetchall())


# Q2 What is the average age of an employee at the time of their hiring?
# (Hint: a lot of arithmetic works with dates.)
avg_age = """SELECT AVG(strftime('%Y', date('now'))-strftime('%Y', Employee.BirthDate) )
FROM Employee;"""
curs.execute(avg_age)
print(curs.fetchall())

# (Stretch) How does the average age of employee at hire vary by city?
avg_age = """SELECT City,
AVG(strftime('%Y', date('now'))-strftime('%Y', Employee.BirthDate) )
FROM Employee
GROUP BY Employee.City;
"""
curs.execute(avg_age)
print(curs.fetchall())

# What are the ten most expensive items (per unit price) in the database
# and their suppliers?
most_expensive = """SELECT Product.Id, ProductName, UnitPrice, Supplier.CompanyName
FROM Product, Supplier WHERE Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC LIMIT 10;"""
curs.execute(most_expensive)
print(curs.fetchall())

#  What is the largest category (by number of products in it)?

largest_category = """SELECT Category.Id, 
COUNT(Product.CategoryId)
FROM  Category, Product
WHERE Category.Id = Product.CategoryId
GROUP BY Product.CategoryId;"""
curs.execute(largest_category)
print(curs.fetchall())
