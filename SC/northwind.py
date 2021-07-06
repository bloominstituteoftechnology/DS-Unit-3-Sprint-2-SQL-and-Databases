import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
most_expensive_query = """
    SELECT ProductName, UnitPrice FROM Product
     ORDER BY UnitPrice DESC
     LIMIT 10;
    """

most_expensive = curs.execute(most_expensive_query).fetchall()
print('\nThe ten most expensive items and their prices (unit unknown):')
print('-------------------------------')
for info in most_expensive:
    item = (info[0] + ':').ljust(24)
    price = info[1]
    print(f'{item} {price}')

"""Output:
The ten most expensive items and their prices (unit unknown):
-------------------------------
Côte de Blaye:           263.5
Thüringer Rostbratwurst: 123.79
Mishi Kobe Niku:         97
Sir Rodney's Marmalade:  81
Carnarvon Tigers:        62.5
Raclette Courdavault:    55
Manjimup Dried Apples:   53
Tarte au sucre:          49.3
Ipoh Coffee:             46
Rössle Sauerkraut:       45.6
"""

# What is the average age of an employee at the time of their hiring?
avg_age_query = """
    SELECT ROUND(AVG(Hiredate - Birthdate), 2) AS average_age_on_hire
      FROM Employee;
    """

avg_age = curs.execute(avg_age_query).fetchone()[0]
print('\nThe average age at the time of hiring of '
      f'employees is {avg_age} years old.')

"""Output:
The average age at the time of hiring of employees is 37.22 years old.
"""

# (Stretch) How does the average age of employee at hire vary by city?
avg_age_by_city_query = """
    SELECT City, ROUND(AVG(Hiredate - Birthdate), 2) AS average_age_on_hire
      FROM Employee
     GROUP BY City
     ORDER BY average_age_on_hire;
    """

avg_age_by_city = curs.execute(avg_age_by_city_query).fetchall()
print('\nThe average age of employees at hire by city:')
print('--------------')
for info in avg_age_by_city:
    city = (info[0] + ':').ljust(9)
    age = info[1]
    print(f'{city} {age}')

"""Output:
The average age of employees at hire by city:
--------------
Kirkland: 29.0
London:   32.5
Seattle:  40.0
Tacoma:   40.0
Redmond:  56.0
"""

# What are the ten most expensive items (per unit price) in the
# database and their suppliers?

item_supplier_query = """
    SELECT ProductName, CompanyName FROM Product
     INNER JOIN Supplier ON Product.SupplierID = Supplier.ID
     ORDER BY UnitPrice DESC
     LIMIT 10;
    """

item_supplier = curs.execute(item_supplier_query).fetchall()

print('\nThe ten most expensive items with their supplier:')
print('----------------------------------------------------------')
for info in item_supplier:
    item = (info[0] + ':').ljust(24)
    supplier = info[1]
    print(f'{item} {supplier}')

"""Output:
The ten most expensive items with their supplier:
----------------------------------------------------------
Côte de Blaye:           Aux joyeux ecclésiastiques
Thüringer Rostbratwurst: Plutzer Lebensmittelgroßmärkte AG
Mishi Kobe Niku:         Tokyo Traders
Sir Rodney's Marmalade:  Specialty Biscuits, Ltd.
Carnarvon Tigers:        Pavlova, Ltd.
Raclette Courdavault:    Gai pâturage
Manjimup Dried Apples:   G'day, Mate
Tarte au sucre:          Forêts d'érables
Ipoh Coffee:             Leka Trading
Rössle Sauerkraut:       Plutzer Lebensmittelgroßmärkte AG
"""

# What is the largest category (by number of unique products in it)?
largest_cat_query = """
    SELECT CategoryName, COUNT(DISTINCT Product.ID) AS NumberProducts
      FROM Category
     INNER JOIN Product ON Category.ID = Product.CategoryID
     GROUP BY CategoryName
     ORDER BY NumberProducts DESC
     LIMIT 1;
    """

largest_cat = curs.execute(largest_cat_query).fetchone()
print(f'\nThe {largest_cat[0]} category has the largest number '
      f'of unique products with {largest_cat[1]} products.')

"""Output:
The Confections category has the largest number of unique products
with 13 products.
"""

# (Stretch) Who's the employee with the most territories?
# Use TerritoryId (not name, region, or other fields)
# as the unique identifier for territories.

most_territories_query = """
    SELECT LastName, FirstName, COUNT(Territory.ID) as NumberTerritories
           FROM Employee
      JOIN EmployeeTerritory AS et
           ON Employee.ID = et.EmployeeID
      JOIN Territory
           ON et.TerritoryID = TerritoryID
     GROUP BY Employee.ID
     ORDER BY NumberTerritories DESC
     LIMIT 1;
    """

most_territories = curs.execute(most_territories_query).fetchone()
print(f'\n{most_territories[1]} {most_territories[0]} is the employee with '
      f'the most territories at {most_territories[2]}.\n')

"""Output:
Robert King is the employee with the most territories at 530.
"""

curs.close()
conn.close()
