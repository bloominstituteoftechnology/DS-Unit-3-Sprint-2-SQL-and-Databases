import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

curs.execute(''' SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;''')
print('10 most expensive items:')
print(curs.fetchall())
'''
[('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]
'''
curs.execute('''SELECT AVG(HireDate - BirthDate) FROM Employee;''')
print('Average Employee Age at hire: ')
print(curs.fetchall())
'''
Average Employee Age at hire: 
[(37.22222222222222,)]
'''
# Stretch Goal: Average hire age by city
print('Average hire age by city')
curs.execute('''SELECT City, AVG(HireDate - BirthDate) FROM Employee GROUP BY City;''')
print(curs.fetchall())
'''
Average hire age by city
[('Kirkland', 29.0), ('London', 32.5), ('Redmond', 56.0), ('Seattle', 40.0), ('Tacoma', 40.0)]
'''
# What are the ten most expensive items (per unit price) in the database *and* their suppliers?
curs.execute('''SELECT ProductName, UnitPrice, CompanyName FROM Product LEFT JOIN Supplier ORDER BY UnitPrice DESC LIMIT 10;''')
print('10 Most Expensive Items With Company Name')
print(curs.fetchall())
'''
10 Most Expensive Items With Company Name
[('Côte de Blaye', 263.5, 'Exotic Liquids'), ('Côte de Blaye', 263.5, 'New Orleans Cajun Delights'), ('Côte de Blaye', 263.5, "Grandma Kelly's Homestead"), ('Côte de Blaye', 263.5, 'Tokyo Traders'), ('Côte de Blaye', 263.5, "Cooperativa de Quesos 'Las Cabras'"), ('Côte de Blaye', 263.5, "Mayumi's"), ('Côte de Blaye', 263.5, 'Pavlova, Ltd.'), ('Côte de Blaye', 263.5, 'Specialty Biscuits, Ltd.'), ('Côte de Blaye', 263.5, 'PB Knäckebröd AB'), ('Côte de Blaye', 263.5, 'Refrescos Americanas LTDA')]
'''
# What is the largest category (by number of unique products in it)?
print('Category with the Most Items: ')
curs.execute('''SELECT CategoryName, COUNT(ProductName) FROM Product INNER JOIN Category ON Product.CategoryID=Category.ID GROUP BY CategoryID ORDER BY COUNT(CategoryID) DESC LIMIT 1;''')
print(curs.fetchall())
'''
Category with the Most Items: 
[('Confections', 13)]
'''
# Who is the employee with the most territories
print('Employee with the most territories:')
curs.execute('''SELECT FirstName, LastName, COUNT(TerritoryID) FROM Employee INNER JOIN EmployeeTerritory ON Employee.ID=EmployeeTerritory.EmployeeID GROUP BY Employee.ID ORDER BY COUNT(TerritoryID) DESC LIMIT 1;''')
print(curs.fetchall())
'''
Employee with the most territories:
[('Robert', 'King', 10)]
'''