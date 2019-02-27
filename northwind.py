# PART 2
import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?

curs.execute("SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;")
curs.fetchall()

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)

curs.execute("""SELECT Id, AVG(HireDate - BirthDate) AS AvgAge FROM Employee GROUP BY Id;""")
curs.fetchall()

# (Stretch) `Who's the employee with the most territories?`


# PART 3
#What are the ten most expensive items (per unit price) in the database and their suppliers?

curs.execute("""SELECT ProductName, CompanyName FROM Product, Supplier WHERE Product.SupplierId = Supplier.Id ORDER BY UnitPrice DESC LIMIT 10;""")
curs.fetchall()

#What is the largest category (by number of products in it)?

curs.execute("""SELECT COUNT(CategoryId) as Total_Items, CategoryName FROM Product, Category WHERE Product.CategoryId = Category.Id GROUP BY CategoryName ORDER BY Total_Items DESC LIMIT 1;""")
curs.fetchall()

#(Stretch) What is the top territory (by number of employees), and how many employees does it have?

