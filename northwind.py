import sqlite3 

conn = sqlite3.connect('C:\\users\\cris\\Documents\\northwind_small.sqlite3')
curs = conn.cursor() 

q1 = """ 
SELECT ProductName 
FROM Product 
ORDER BY UnitPrice 
DESC LIMIT 10; 
"""

q2 = """ 
SELECT AVG (HireDate-Birthdate) FROM Employee;
"""
q3 = """
SELECT AVG (HireDate-Birthdate) FROM Employee GROUP BY City;
"""

q4 = """
SELECT ProductName, CompanyName 
FROM Product 
INNER JOIN Supplier 
ON Product.SupplierId = Supplier.Id 
ORDER BY UnitPrice DESC 
LIMIT 10;
""" 

q5 = """ 
SELECT Category.CategoryName, COUNT(*)
FROM Product 
JOIN Category
ON Category.Id = Product.CategoryId
GROUP BY CategoryId
ORDER BY COUNT(DISTINCT ProductName) DESC
LIMIT 1;
""" 

curs1 = conn.cursor() 
print('10 most expensive items:', curs1.execute(q1).fetchall())

curs2 = conn.cursor() 
print('Avg age of employee on hiredate:', curs2.execute(q2).fetchall())

curs3 = conn.cursor()
print('Avg age of employee on hiredate by city:', curs3.execute(q3).fetchall())

curs4 = conn.cursor() 
print('10 most expensive items and their suppliers:', curs4.execute(q4).fetchall())

curs5 = conn.cursor() 
print('Largest category by unique products:', curs5.execute(q5).fetchall())

conn.commit()
