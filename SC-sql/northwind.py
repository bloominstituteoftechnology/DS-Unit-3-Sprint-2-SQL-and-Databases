"""

Northwind Database

"""

import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

print(cur.execute('SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;').fetchall())

"""

('Côte de Blaye', 263.5),
 ('Thüringer Rostbratwurst', 123.79),
 ('Mishi Kobe Niku', 97),
 ("Sir Rodney's Marmalade", 81),
 ('Carnarvon Tigers', 62.5),
 ('Raclette Courdavault', 55),
 ('Manjimup Dried Apples', 53),
 ('Tarte au sucre', 49.3),
 ('Ipoh Coffee', 46),
 ('Rössle Sauerkraut', 45.6)]

"""


print(cur.execute('SELECT AVG(HireDate - BirthDate) FROM Employee').fetchall()[0][0])

"""

37.22

"""

print(cur.execute('''SELECT ProductName, UnitPrice, Supplier.CompanyName
            FROM Product 
            LEFT JOIN Supplier 
            ON Product.SupplierID=Supplier.ID
            ORDER BY UnitPrice 
            DESC LIMIT 10
            ;''').fetchall())

"""

[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
 ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
 ('Mishi Kobe Niku', 97, 'Tokyo Traders'),
 ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
 ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
 ('Raclette Courdavault', 55, 'Gai pâturage'),
 ('Manjimup Dried Apples', 53, "G'day, Mate"),
 ('Tarte au sucre', 49.3, "Forêts d'érables"),
 ('Ipoh Coffee', 46, 'Leka Trading'),
 ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]

"""

print(cur.execute('''SELECT ProductName, COUNT(Category.CategoryName)
            FROM Product
            LEFT JOIN Category ON Product.CategoryID=Category.Id
            GROUP BY Category.CategoryName
            ORDER BY COUNT(Category.CategoryName) DESC LIMIT 1;''').fetchall())

"""

[('Pavlova', 13)]

"""
