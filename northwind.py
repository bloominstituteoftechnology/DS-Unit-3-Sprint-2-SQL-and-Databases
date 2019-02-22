import sqlite3

conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()

one = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC 
LIMIT 10
"""

print(curs.execute(one).fetchall(), "\n")
conn.commit()

two = """
Select AVG(strftime("%Y",hiredate)-strftime("%Y", birthdate) +
round((strftime("%m",hiredate)-strftime("%m", birthdate))/12.0, 2) +
round((strftime("%d",hiredate)-strftime("%d", birthdate))/365.0, 2)) AS precise,
AVG(hiredate-birthdate) as estimate
FROM Employee
"""
print(curs.execute(two).fetchall(), "\n")
conn.commit()


three = """
Select City, AVG(strftime("%Y",hiredate)-strftime("%Y", birthdate) +
round((strftime("%m",hiredate)-strftime("%m", birthdate))/12.0, 2) +
round((strftime("%d",hiredate)-strftime("%d", birthdate))/365.0, 2)) AS precise,
AVG(hiredate-birthdate) as estimate
FROM Employee
GROUP BY City
"""
print(curs.execute(three).fetchall(), "\n")
conn.commit()


four = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
LEFT JOIN Supplier 
on SupplierId = SupplierId
ORDER BY UnitPrice DESC 
LIMIT 10
"""
print(curs.execute(four).fetchall(), "\n")
conn.commit()

five = """
SELECT COUNT(CategoryId)
FROM Product
ORDER BY COUNT(CategoryID) desc
LIMIT 1
"""
print(curs.execute(five).fetchall(), "\n")
conn.commit()

six = """
SELECT employeeId, Count(employeeID) AS cnt
FROM EmployeeTerritory
GROUP BY EmployeeId
ORDER BY cnt DESC
LIMIT 1
"""
print(curs.execute(six).fetchall(), "\n")
conn.commit()

# Answers
# [('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]

# [(37.28666666666667, 37.22222222222222)]

# [('Kirkland', 28.590000000000003, 29.0), ('London', 32.8275, 32.5), ('Redmond', 55.63, 56.0), ('Seattle', 39.78, 40.0), ('Tacoma', 40.49, 40.0)]

# [('Côte de Blaye', 263.5, 'Exotic Liquids'), ('Côte de Blaye', 263.5, 'New Orleans Cajun Delights'), ('Côte de Blaye', 263.5, "Grandma Kelly's Homestead"), ('Côte de Blaye', 263.5, 'Tokyo Traders'), ('Côte de Blaye', 263.5, "Cooperativa de Quesos 'Las Cabras'"), ('Côte de Blaye', 263.5, "Mayumi's"), ('Côte de Blaye', 263.5, 'Pavlova, Ltd.'), ('Côte de Blaye', 263.5, 'Specialty Biscuits, Ltd.'), ('Côte de Blaye', 263.5, 'PB Knäckebröd AB'), ('Côte de Blaye', 263.5, 'Refrescos Americanas LTDA')]

# [(77,)]

# [(7, 10)]
