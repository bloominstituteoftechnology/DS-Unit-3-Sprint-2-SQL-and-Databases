# connecting northwind_small.sqlite3 file
import sqlite3
conn = sqlite3.connect(
    '/home/mishraka/repos/manjulamishra/northwind_small.sqlite3')

# create a cursor
curs = conn.cursor()


# Question 1What are the ten most expensive
# items (per unit price) in the database?
most_expensive = """SELECT Id, ProductName, UnitPrice
FROM Product ORDER BY UnitPrice DESC LIMIT 10;"""
curs.execute(most_expensive)
print(curs.fetchall())


# Q2 What is the average age of an employee at the time of their hiring?
# (Hint: a lot of arithmetic works with dates.)
avg_age = """SELECT AVG(HireDate - BirthDate)
From Employee;"""
curs.execute(avg_age)
print(curs.fetchall())

# (Stretch) How does the average age of employee at hire vary by city?
avg_age = """SELECT City, AVG(HireDate-BirthDate)
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

largest_category = """SELECT Category.Id, COUNT(Product.CategoryId)
FROM  Category, Product
WHERE Category.Id = Product.CategoryId
GROUP BY Product.CategoryId;"""
curs.execute(largest_category)
print(curs.fetchall())
