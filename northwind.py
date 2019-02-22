#import sqlite, create and connect to data file
import sqlite3 as sq
conn = sq.connect('northwind_small.sqlite3')
curs = conn.cursor()

#10 most expensive items
def most_exp():
    a = '''
    SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice desc
    LIMIT 10'''
    curs.execute(a)
    return curs.fetchall()
        
most_exp()  

[('Côte de Blaye', 263.5),
 ('Thüringer Rostbratwurst', 123.79),
 ('Mishi Kobe Niku', 97),
 ("Sir Rodney's Marmalade", 81),
 ('Carnarvon Tigers', 62.5),
 ('Raclette Courdavault', 55),
 ('Manjimup Dried Apples', 53),
 ('Tarte au sucre', 49.3),
 ('Ipoh Coffee', 46),
 ('Rössle Sauerkraut', 45.6)]

 #Average hire age
def avg_age():
    a1 = '''
    SELECT AVG
    (HireDate - BirthDate)
    FROM Employee
    '''
    curs.execute(a1)
    return curs.fetchall()

avg_age()

[(37.22222222222222,)]