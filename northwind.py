import sqlite3

conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
q_1 = 'SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
results_1 = curs.execute(q_1)
print("Top 10 most expensive items:", results_1.fetchall())

# What is the average age of an employee at the time of their hiring?
q_2 = 'SELECT AVG(HireDate - BirthDate) FROM Employee;'
results_2 = curs.execute(q_2)
print("Average age of employee at time of hire:", results_2.fetchall())

# What are the ten most expensive items (per unit price) in the database and their suppliers?
q_3 = """SELECT Product.ProductName, Supplier.CompanyName
FROM Product
LEFT JOIN Supplier
ON Product.ID = Supplier.ID
ORDER BY UnitPrice DESC
LIMIT 10;"""
results_3 = curs.execute(q_3)
print("Top 10 most expensive items and their supplier per unit price:", results_3.fetchall())

# What is the largest category (by number of unique products in it)?
q_4 = """SELECT Category.CategoryName
FROM Category
INNER JOIN Product
ON Product.ID = Category.ID
ORDER BY CategoryId DESC
LIMIT 1;"""
results_4 = curs.execute(q_4)
print("Largest category:", results_4.fetchall())
