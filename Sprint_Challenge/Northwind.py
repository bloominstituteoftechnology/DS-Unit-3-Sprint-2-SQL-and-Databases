import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Question 1
q1 = curs.execute("""
SELECT ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
""").fetchall()
print("The ten most expensive items (per unite price) in the database are: ", q1)


# Question 2
q2 = curs.execute("""
SELECT AVG(HireDate - BirthDate) from Employee
""").fetchall()
print("The average age of an employee at the time of their hiring is: ", q2)

# Part 3 Question 1

p3q1 = curs.execute("""
SELECT Supplier.CompanyName AS Supplier, Product.ProductName AS ProductName , Product.UnitPrice as UnitPrice
FROM Product JOIN Supplier
ON Product.SupplierID = Supplier.ID
ORDER BY UnitPrice DESC
LIMIT 10;
""").fetchall()

print("The ten most expensive items (per unit price) and their suppliers are: ", p3q1)

p3q2 = curs.execute("""
SELECT Category.CategoryName, COUNT(DISTINCT Product.ProductName) as unique_prod
FROM Product JOIN Category
WHERE Product.CategoryID = Category.ID
ORDER BY unique_prod DESC
""").fetchall()[0][0]

print("The largest category by number of unique products is: ", p3q2)