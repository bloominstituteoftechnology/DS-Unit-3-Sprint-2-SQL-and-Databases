'''Sprint Challenge U3S2 - Parts 2 & 3'''
'''Access with northwind.ipynb'''

import sqlite3
import pandas as pd

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


# PART 2 -----------------------------------------------------------------

def most_expensive_items():
    # What are the ten most expensive items (per unit price) in the database?
    ''' RESULT: 
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
    '''
    print(pd.read_sql_query(
        ''' SELECT ProductName, UnitPrice FROM Product
            Order by UnitPrice DESC
            Limit 10
        ''',
        conn)
    )


def avg_employee_age():
    # What is the average age of an employee at the time of their hiring? 
    #  (Hint: a lot of arithmetic works with dates.)
    ''' RESULT: 37.2222222'''
    print(pd.read_sql_query(
        ''' SELECT AVG(HireDate-BirthDate) FROM Employee
        ''',
        conn)
    )

def avg_employee_per_city():
    # (Stretch) How does the average age of employee at hire vary by city?
    ''' RESULT: 
    [('Kirkland', 29.0),
    ('London', 32.5),
    ('Redmond', 56.0),
    ('Seattle', 40.0),
    ('Tacoma', 40.0)]
    '''
    print(pd.read_sql_query(
        ''' SELECT CITY, AVG(HireDate-BirthDate) FROM Employee
            GROUP BY CITY
        ''',
        conn)
    )

# PART 3 -----------------------------------------------------------------

def most_expensive_items_and_city():  
    # What are the ten most expensive items (per unit price) in the database 
    #  and their suppliers?
    '''RESULT: 
         UnitPrice                     CompanyName
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
    '''
    print(pd.read_sql_query(
        ''' SELECT UnitPrice,CompanyName 
            FROM Product as P
            LEFT JOIN Supplier as S
            ON P.SupplierID = S.ID 
            ORDER BY UnitPrice DESC
            LIMIT 10             
        ''',
        conn)
    )

def largest_category_by_unique_products():
    # What is the largest category (by number of unique products in it)?
    ''' RESULT: Category ID #3'''
    print(pd.read_sql_query(
        ''' SELECT P.CategoryID, COUNT(distinct O.ProductID)
            FROM OrderDetail as O
            JOIN Product as P
            ON P.ID = O.ProductID
            GROUP BY P.CategoryID
            ORDER BY COUNT(distinct O.ProductID) DESC
        ''',
        conn)
    )

def employee_with_most_territories():
    # (Stretch) Who's the employee with the most territories? Use TerritoryId 
    # (not name, region, or other fields) as the unique identifier for territories.
    ''' RESULT: Robert King '''
    print(pd.read_sql_query(
        ''' SELECT E.ID, E.FirstName, E.LastName, COUNT(ET.TerritoryID) 
            FROM Employee as E
            JOIN EmployeeTerritory as ET
            ON E.ID = ET.EmployeeID
            GROUP BY E.ID
            ORDER BY COUNT(ET.TerritoryID) DESC
        ''',
        conn)
    )