import sqlite3


# Connect to sqlite3 file
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Get names of table in database
print(curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall())

# What are the ten most expensive items (per unit price) in the database?
"""[('Côte de Blaye',),
 ('Thüringer Rostbratwurst',),
 ('Mishi Kobe Niku',),
 ("Sir Rodney's Marmalade",),
 ('Carnarvon Tigers',),
 ('Raclette Courdavault',),
 ('Manjimup Dried Apples',),
 ('Tarte au sucre',),
 ('Ipoh Coffee',),
 ('Rössle Sauerkraut',)]"""
print(curs.execute("""
SELECT ProductName, SupplierId
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;""").fetchall())

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
# 37.22 years old
print(curs.execute("""
SELECT AVG(age)
FROM (
SELECT HireDate-BirthDate AS age
FROM Employee
GROUP BY Id);""").fetchall())

# (Stretch) How does the average age of employee at hire vary by city?
"""[('Kirkland', 29.0),
 ('London', 32.5),
 ('Redmond', 56.0),
 ('Seattle', 40.0),
 ('Tacoma', 40.0)]"""
print(curs.execute("""
SELECT City, AVG(age)
FROM (
SELECT City, HireDate-BirthDate AS age
FROM Employee
GROUP BY Id)
GROUP BY City;""").fetchall())

# What are the ten most expensive items (per unit price) in the database and their suppliers?
"""[('Côte de Blaye', 'Aux joyeux ecclésiastiques'),
 ('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG'),
 ('Mishi Kobe Niku', 'Tokyo Traders'),
 ("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'),
 ('Carnarvon Tigers', 'Pavlova, Ltd.'),
 ('Raclette Courdavault', 'Gai pâturage'),
 ('Manjimup Dried Apples', "G'day, Mate"),
 ('Tarte au sucre', "Forêts d'érables"),
 ('Ipoh Coffee', 'Leka Trading'),
 ('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]"""
print(curs.execute("""
SELECT ProductName, CompanyName
FROM Supplier, (
SELECT ProductName, SupplierId
FROM Product
ORDER BY UnitPrice DESC)
WHERE Id=SupplierId
LIMIT 10;""").fetchall())

# What is the largest category (by number of unique products in it)?
# Category: Confections (13 unique products)
"""[('Confections', 13)]"""
print(curs.execute("""
SELECT CategoryName, MAX(cat_id_count)
FROM Category, (
SELECT CategoryId, COUNT(CategoryId) AS cat_id_count
FROM Product
GROUP BY CategoryId)
WHERE Id=CategoryId;""").fetchall())

# (Stretch) Who's the employee with the most territories?
# Robert King with 10 territories
"""[('King', 'Robert', 10)]"""
print(curs.execute("""
SELECT LastName, FirstName, MAX(terri_id_count)
FROM Employee, (
SELECT EmployeeId, COUNT(TerritoryID) AS terri_id_count
FROM EmployeeTerritory
GROUP BY EmployeeId)
WHERE EmployeeId=Id;""").fetchall())
