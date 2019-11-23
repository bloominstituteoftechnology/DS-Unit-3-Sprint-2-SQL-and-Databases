# imports
import sqlite3

# open connection and cursor
nw_conn = sqlite3.connect('northwind_small.sqlite3')
nw_cur = nw_conn.cursor()


# Part 2

def toptenprice():
    '''return the ten most expensive items. returns: 
    [('Côte de Blaye',), ('Thüringer Rostbratwurst',), 
    ('Mishi Kobe Niku',), ("Sir Rodney's Marmalade",), 
    ('Carnarvon Tigers',), ('Raclette Courdavault',), 
    ('Manjimup Dried Apples',), ('Tarte au sucre',), 
    ('Ipoh Coffee',), ('Rössle Sauerkraut',)]'''

    toptenprice = """SELECT ProductName FROM Product 
                 ORDER BY UnitPrice DESC LIMIT 10;"""
    nw_cur.execute(toptenprice)
    return nw_cur.fetchall()


def ageathire():
    '''return the average age of an employee when they were hired.
    returns [(37.22222222222222,)]'''

    ageathire = """SELECT AVG(HireDate - BirthDate) AS AVG_age FROM Employee;"""
    nw_cur.execute(ageathire)
    return nw_cur.fetchall()


def ageathire_city():
    '''return the average hiring age of employees by city.
    returns [(29.0,), (32.5,), (56.0,), (40.0,), (40.0,)]'''

    ageathire_city = """SELECT AVG(HireDate - BirthDate) AS AVG_age FROM Employee 
                    GROUP BY City;"""
    nw_cur.execute(ageathire_city)
    return nw_cur.fetchall()


# Part 3

def toptenprice_supplier():
    '''returns the ten most expensive items with their suppliers. returns:
    [('Côte de Blaye', 'Aux joyeux ecclésiastiques'), 
    ('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG'), 
    ('Mishi Kobe Niku', 'Tokyo Traders'), 
    ("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'), 
    ('Carnarvon Tigers', 'Pavlova, Ltd.'), ('Raclette Courdavault', 'Gai pâturage'), 
    ('Manjimup Dried Apples', "G'day, Mate"), ('Tarte au sucre', "Forêts d'érables"), 
    ('Ipoh Coffee', 'Leka Trading'), ('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]'''

    toptenprice_supplier = """SELECT ProductName, CompanyName FROM Product p
                          JOIN Supplier s ON p.SupplierID = s.ID
                          ORDER BY UnitPrice DESC LIMIT 10;"""
    nw_cur.execute(toptenprice_supplier)
    return nw_cur.fetchall()


def largest_cat():
    '''returns the category with the largest number of unique products.
    returns [('Confections', 13)]'''

    largest_cat = """SELECT CategoryName, MAX(pcount) FROM(
                    SELECT CategoryName, COUNT(DISTINCT(ProductName)) AS pcount FROM Product p
                    JOIN Category c ON p.CategoryID = c.ID
                    GROUP BY CategoryName);"""
    nw_cur.execute(largest_cat)
    return nw_cur.fetchall()


def most_turf():
    '''returns the employee with the most territories.
    returns [('Robert', 'King', 10)]'''

    most_turf = """SELECT FirstName, LastName, MAX(tcount) FROM(
                    SELECT FirstName, LastName, EmployeeID, COUNT(DISTINCT(TerritoryID)) AS tcount FROM EmployeeTerritory t
                    JOIN Employee e ON t.EmployeeID = e.ID
                    GROUP BY EmployeeID);"""
    nw_cur.execute(most_turf)
    return nw_cur.fetchall()

print(toptenprice())
print(ageathire())
print(ageathire_city())
print(toptenprice_supplier())
print(largest_cat())
print(most_turf())