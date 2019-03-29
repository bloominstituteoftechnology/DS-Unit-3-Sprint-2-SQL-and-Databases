import sqlite3

conn = sqlite3.connect('/Users/shilpasingh/Downloads/northwind_small.sqlite3')
curs = conn.cursor()

print('What are the ten most expensive items (per unit price) in the database?')
query1 = """
SELECT  ProductName, UnitPrice FROM Product
Order by UnitPrice DESC
LIMIT 10;
"""
print(curs.execute(query1).fetchall())

print('What is the average age of an employee at the time of their hiring?')
query2 = """
SELECT avg(HireDate - BirthDate) AS AverageAge
FROM Employee;
"""
print(curs.execute(query2).fetchall())

print('How does the average age of employee at hire vary by city?')
query3 = """
SELECT City, avg(HireDate - BirthDate) AS AverageAGE
FROM Employee GROUP BY City;
"""
print(curs.execute(query3).fetchall())

print('What are the ten most expensive items (per unit price) in the database and their suppliers?')
query4 = """
SELECT CompanyName,ProductName, UnitPrice FROM Product P,
Supplier S WHERE P.SupplierId = S.Id ORDER BY UnitPrice
DESC LIMIT 10;
"""
print(curs.execute(query4).fetchall())

print('What is the largest category (by number of unique products in it)?')
query5 = """
SELECT C.CategoryName, count(P.Id) from Product P, Category C
where C.Id = P.CategoryId
GROUP BY C.CategoryName
ORDER BY count(P.Id) DESC
LIMIT 1
"""
print(curs.execute(query5).fetchall())

print('Whos the employee with the most territories?')


