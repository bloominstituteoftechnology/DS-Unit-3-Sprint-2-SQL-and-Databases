import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect('northwind_small.sqlite3')
cursor = connection.cursor()

# Ten most expensive items (per unit price) in the database?
most_expensive = """SELECT ProductName, UnitPrice, SupplierId
                    FROM Product
                    ORDER BY UnitPrice DESC
                    LIMIT 10"""

cursor.execute(most_expensive)
cursor.fetchall()

# Largest category by number of products
largest_category = """SELECT Category.CategoryName, COUNT(Product.ProductName)
                      FROM Category, Product
                      WHERE Category.Id = Product.CategoryId
                      GROUP BY Product.CategoryId
                      ORDER BY COUNT(Product.ProductName) DESC
                      LIMIT 1"""

cursor.execute(largest_category)
cursor.fetchone()[0]

# Average age of an employee
average_age = """SELECT city, AVG(HireDate - Birthdate)
                 FROM Employee
                 GROUP BY City"""

cursor.execute(average_age)
cursor.fetchall()