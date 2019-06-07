### Jason Murphy, BLAH BLAH HEADER GOES HERE!!!


import sqlite3

#SQL Connection created
demo_conn = sqlite3.connect('demo_data.sqlite3')

#Cursor created from connection
demo_curs = demo_conn.cursor()

# create SQL Script
insertvals = """
             CREATE TABLE demo('s' varchar(1),
                               'x' int,
                               'y' int);

             INSERT INTO demo ('s', 'x', 'y')
             VALUES ('g', 3, 9);
             INSERT INTO demo ('s', 'x', 'y')
             VALUES ('v', 5, 7);
             INSERT INTO demo ('s', 'x', 'y')
             VALUES ('f', 8, 7);
             """

#SQL Script is executed
#demo_conn.executescript(insertvals)

#Connection writes data to file.
#demo_conn.commit()


### Querying section

query = """SELECT COUNT(*) FROM demo"""
print('There are ',demo_curs.execute(query).fetchall()[0][0], ' rows.')

query = """SELECT count(*) FROM demo WHERE (x >= 5 AND y >=5)"""
print('There are ',demo_curs.execute(query).fetchall()[0][0], ' rows where x and y are at least 5.')

query = """SELECT count(DISTINCT y) FROM demo"""
print('There are ',demo_curs.execute(query).fetchall()[0][0], ' unique values in y')

nw_conn = sqlite3.connect('northwind_small.sqlite3')

nw_curs = nw_conn.cursor()

### Part 2 Querying with Join

query = """SELECT Product.ProductName from Product ORDER BY Product.UnitPrice DESC LIMIT 10"""
print('The 10 most expensive items are ', nw_curs.execute(query).fetchall())


query = """SELECT AVG(date(Employee.HireDate) - date(Employee.BirthDate)) FROM Employee"""

print('The Average age of employees at hireing date is ',nw_curs.execute(query).fetchall())


### Part 3 Querying with Join

query = """SELECT Product.ProductName, Supplier.CompanyName
from Supplier LEFT JOIN Product
ON Supplier.Id = Product.SupplierId
ORDER BY Product.UnitPrice DESC
LIMIT 10
"""

print('The 10 most expensive items and their supplier are ', nw_curs.execute(query).fetchall())

query = """SELECT Category.CategoryName
FROM Product JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY Product.CategoryID
ORDER BY COUNT(*) DESC
LIMIT 1
"""

print('The largest category of unique items is ', nw_curs.execute(query).fetchall())
