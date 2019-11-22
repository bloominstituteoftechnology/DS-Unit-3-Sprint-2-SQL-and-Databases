import sqlite3


conn = sqlite3.connect('/Users/ericchiyembekeza/Desktop/Lambda School/DS-Unit-3-Sprint-2-SQL-and-Databases/northwind_small.sqlite3')
curs = conn.cursor()

print('What are the ten most expensive items (per unit price) in the database?')
q1 = 'SELECT  ProductName, UnitPrice FROM Product Order by UnitPrice DESC LIMIT 10;'
print(curs.execute(q1).fetchall())
"""[('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81),
('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3),
('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]"""


print('What is the average age of an employee at the time of their hiring?')
q2 = 'SELECT avg(HireDate - BirthDate) AS AverageAge FROM Employee;'
print(curs.execute(q2).fetchall())
"""37.2222222222222222"""

print('How does the average age of employee at hire vary by city?')
q3 = 'SELECT City, avg(HireDate - BirthDate) AS AverageAGE FROM Employee GROUP BY City;'
print(curs.execute(q3).fetchall())
"""[('Kirkland', 29.0), ('London', 32.5), ('Redmond', 56.0), ('Seattle', 40.0), ('Tacoma', 40.0)]"""



print('What are the ten most expensive items (per unit price) in the database and their suppliers?')
q4 = 'SELECT CompanyName, ProductName, UnitPrice FROM Product P, Supplier S WHERE P.SupplierId = S.Id ORDER BY UnitPrice DESC LIMIT 10;'
print(curs.execute(q4).fetchall())
"""[('Aux joyeux ecclésiastiques', 'Côte de Blaye', 263.5), ('Plutzer Lebensmittelgroßmärkte AG', 'Thüringer Rostbratwurst', 123.79), ('Tokyo Traders', 'Mishi Kobe Niku', 97), ('Specialty Biscuits, Ltd.', "Sir Rodney's Marmalade", 81), ('Pavlova, Ltd.', 'Carnarvon Tigers', 62.5), ('Gai pâturage', 'Raclette Courdavault', 55), ("G'day, Mate", 'Manjimup Dried Apples', 53), ("Forêts d'érables", 'Tarte au sucre', 49.3), ('Leka Trading', 'Ipoh Coffee', 46), ('Plutzer Lebensmittelgroßmärkte AG', 'Rössle Sauerkraut', 45.6)]"""


print('What is the largest category (by number of unique products in it)?')
q5 = 'SELECT C.CategoryName, count(P.Id) from Product P, Category C WHERE C.Id = P.CategoryId GROUP BY C.CategoryName ORDER BY count(P.Id) DESC LIMIT 1'
print(curs.execute(q5).fetchall())
"""[('Confections', 13)]"""
