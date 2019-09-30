import sqlite3

# Part 2 - The Northwind Database

# Connect to database (small version).
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Find ten most expensive items by unit price.
print('What are the ten most expensive items (per unit price) in the '
      'database?')
curs.execute('SELECT Id, ProductName, UnitPrice '
             'FROM Product '
             'ORDER BY UnitPrice DESC '
             'LIMIT 10;')
print('\n'.join([str(row) for row in curs]), '\n')
# (38, 'Côte de Blaye', 263.5)
# (29, 'Thüringer Rostbratwurst', 123.79)
# (9, 'Mishi Kobe Niku', 97)
# (20, "Sir Rodney's Marmalade", 81)
# (18, 'Carnarvon Tigers', 62.5)
# (59, 'Raclette Courdavault', 55)
# (51, 'Manjimup Dried Apples', 53)
# (62, 'Tarte au sucre', 49.3)
# (43, 'Ipoh Coffee', 46)
# (28, 'Rössle Sauerkraut', 45.6)

# Find average employee age at time of hire.
print('What is the average age of an employee at the time of their hiring? '
      '(Hint: a lot of arithmetic works with dates.)')
curs.execute('SELECT AVG((JULIANDAY(HireDate)-JULIANDAY(Birthdate))/365.25) '
             'FROM Employee;')
print(curs.fetchall(), '\n')
# [(37.28344360787892,)]

# Check: What numbers do different methods of calculating the hire age yield?
curs.execute('SELECT BirthDate, HireDate, HireDate - BirthDate, '
             '(strftime("%Y", HireDate) - strftime("%Y", BirthDate)) - '
             '(strftime("%m-%d", HireDate) < strftime("%m-%d", BirthDate)), '
             '(julianday(HireDate)-julianday(Birthdate))/365.25 '
             'FROM Employee;')
print('\n'.join([str(row) for row in curs]), '\n')
# ('1980-12-08', '2024-05-01', 44, 43, 43.39493497604381)
# ('1984-02-19', '2024-08-14', 40, 40, 40.48459958932238)
# ('1995-08-30', '2024-04-01', 29, 28, 28.588637919233403)
# ('1969-09-19', '2025-05-03', 56, 55, 55.619438740588635)
# ('1987-03-04', '2025-10-17', 38, 38, 38.62286105407255)
# ('1995-07-02', '2025-10-17', 30, 30, 30.2943189596167)
# ('1992-05-29', '2026-01-02', 34, 33, 33.596167008898014)
# ('1990-01-09', '2026-03-05', 36, 36, 36.15058179329227)
# ('1998-01-27', '2026-11-15', 28, 28, 28.799452429842574)

# Calculate average employee age at hire data by city.
print('(Stretch) How does the average age of employee at hire vary by city?')
curs.execute('SELECT City, '
             'AVG((JULIANDAY(HireDate)-JULIANDAY(Birthdate))/365.25) '
             'FROM Employee '
             'GROUP BY City;')
print('\n'.join([str(row) for row in curs]), '\n')
# ('Kirkland', 28.588637919233403)
# ('London', 32.82819986310746)
# ('Redmond', 55.619438740588635)
# ('Seattle', 39.77275838466804)
# ('Tacoma', 40.48459958932238)

# Part 3 - Sailing the Northwind Seas

#  Match the 10 most expensive items by unit price with their suppliers.
print('What are the ten most expensive items (per unit price) in the '
      'database and their suppliers?')
curs.execute('SELECT Supplier.Id, CompanyName, top10.Id, ProductName, '
             'UnitPrice FROM '
             '(SELECT Id, SupplierID, ProductName, UnitPrice '
             'FROM Product '
             'ORDER BY UnitPrice DESC '
             'LIMIT 10) AS top10 '
             'JOIN Supplier ON top10.SupplierId = Supplier.Id;')
print('\n'.join([str(row) for row in curs]), '\n')
# (18, 'Aux joyeux ecclésiastiques', 38, 'Côte de Blaye', 263.5)
# (12, 'Plutzer Lebensmittelgroßmärkte AG', 29, 'Thüringer Rostbratwurst',
# 123.79)
# (4, 'Tokyo Traders', 9, 'Mishi Kobe Niku', 97)
# (8, 'Specialty Biscuits, Ltd.', 20, "Sir Rodney's Marmalade", 81)
# (7, 'Pavlova, Ltd.', 18, 'Carnarvon Tigers', 62.5)
# (28, 'Gai pâturage', 59, 'Raclette Courdavault', 55)
# (24, "G'day, Mate", 51, 'Manjimup Dried Apples', 53)
# (29, "Forêts d'érables", 62, 'Tarte au sucre', 49.3)
# (20, 'Leka Trading', 43, 'Ipoh Coffee', 46)
# (12, 'Plutzer Lebensmittelgroßmärkte AG', 28, 'Rössle Sauerkraut', 45.6)

# Find the category with the greatest number of unique products.
# We don't need the DISTINCT keyword, because we're working with a primary key.
# This one could also be done with MAX and a subquery.
print('What is the largest category (by number of unique products in it)?')
curs.execute('SELECT CategoryID, CategoryName, '
             'COUNT(Product.ID) AS numProducts '
             'FROM Category LEFT OUTER JOIN Product ON '
             'Product.CategoryID = Category.Id '
             'GROUP BY CategoryID, CategoryName '
             'ORDER BY numProducts DESC '
             'LIMIT 1;')
print(curs.fetchall(), '\n')
# [(3, 'Confections', 13)]

# Find the employee with the most territories.
print('(Stretch) Who\'s the employee with the most territories? Use '
      'TerritoryId (not name, region, or other fields) as the unique '
      'identifier for territories.')
curs.execute('SELECT Employee.Id, Title, FirstName, LastName, numTerritories '
             'FROM '
             '(SELECT EmployeeID, COUNT(TerritoryID) as numTerritories '
             'FROM EmployeeTerritory '
             'GROUP BY EmployeeID '
             'ORDER BY numTerritories DESC '
             'LIMIT 1) '
             'JOIN Employee ON EmployeeID = Employee.Id;')
print(curs.fetchall(), '\n')
# [(7, 'Sales Representative', 'Robert', 'King', 10)]

conn.close()
