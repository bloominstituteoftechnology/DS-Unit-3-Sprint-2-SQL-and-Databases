import sqlite3
import pandas as pd

dbfile = 'northwind_small.sqlite3'

def count(dbfile,query):
    c = sqlite3.connect(dbfile)
    curs = c.cursor()
    return curs.execute(query).fetchall()

conn = sqlite3.connect(dbfile)

query = '''SELECT ProductName,UnitPrice FROM Product
            ORDER BY UnitPrice DESC
            LIMIT 10;'''

df = pd.read_sql(query, conn)

print(f'10 Most expensive items in database are: \n{df}\n')

query2 = '''SELECT AVG(HireDate - BirthDate) FROM Employee;'''

print(f'Average age of Employee at time of Hiring is: {count(dbfile,query2)}\n')

query3 = '''SELECT City, AVG(HireDate - BirthDate) FROM Employee
            GROUP BY City;'''

print(f'Average age of Employee at time of Hiring by City is:\n {count(dbfile,query3)}\n')

query4 =  """SELECT UnitPrice, CompanyName
             FROM Product
             JOIN Supplier 
                ON Product.SupplierId = Supplier.Id
             ORDER BY UnitPrice DESC
             LIMIT 10;"""

df2 = pd.read_sql(query4, conn)

print (f'ten most expensive items (per unit price) in the database and their suppliers are:\n {df2}\n')

query5 = """SELECT CategoryName, COUNT(DISTINCT ProductName) as ProductCount FROM Category
            JOIN Product 
                ON Category.Id = Product.CategoryId
            GROUP BY CategoryName
            ORDER BY ProductCount DESC
            LIMIT 1;"""
            
print(f'largest category by number of products in it is:{count(dbfile,query5)}\n')

# Below is the output of this file :
'''
10 Most expensive items in database are: 
               ProductName  UnitPrice
0            Côte de Blaye     263.50
1  Thüringer Rostbratwurst     123.79
2          Mishi Kobe Niku      97.00
3   Sir Rodney's Marmalade      81.00
4         Carnarvon Tigers      62.50
5     Raclette Courdavault      55.00
6    Manjimup Dried Apples      53.00
7           Tarte au sucre      49.30
8              Ipoh Coffee      46.00
9        Rössle Sauerkraut      45.60

Average age of Employee at time of Hiring is: [(37.22222222222222,)]

Average age of Employee at time of Hiring by City is:
 [('Kirkland', 29.0), ('London', 32.5), ('Redmond', 56.0), ('Seattle', 40.0), ('Tacoma', 40.0)]

ten most expensive items (per unit price) in the database and their suppliers are:
    UnitPrice                        CompanyName
0     263.50         Aux joyeux ecclésiastiques
1     123.79  Plutzer Lebensmittelgroßmärkte AG
2      97.00                      Tokyo Traders
3      81.00           Specialty Biscuits, Ltd.
4      62.50                      Pavlova, Ltd.
5      55.00                       Gai pâturage
6      53.00                        G'day, Mate
7      49.30                   Forêts d'érables
8      46.00                       Leka Trading
9      45.60  Plutzer Lebensmittelgroßmärkte AG

largest category by number of products in it is:[('Confections', 13)]
'''