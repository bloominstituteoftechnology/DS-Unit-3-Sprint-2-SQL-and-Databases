import sqlite3

connect = sqlite3.connect('northwind_small.sqlite3')
curs= connect.cursor()
query ="SELECT COUNT(*) FROM Product;"
curs.execute(query).fetchall()
query = 'SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
curs.execute(query).fetchall()
query = 'SELECT AVG(HireDate-BirthDate) FROM Employee;'
curs.execute(query).fetchall()
query = 'SELECT SupplierID, CompanyName, ProductName, UnitPrice FROM Product, Supplier WHERE Product.SupplierID = Supplier.ID ORDER BY UnitPrice DESC LIMIT 10;'
curs.execute(query).fetchall()
query = 'SELECT COUNT(DISTINCT Product.ID) AS Counting, CategoryName FROM Product, Category  WHERE Product.CategoryID = Category.ID GROUP BY CategoryName ORDER BY Counting DESC LIMIT 1;'
curs.execute(query).fetchall()
