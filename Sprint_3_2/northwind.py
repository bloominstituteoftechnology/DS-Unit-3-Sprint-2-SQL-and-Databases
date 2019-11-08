import sqlite3

"""Queries for Northwind_small.sqlite3 for 3_2 Sprint"""

"""PART 2: The Northwind Database"""

CONN = sqlite3.connect('northwind_small.sqlite3')
cursor = CONN.cursor()

"""Query 1: What are the ten most expensive items (per uniqt price)
in the database?
"""

query_1 = """SELECT ProductName, UnitPrice
            FROM Product
            ORDER BY UnitPrice DESC
            LIMIT 10;
            """
expensive = cursor.execute(query_1).fetchall()
print("The ten most expensive items by unit price are:")
for item in expensive:
    print (item)
print (" \n")

"""Query 2: What is the average age of an employee
at the time of their hiring?
"""

query_2 = """SELECT AVG(HireDate - BirthDate)
            FROM Employee;
            """
avg_age = cursor.execute(query_2).fetchone()
avg_age = str(avg_age).strip('[](),')
avg_age = float(avg_age)
print(f"The average age of an employee at the time of hiring is {avg_age:.1f}. \n")

"""Query3 (*Stretch*): How does the average age
of employee at hire vary by city?
"""

query_3 = """SELECT AVG(HireDate - BirthDate) AS Average_Age,
                City
                FROM Employee
                GROUP BY City
                ORDER BY Average_Age;
                """
avg_age_city = cursor.execute(query_3).fetchall()
print("The average age of employees at hiring time varies by city as follows:")
for age in avg_age_city:
    print(age)
print(" \n")

"""PART 3: Sailing the Northwind Seas"""

"""Query 3_1: What are the ten most expensive items (per unit price)
*and* thier suppliers?
"""

query_3_1 = """SELECT Product.ProductName,
                Product.UnitPrice, Supplier.CompanyName
                FROM Product
                INNER JOIN Supplier
                ON Product.SupplierId=Supplier.Id
                ORDER BY UnitPrice DESC
                LIMIT 10;
                """
item_and_supplier = cursor.execute(query_3_1).fetchmany(10)
print("The ten most expensive items and their suppliers are as follows:")
for item in item_and_supplier:
    print(item)
print(" \n")

"""Query 3_2: What is the largest category
(by number of unique products in it)?
"""

query_3_2 = """SELECT Category.CategoryName,
            COUNT(Product.ProductName) AS Num_Products
            FROM Category
            INNER JOIN Product
            on Product.CategoryId=Category.Id
            GROUP BY Category.CategoryName
            ORDER BY Num_Products DESC
            LIMIT 1
            ;
            """
largest_category = cursor.execute(query_3_2).fetchone()
largest_category = str(largest_category).strip('[]().')
category, num_products = largest_category.split()
category = str(category).strip("',")
print (f"{category.capitalize()} is the category with the largest number of products: {num_products}.")

"""Query 3_3 (*Stretch*): Who's the employee with the most territories?
Use 'TerritoryId' (not name, region, or other fields)
as the unique identifier for territories.
"""

query_3_3 = """SELECT Employee.FirstName,
                Employee.LastName,
                COUNT(EmployeeTerritory.TerritoryId)
                FROM Employee
                INNER JOIN EmployeeTerritory
                ON Employee.Id=EmployeeTerritory.EmployeeId
                GROUP BY EmployeeTerritory.EmployeeId
                ORDER BY COUNT(EmployeeTerritory.TerritoryId) DESC
                LIMIT 1;
                """
emp_most_territory = cursor.execute(query_3_3).fetchall()
emp_most_territory = str(emp_most_territory).strip('[](),')
first, last, num_ter = emp_most_territory.split()
first = str(first).strip("',")
last = str(last).strip("',")
print (" \n")
print(f"{first} {last} is the employee with the most territories: {num_ter}")