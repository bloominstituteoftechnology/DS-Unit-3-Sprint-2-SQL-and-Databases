!#/usr/bin/env python

import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')

curs = conn.cursor()
curs.execute('select name from sqlite_master where type="table" order by name;').fetchall()

curs.execute('select sql from sqlite_master where type="table" order by name;').fetchall()

curs.execute('select ProductName,UnitPrice from Product order by UnitPrice desc limit 10').fetchall()
[('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]

curs.execute('SELECT firstname, lastname, AVG(hiredate - birthdate) FROM employee').fetchall()
[('Nancy', 'Davolio', 37.22222222222222)]

curs.execute('SELECT firstname, lastname, AVG(hiredate - birthdate) FROM employee GROUP BY city').fetchall()
[('Janet', 'Leverling', 29.0), ('Steven', 'Buchanan', 32.5), ('Margaret', 'Peacock', 56.0), ('Nancy', 'Davolio', 40.0), ('Andrew', 'Fuller', 40.0)]



 curs.execute('select territoryDescription, count(employeeid) from territory, employeeterritory where territory.id = employeeterritory.territoryid  group by employeeid order by count(employeeid) limit 1').fetchall()
[('Wilton', 2)]
