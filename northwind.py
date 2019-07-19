import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()

cursor.execute("SELECT ProductName FROM Product ORDER BY UnitPrice LIMIT 10;").fetchall()
'''10 most expensive items:
[('Geitost',),
 ('Guaraná Fantástica',),
 ('Konbu',),
 ('Filo Mix',),
 ('Tourtière',),
 ('Rhönbräu Klosterbier',),
 ('Tunnbröd',),
 ('Teatime Chocolate Biscuits',),
 ('Rogede sild',),
 ('Zaanse koeken',)]'''

cursor.execute("SELECT AVG(HireDate - BirthDate) FROM Employee;").fetchall()
#Average age at hire [(37.22222222222222,)]

cursor.execute("SELECT AVG(HireDate - BirthDate), City FROM Employee GROUP BY City;").fetchall()
'''Average age at hire by city
[(29.0, 'Kirkland'),
 (32.5, 'London'),
 (56.0, 'Redmond'),
 (40.0, 'Seattle'),
 (40.0, 'Tacoma')]'''

query = (
    '''      SELECT ProductName, CompanyName
               FROM Product
    LEFT OUTER JOIN Supplier
                 ON Product.SupplierID = Supplier.ID
                 ORDER BY UnitPrice
           LIMIT 10;
    ''')
#It's ID, not supplier ID
cursor.execute(query).fetchall()
'''10 most expensive items and their suppliers
[('Geitost', 'Norske Meierier'),
 ('Guaraná Fantástica', 'Refrescos Americanas LTDA'),
 ('Konbu', "Mayumi's"),
 ('Filo Mix', "G'day, Mate"),
 ('Tourtière', 'Ma Maison'),
 ('Rhönbräu Klosterbier', 'Plutzer Lebensmittelgroßmärkte AG'),
 ('Tunnbröd', 'PB Knäckebröd AB'),
 ('Teatime Chocolate Biscuits', 'Specialty Biscuits, Ltd.'),
 ('Rogede sild', 'Lyngbysild'),
 ('Zaanse koeken', 'Zaanse Snoepfabriek')]'''

query = (
    '''
               SELECT Product.ID, CategoryName
               FROM Product
    LEFT OUTER JOIN Category
                 ON Product.CategoryID = Category.ID
                 ;
    ''')
cursor.execute(query).fetchall()

query = (
    '''

               SELECT CategoryName, COUNT(*) FROM
               (
               SELECT Product.ID, CategoryName
               FROM Product
    LEFT OUTER JOIN Category
                 ON Product.CategoryID = Category.ID)
                 GROUP BY CategoryName
                 ORDER BY COUNT(*) DESC
                 LIMIT 1
                 ;
    ''')
cursor.execute(query).fetchall()
#Largest category by number of unique products: [('Confections', 13)]

query = (
    '''
               SELECT Employee.ID, FirstName, LastName, TerritoryID
               FROM Employee
    LEFT OUTER JOIN EmployeeTerritory
                 ON Employee.ID = EmployeeTerritory.EmployeeID
                 ;
    ''')
cursor.execute(query).fetchall()

query = (
    '''        SELECT ID, FirstName, LastName, COUNT(*) FROM
               (SELECT Employee.ID, FirstName, LastName, TerritoryID
               FROM Employee
    LEFT OUTER JOIN EmployeeTerritory
                 ON Employee.ID = EmployeeTerritory.EmployeeID)
                 GROUP BY ID
                 ORDER BY COUNT(*) DESC
                 LIMIT 1
                 ;
    ''')
cursor.execute(query).fetchall()
'''Employee with the most territories is Robert King Employee ID 7 with
10 territories
[(7, 'Robert', 'King', 10)]'''

'''In the Northwind database, what is the type of relationship between
the Employee and Territory tables?

The Employee and Territory tables are linked by the EmployeeTerritory
table. In that table, the TerritoryID is keyed to the Territory
table and the EmployeeID is keyed to the Employee table. The tables
could be joined through the EmployeeTerritory table.

What is a situation where a document store (like MongoDB) is
appropriate, and what is a situation where it is not appropriate?

Document stores are useful for storing large amounts of low structure
data that needs to be quickly retrieved. A document store is not
appropriate if you want to store the data
in a highly structured fashion like in an RDBMS. Another situation
when it is not the best choice is when ACID-type criteria such as
reliability are important.


What is "NewSQL", and what is it trying to achieve?
NewSQL is a type of RDMS which is trying to have both the strengths
of NoSQL and traditional SQL databases. It is ACID-compliant while
having better performance than most such systems. This allows
saving of costs over full deployment of traditional SQL databases.


'''
