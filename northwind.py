import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# ten most expensive items (per unit price) in the database
curs.execute("""
  SELECT ProductName, UnitPrice 
    FROM Product 
ORDER BY UnitPrice DESC
   LIMIT 10;
   """)
print()
print('Ten most expensive items by unit price:')
print('---'*13)
print(curs.fetchall())
print()

# average employee age on hiring date
curs.execute("""
  SELECT AVG(HireDate - BirthDate) 
        FROM Employee;
   """)
print('Average employee age on hiring:')
print('---'*10)
print(curs.fetchall())
print()

# average employee age on hiring date by city
curs.execute("""
      SELECT City, AVG(HireDate - BirthDate) 
        FROM Employee
    GROUP BY City;
   """)
print('Average employee age on hiring by city:')
print('---'*13)
print(curs.fetchall())
print()

# ten most expensive items (per unit price) in the database AND their suppliers
curs.execute("""
   SELECT ProductName, UnitPrice, CompanyName 
     FROM Product 
LEFT JOIN Supplier
       ON Product.SupplierID = Supplier.Id
 ORDER BY UnitPrice DESC
    LIMIT 10;
   """)
print('Most expensive items (by unit price) with supplier:')
print('---'*17)
print(curs.fetchall())
print()

# What is the largest category (by number of unique products in it)?
curs.execute("""
  SELECT CategoryName, COUNT(DISTINCT(Product.Id))
    FROM Product
    JOIN Category
      ON Product.CategoryId = Category.Id
GROUP BY CategoryId
ORDER BY COUNT(DISTINCT(Product.Id)) DESC
   LIMIT 1"""
)
print('What is the largest category:')
print('---'*10)
print(curs.fetchall())
print()

# Who's the employee with the most territories? 
# Use TerritoryId as the unique identifier for territories
curs.execute("""
  SELECT EmployeeId, COUNT(DISTINCT(TerritoryId)) 
    FROM EmployeeTerritory
GROUP BY EmployeeId
ORDER BY COUNT(DISTINCT(TerritoryId)) DESC
   LIMIT 1"""
            )
print('Employee with the most territories:')
print('---'*12)
print(curs.fetchall())
print()

conn.close()

"""
$ python northwind.py

Ten most expensive items by unit price:
---------------------------------------
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

Average employee age on hiring:
------------------------------
[(37.22222222222222,)]

Average employee age on hiring by city:
---------------------------------------
[('Kirkland', 29.0), 
('London', 32.5), 
('Redmond', 56.0), 
('Seattle', 40.0), 
('Tacoma', 40.0)]

Most expensive items (by unit price) with supplier:
---------------------------------------------------
[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'), 
('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), 
('Mishi Kobe Niku', 97, 'Tokyo Traders'), 
("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), 
('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'), 
('Raclette Courdavault', 55, 'Gai pâturage'), 
('Manjimup Dried Apples', 53, "G'day, Mate"), 
('Tarte au sucre', 49.3, "Forêts d'érables"), 
('Ipoh Coffee', 46, 'Leka Trading'), 
('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]

What is the largest category:
------------------------------
[('Confections', 13)]

Employee with the most territories:
------------------------------------
[(7, 10)]

"""