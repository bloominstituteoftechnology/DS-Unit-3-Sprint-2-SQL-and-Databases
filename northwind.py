import sqlite3

CONN = sqlite3.connect('northwind_small.sqlite3')

cursor1 = CONN.cursor()
query1 = '''SELECT ProductName, UnitPrice FROM Product
            ORDER BY UnitPrice DESC
            LIMIT 10;
        '''
cursor1.execute(query1).fetchall()
print(cursor1.execute(query1).fetchall())
'''[('Côte de Blaye', 263.5),
    ('Thüringer Rostbratwurst', 123.79),
    ('Mishi Kobe Niku', 97),
    ("Sir Rodney's Marmalade", 81),
    ('Carnarvon Tigers', 62.5),
    ('Raclette Courdavault', 55),
    ('Manjimup Dried Apples', 53),
    ('Tarte au sucre', 49.3),
    ('Ipoh Coffee', 46),
    ('Rössle Sauerkraut', 45.6)]'''
 
cursor2 = CONN.cursor()
query2 = '''SELECT avg(CAST((
            julianday(emp.HireDate) - julianday(emp.BirthDate)
            ) / 365 As Integer))   
            FROM Employee as emp;
        '''
cursor2.execute(query2).fetchall()
print(cursor2.execute(query2).fetchall())
'''[(36.77777777777778,)]'''

cursor3 = CONN.cursor()
query3 = '''SELECT ProductName, UnitPrice, CompanyName 
            FROM Product as prod, Supplier as sup
            WHERE prod.SupplierID = sup.Id
            ORDER BY UnitPrice DESC
            LIMIT 10;
        '''
cursor3.execute(query3).fetchall()
print(cursor3.execute(query3).fetchall())
'''[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
    ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
    ('Mishi Kobe Niku', 97, 'Tokyo Traders'),
    ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
    ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
    ('Raclette Courdavault', 55, 'Gai pâturage'),
    ('Manjimup Dried Apples', 53, "G'day, Mate"),
    ('Tarte au sucre', 49.3, "Forêts d'érables"),
    ('Ipoh Coffee', 46, 'Leka Trading'),
    ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]'''

cursor4 = CONN.cursor()
query4 = '''SELECT CategoryName, COUNT(DISTINCT ProductName)
            FROM Product as prod, Category as cat
            WHERE prod.CategoryId = cat.Id
            GROUP BY CategoryName
            ORDER BY COUNT(DISTINCT ProductName) DESC
            LIMIT 1;
        '''
cursor4.execute(query4).fetchall()
print(cursor4.execute(query4).fetchall())
'''[('Confections', 13)]'''
