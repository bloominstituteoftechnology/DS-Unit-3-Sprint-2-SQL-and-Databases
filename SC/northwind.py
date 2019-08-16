import sqlite3


# Connect to sqlite3 file
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Get names of table in database
print(curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall())
"""[('Category',),
 ('Customer',),
 ('CustomerCustomerDemo',),
 ('CustomerDemographic',),
 ('Employee',),
 ('EmployeeTerritory',),
 ('Order',),
 ('OrderDetail',),
 ('Product',),
 ('Region',),
 ('Shipper',),
 ('Supplier',),
 ('Territory',)]"""

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
SELECT ProductName
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;""").fetchall())

# What is the largest category (by number of unique products in it)?
# CategoryId: 3
# 13 unique products
"""[(3, 13)]"""
print(curs.execute("""
SELECT CategoryId, MAX(cat_id_count)
FROM (
SELECT CategoryId, COUNT(CategoryId) AS cat_id_count
FROM Product
GROUP BY CategoryId);""").fetchall())

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
