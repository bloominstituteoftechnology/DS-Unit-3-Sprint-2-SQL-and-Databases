import sqlite3
connection = sqlite3.connect('northwind_small.sqlite3')
c = connection.cursor()
c.execute("SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10")
c.fetchall()
c.execute("SELECT AVG(HireDate-BirthDate) FROM Employee")
c.fetchone()