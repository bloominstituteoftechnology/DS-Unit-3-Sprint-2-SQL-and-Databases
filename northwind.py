import sqlite3
import pandas as pd

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Query to view all tables
curs.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;""").fetchall()

# Query to view create table statement for any table
curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()

# Queries for SC questions


# What are the ten most expensive items (per unit price) in the database?
def top_products_price():
    print(pd.read_sql_query("""SELECT ProductName, UnitPrice
            FROM Product
            ORDER BY UnitPrice DESC
            LIMIT 10;""", conn))
#                ProductName  UnitPrice
# 0            Côte de Blaye     263.50
# 1  Thüringer Rostbratwurst     123.79
# 2          Mishi Kobe Niku      97.00
# 3   Sir Rodney's Marmalade      81.00
# 4         Carnarvon Tigers      62.50
# 5     Raclette Courdavault      55.00
# 6    Manjimup Dried Apples      53.00
# 7           Tarte au sucre      49.30
# 8              Ipoh Coffee      46.00
# 9        Rössle Sauerkraut      45.60


# What is the average age of an employee at the time of their hiring?
# (Hint: a lot of arithmetic works with dates.)
def avg_emp_age():
    print(pd.read_sql_query("""SELECT ROUND(AVG(HireDate - BirthDate)) as avg_age
            FROM Employee;""", conn))
#    avg_age
# 0     37.0


# (Stretch) How does the average age of employee at hire vary by city?
def row_count():
    print(pd.read_sql_query("""SELECT City, ROUND(AVG(HireDate - BirthDate)) as avg_age
            FROM Employee
            GROUP BY City;""", conn))
#        City  avg_age
# 0  Kirkland     29.0
# 1    London     33.0
# 2   Redmond     56.0
# 3   Seattle     40.0
# 4    Tacoma     40.0


# What are the ten most expensive items (per unit price) in the
# database and their suppliers?
def top_products_price_supp():
    print(pd.read_sql_query("""SELECT s.CompanyName, p.ProductName, p.UnitPrice
            FROM Product p
            JOIN Supplier s ON s.Id = p.SupplierId
            ORDER BY UnitPrice DESC
            LIMIT 10;""", conn))
#                          CompanyName              ProductName  UnitPrice
# 0         Aux joyeux ecclésiastiques            Côte de Blaye     263.50
# 1  Plutzer Lebensmittelgroßmärkte AG  Thüringer Rostbratwurst     123.79
# 2                      Tokyo Traders          Mishi Kobe Niku      97.00
# 3           Specialty Biscuits, Ltd.   Sir Rodney's Marmalade      81.00
# 4                      Pavlova, Ltd.         Carnarvon Tigers      62.50
# 5                       Gai pâturage     Raclette Courdavault      55.00
# 6                        G'day, Mate    Manjimup Dried Apples      53.00
# 7                   Forêts d'érables           Tarte au sucre      49.30
# 8                       Leka Trading              Ipoh Coffee      46.00
# 9  Plutzer Lebensmittelgroßmärkte AG        Rössle Sauerkraut      45.60


# What is the largest category (by number of products in it)?
def top_category():
    print(pd.read_sql_query("""SELECT c.CategoryName, COUNT(p.Id) prod_count
            FROM Product p
            JOIN Category c ON c.Id = p.CategoryId
            GROUP BY c.CategoryName
            ORDER BY COUNT(p.Id) DESC
            LIMIT 1;""", conn))
# 0  Confections          13


# (*Stretch*) What is the top territory (by number of employees), and
#  how many employees does it have?
def top_territory():
    print(pd.read_sql_query("""SELECT t.TerritoryDescription, COUNT(e.Id) as employee_count
            FROM EmployeeTerritory et
            JOIN Territory t ON t.Id = et.TerritoryId
            JOIN Employee e on e.Id = et.EmployeeId
            GROUP BY TerritoryDescription
            ORDER BY COUNT(e.Id) DESC
            LIMIT 1;""", conn))
#   TerritoryDescription  employee_count
# 0             New York               2


# Who's the employee with the most territories?
def top_employee():
    print(pd.read_sql_query("""SELECT e.Id, e.LastName, e.FirstName,
            COUNT(distinct et.TerritoryId) count_territories
            FROM EmployeeTerritory et
            JOIN Employee e on e.Id = et.EmployeeId
            GROUP BY e.Id
            ORDER BY COUNT(distinct et.TerritoryId) DESC
            LIMIT 1;""", conn))
#             Id LastName FirstName  count_territories
# 0   7     King    Robert                 10
