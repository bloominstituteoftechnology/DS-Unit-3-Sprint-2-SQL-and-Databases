#!/usr/bin/env python
""" Unit3 Sprint2 Challenge - Northwind
"""

import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


curs.execute("""SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice
             DESC LIMIT 10;""")
results1 = curs.fetchall()
print(results1)
# [('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79),
# ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81),
# ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55),
# ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3),
# ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]


curs.execute("""SELECT avg(HireDate - BirthDate) AS AverageAge
             FROM Employee;""")
results2 = curs.fetchall()
print(results2)
# [(37.22222222222222,)] Average age of employees at the hire date


curs.execute("""SELECT City, avg(HireDate - BirthDate) AS AverageAGE
             FROM Employee GROUP BY City ORDER BY AverageAGE;""")
results3 = curs.fetchall()
print(results3)
# [('Kirkland', 29.0), ('London', 32.5), ('Seattle', 40.0),
# ('Tacoma', 40.0), ('Redmond', 56.0)]


curs.execute("""SELECT CompanyName,ProductName, UnitPrice FROM Product AS p,
             Supplier AS sup WHERE p.SupplierId = sup.Id ORDER BY UnitPrice
             DESC LIMIT 10;""")
results4 = curs.fetchall()
print(results4)
# [('Aux joyeux ecclésiastiques', 'Côte de Blaye', 263.5),
# ('Plutzer Lebensmittelgroßmärkte AG', 'Thüringer Rostbratwurst', 123.79),
# ('Tokyo Traders', 'Mishi Kobe Niku', 97), ('Specialty Biscuits, Ltd.',
# "Sir Rodney's Marmalade", 81), ('Pavlova, Ltd.', 'Carnarvon Tigers', 62.5),
# ('Gai pâturage', 'Raclette Courdavault', 55), ("G'day, Mate",
# 'Manjimup Dried Apples', 53), ("Forêts d'érables", 'Tarte au sucre', 49.3),
# ('Leka Trading', 'Ipoh Coffee', 46), ('Plutzer Lebensmittelgroßmärkte AG',
# 'Rössle Sauerkraut', 45.6)]


curs.execute("""SELECT cat.CategoryName, Count(p.Id)as NumberOfProducts
             FROM Product AS p, Category AS cat WHERE cat.Id = p.CategoryId
             GROUP BY cat.CategoryName ORDER BY NumberOfProducts DESC
             LIMIT 1;""")
results5 = curs.fetchall()
print(results5)
# [('Confections', 13)] The max category is Confections which has 13 products


curs.execute("""SELECT FirstName, LastName, et.EmployeeId, Count(TerritoryId)
             AS NumberOfTerritories FROM Employee AS emp, EmployeeTerritory
             AS et WHERE emp.Id = et.EmployeeId GROUP BY et.EmployeeId
             ORDER BY NumberOfTerritories DESC LIMIT 1;""")
results6 = curs.fetchall()
print(results6)
# [('Robert', 'King', 7, 10)] max territories is 10 by employeeID 7 Robert King


curs.close()
CONN.close()
