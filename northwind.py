!#/usr/bin/env python

import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')

curs = conn.cursor()
curs.execute('select name from sqlite_master where type="table" order by name;').fetchall()

curs.execute('select sql from sqlite_master where type="table" order by name;').fetchall()

curs.execute('select ProductName from Product order by UnitPrice limit 10').fetchall()
[('Geitost',), ('Guaraná Fantástica',), ('Konbu',), ('Filo Mix',), ('Tourtière',), ('Rhönbräu Klosterbier',), ('Tunnbröd',), ('Teatime Chocolate Biscuits',), ('Rogede sild',), ('Zaanse koeken',)]

curs.execute('SELECT firstname, lastname, AVG(hiredate - birthdate) FROM employee').fetchall()
[('Nancy', 'Davolio', 37.22222222222222)]

curs.execute('SELECT firstname, lastname, AVG(hiredate - birthdate) FROM employee GROUP BY city').fetchall()
[('Janet', 'Leverling', 29.0), ('Steven', 'Buchanan', 32.5), ('Margaret', 'Peacock', 56.0), ('Nancy', 'Davolio', 40.0), ('Andrew', 'Fuller', 40.0)]




