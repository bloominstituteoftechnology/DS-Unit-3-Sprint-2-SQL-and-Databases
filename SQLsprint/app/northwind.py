
import sqlite3
import os

# Construct a path to where your DB exists 
# if DB IS IN "DATA" DIR AND THIS FILE IS IN THE 'APP' DIR
# DB_FILEPATH = "chinook.db"
# NOw we can run file from anywhere in our directory and also run w/o using '/'
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "northwind_small.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
# connection.row_factory = sqlite3.Row # let's treat our results like object/dict 
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

print("----------")
query = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
result = cursor.execute(query).fetchall()
print("Top 10 Products:", result)

print("-------")
query = """
SELECT LastName,
(HireDate - BirthDate) AS AverageAge
FROM Employee;
"""
result = cursor.execute(query).fetchall()
print("Average age of employee:", result)


print("--------")
query = """
SELECT AVG (HireDate - BirthDate) AS CityAVG
FROM Employee
GROUP BY City;
"""
result = cursor.execute(query).fetchall()
print("Average age of employee by city:", result)


print("------")
query = """
SELECT p.ProductName,s.CompanyName
FROM Product p
ORDER BY UnitPrice DESC
LIMIT 10
LEFT JOIN Supplier AS s ON Product.SupplierId = Supplier.Id
GROUP by s.CompanyName;
"""
result = cursor.execute(query).fetchall()
print("Top 10 items by supplier name:", result)


print("--------")
query = """
SELECT CategoryName, Description
FROM Category
ORDER BY LENGTH(Description) DESC
LIMIT 1;
"""
result = cursor.execute(query).fetchall()
print("Top category:", result)




