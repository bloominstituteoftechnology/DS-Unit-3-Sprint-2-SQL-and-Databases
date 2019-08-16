import sqlite3

con = sqlite3.connect('northwind_small.sqlite3')

cursor = con.cursor()

query1 = '''SELECT ProductName FROM Product
        ORDER BY UnitPrice DESC
        LIMIT 10;'''

cursor.execute(query1)
rows1 = cursor.fetchall()
print(f'Top 10 most expensive items: {",".join(map(" ".join,rows1))}')

"""
ANSWER: Top 10 most expensive items: Côte de Blaye,Thüringer Rostbratwurst,Mishi Kobe Niku,Sir Rodney's Marmalade,
Carnarvon Tigers,Raclette Courdavault,Manjimup Dried Apples,Tarte au sucre,Ipoh Coffee,Rössle Sauerkraut

"""

query2 = '''SELECT AVG(HireDate-BirthDate) FROM Employee;'''

cursor.execute(query2)
rows2 = cursor.fetchall()
print(f'Average age of employees at date of hire: {str(rows2).strip("[],()")}')

"""
ANSWER: 37.22

"""

query3 = '''SELECT AVG(HireDate-BirthDate), City FROM Employee
        GROUP BY City;'''

cursor.execute(query3)
rows3 = cursor.fetchall()
rows_result3 = [x[0] for x in rows3]
labels3 = [x[1] for x in rows3]
for label, row in zip(labels3, rows_result3):
    print(f'{label}: {row:.2f}')

"""
ANSWER: 

Kirkland: 29.00
London: 32.50
Redmond: 56.00
Seattle: 40.00
Tacoma: 40.00

"""

query4 = '''SELECT ProductName, CompanyName
        FROM Product a
        INNER JOIN Supplier b
        ON a.SupplierId = b.Id
        ORDER BY UnitPrice DESC
        LIMIT 10;'''

cursor.execute(query4)
rows4 = cursor.fetchall()
rows_result4 = [x[1] for x in rows4]
labels4 = [x[0] for x in rows4]
for label, row in zip(labels4, rows_result4):
    print(f'{label}: {row}')

"""
ANSWER: 

Côte de Blaye: Aux joyeux ecclésiastiques
Thüringer Rostbratwurst: Plutzer Lebensmittelgroßmärkte AG
Mishi Kobe Niku: Tokyo Traders
Sir Rodney's Marmalade: Specialty Biscuits, Ltd.
Carnarvon Tigers: Pavlova, Ltd.
Raclette Courdavault: Gai pâturage
Manjimup Dried Apples: G'day, Mate
Tarte au sucre: Forêts d'érables
Ipoh Coffee: Leka Trading
Rössle Sauerkraut: Plutzer Lebensmittelgroßmärkte AG

"""


query5 = '''SELECT CategoryName, COUNT(DISTINCT ProductName) AS ct
        FROM Product a
        INNER JOIN Category b
        ON a.CategoryId = b.Id
        GROUP BY CategoryName
        ORDER BY ct DESC
        LIMIT 1;'''

cursor.execute(query5)
rows5 = cursor.fetchall()
rows_result5 = [x[1] for x in rows5]
labels5 = [x[0] for x in rows5]
for label, row in zip(labels5, rows_result5):
    print(f'{label}: {row}')

"""

ANSWER:

Confections: 13

"""


query6 = '''SELECT FirstName, LastName, COUNT(DISTINCT b.TerritoryId) AS "No. Territories"
        FROM Employee a
        INNER JOIN EmployeeTerritory b
        ON a.Id = b.EmployeeId
        INNER JOIN Territory c
        ON b.TerritoryId = c.Id
        GROUP BY FirstName, LastName
        ORDER BY "No. Territories" DESC
        LIMIT 1;'''

cursor.execute(query6)
rows6 = cursor.fetchall()
rows_result6 = [x[1] for x in rows6]
labels6 = [x[0] for x in rows6]
for label, row in zip(labels6, rows_result6):
    print(f'{label} {row}')

"""

ANSWER:

Robert King

"""

cursor.close()
con.commit()