
import sqlite3
import os

# Omg this filename had a space the whole time
conn = sqlite3.connect('northwind_small (1).sqlite3')
curs = conn.cursor()


def list_entries(query):
    ''' List entries

    Parameters
    ------------------
    query: str

    ------------------
    Returns
    queried: list of tuples(?)
    '''
    queried = curs.execute(query).fetchall()
    # Sorry for the super ugly output
    return queried


# Example of list of columns
"""
print(curs.execute('''
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;
''').fetchall())
"""
"""
# Example of customer column
print(curs.execute('''
SELECT sql FROM sqlite_master WHERE name="Supplier";
''').fetchall())
"""
# Part 2

# Ten most expensive items (per unit price in database)
expensive_items = f'''
SELECT ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''
# Average age at hiring
average_age_hired = f'''
SELECT ROUND(AVG(HireDate-BirthDate),2) FROM Employee
'''
# Average age at hiring by city
average_age_hByC = f'''
SELECT City, ROUND(AVG(HireDate-BirthDate),2) FROM Employee
GROUP BY City
'''
print(f'''
Top ten most expensive items:
{list_entries(expensive_items)} \n
Average Hired Age:
{list_entries(average_age_hired)} \n
Average Age Hired (by city):
{list_entries(average_age_hByC)} \n
''')

# Part 3 JOINs

# Ten most expensive items and their suppliers
expensive_items_pSp = f'''
SELECT ProductName, UnitPrice, Supplier.CompanyName
FROM Product JOIN Supplier ON (Product.SupplierID=Supplier.Id)
ORDER BY UnitPrice DESC
LIMIT 10;
'''
# Largest category by unique products
largest_category_unique = f'''
SELECT
CategoryName,
COUNT(DISTINCT(Product.ProductName)) c
FROM Product LEFT JOIN Category ON (Product.CategoryID=Category.Id)
GROUP BY CategoryName
ORDER BY c DESC
LIMIT 1;
'''
# Employee with the most territories
most_territories = f'''
SELECT
FirstName, LastName,
COUNT(DISTINCT(EmployeeTerritory.TerritoryId)) a
FROM
Employee JOIN EmployeeTerritory ON (Employee.Id=EmployeeTerritory.EmployeeID)
GROUP BY FirstName
ORDER BY a DESC
LIMIT 1;
'''
print(f'''
Top ten most expensive items (w/ supplier):
{list_entries(expensive_items_pSp)} \n
Largest Category (w/ unique products):
{list_entries(largest_category_unique)} \n
Employee with most territories:
{list_entries(most_territories)}
''')
