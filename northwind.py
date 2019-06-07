import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

query1 = """
SELECT ProductName, UnitPrice FROM Product
         ORDER BY UnitPrice Desc LIMIT 10; """

query2 = """
SELECT AVG(HireDate-BirthDate) AS hire_age FROM Employee; """

query3 = """
SELECT City, AVG(HireDate-BirthDate) AS hire_age FROM Employee
       GROUP BY City; """

print(curs.execute(query1).fetchall())
print(curs.execute(query2).fetchall())
print(curs.execute(query3).fetchall())
