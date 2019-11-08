import sqlite3

# connect to sqlite file
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

expensive_items = """
SELECT Id,UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

# ten most expensive items (per unit price) in the database
print(
    curs.execute(expensive_items).fetchall()
)

# Returns: [(38, 263.5), (29, 123.79), (9, 97), (20, 81),
# (18, 62.5), (59, 55), (51, 53), (62, 49.3), (43, 46), (28, 45.6)]

# the average age of an employee at the time of their hiring
employee_age = """
SELECT AVG(date(HireDate) - date(BirthDate))
FROM Employee;
"""
print(curs.execute(employee_age).fetchall())
# Returns: [(37.22222222222222,)]

# The ten most expensive items (per unit price) and suppliers
unit_supply = """
SELECT Product.Id, ProductName,SupplierID,CompanyName
FROM Product
LEFT JOIN Supplier
ON Product.SupplierID = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
"""
print(curs.execute(unit_supply).fetchall())
# Returns:[(38, 'Côte de Blaye', 18, 'Aux joyeux ecclésiastiques'),
# (29, 'Thüringer Rostbratwurst', 12, 'Plutzer Lebensmittelgroßmärkte AG'),
# (9, 'Mishi Kobe Niku', 4, 'Tokyo Traders'),
# (20, "Sir Rodney's Marmalade", 8, 'Specialty Biscuits, Ltd.'),
# (18, 'Carnarvon Tigers', 7, 'Pavlova, Ltd.'),
# (59, 'Raclette Courdavault', 28, 'Gai pâturage'),
# (51, 'Manjimup Dried Apples', 24, "G'day, Mate"),
# (62, 'Tarte au sucre', 29, "Forêts d'érables"),
# (43, 'Ipoh Coffee', 20, 'Leka Trading'),
# (28, 'Rössle Sauerkraut', 12, 'Plutzer Lebensmittelgroßmärkte AG')]

# The largest category by number of unique products in it
category = """
SELECT CategoryName, COUNT(DISTINCT Product.Id) AS count
FROM Category
LEFT JOIN Product
ON Category.Id = Product.CategoryId
GROUP BY CategoryID
ORDER By count DESC
LIMIT 1;
"""
print(curs.execute(category).fetchall())
# Returns: [('Confections', 13)]
