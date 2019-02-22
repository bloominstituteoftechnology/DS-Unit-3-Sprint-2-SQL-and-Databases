#!/usr/bin/env python 

"""SQlite3 demo_data.db queries"""

import sqlite3

# connet to database 
conn = sqlite3.connect('northwind_small.sqlite3')
c = conn.cursor()


 # ten most expensive products 
c.execute("SELECT ID, ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10")

 """"(38, 'Côte de Blaye', 263.5), 
 (29, 'Thüringer Rostbratwurst', 123.79), 
 (9, 'Mishi Kobe Niku', 97), 
 (20, "Sir Rodney's Marmalade", 81), 
 (18, 'Carnarvon Tigers', 62.5), 
 (59, 'Raclette Courdavault', 55), 
 (51, 'Manjimup Dried Apples', 53), 
 (62, 'Tarte au sucre', 49.3), 
 (43, 'Ipoh Coffee', 46), 
 (28, 'Rössle Sauerkraut', 45.6)"""


# average age when hired 
c.execute("SELECT avg(Employee.HireDate - Employee.BirthDate) FROM Employee")
# [(37.22222222222222,)]

#average age by city

c.execute("SELECT Employee.city, avg(Employee.HireDate - Employee.BirthDate) FROM Employee GROUP BY Employee.city")
"""[('Kirkland', 29.0), 
	('London', 32.5), 
	('Redmond', 56.0), 
	('Seattle', 40.0), 
	('Tacoma', 40.0)]"""


#ten most expensive products and supplier name 
c.execute("SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName FROM Product INNER JOIN Supplier ON Product.SupplierID=Supplier.ID ORDER BY UnitPrice DESC LIMIT 10;")
"""[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'), 
 ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), 
 ('Mishi Kobe Niku', 97, 'Tokyo Traders'), 
 ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), 
 ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'), 
 ('Raclette Courdavault', 55, 'Gai pâturage'), 
 ('Manjimup Dried Apples', 53, "G'day, Mate"), 
 ('Tarte au sucre', 49.3, "Forêts d'érables"), 
 ('Ipoh Coffee', 46, 'Leka Trading'), 
 ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]"""


#largest category based on number of products
c.execute("SELECT Category.CategoryName  FROM Category INNER JOIN Product ON Product.CategoryID=Category.ID ORDER BY Category.CategoryName DESC LIMIT 1;")
"""[('Beverages')]"""