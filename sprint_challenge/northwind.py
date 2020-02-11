import sqlite3

DB_FILEPATH = ("northwind_small.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

# Begin Part 2 queries

most_expensive_prod = """
    SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""

curs.execute(most_expensive_prod)

avg_emp_age = """
    SELECT AVG(
        CAST((julianday(HireDate) - julianday(BirthDate)) / 365 AS INTEGER))
    FROM Employee
"""

curs.execute(avg_emp_age)

avg_emp_age_stretch = """
    SELECT AVG(
        CAST((julianday(HireDate) - julianday(BirthDate)) / 365 AS INTEGER))
    FROM Employee
    GROUP BY City
"""

curs.execute(avg_emp_age_stretch)

# Begin Part 3 queries
most_expensive_plus_suppliers = """
    SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
    FROM Product
    JOIN Supplier on Supplier.Id = Product.SupplierId
    ORDER BY Product.UnitPrice DESC
    LIMIT 10
"""

curs.execute(most_expensive_plus_suppliers)

largest_category = """
    SELECT MAX(ProductCount), CategoryName
    FROM(SELECT COUNT(DISTINCT ProductName) as ProductCount,
    Category.CategoryName as CategoryName
    FROM Product
    LEFT JOIN Category on Category.Id = Product.CategoryId
    GROUP BY CategoryId)
"""

curs.execute(largest_category)

emp_w_most_territories = """
    SELECT MAX(MostTerritories) as TerritoryCount, FirstName, LastName
    FROM(SELECT COUNT(EmployeeID) as MostTerritories,
    Employee.FirstName as FirstName, Employee.LastName as LastName
    FROM EmployeeTerritory
    LEFT JOIN Employee on Employee.Id = EmployeeTerritory.EmployeeId
    )
"""
