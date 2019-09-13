import sqlite3


# Connect to database & instantiate cursor
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
curs.execute('''SELECT ProductName, UnitPrice
                FROM Product
                ORDER BY UnitPrice DESC
                LIMIT 10;''').fetchall()

# What is the average age of an employee at the time of their hiring?
curs.execute('''SELECT AVG(HireDate - BirthDate)
                FROM Employee;''').fetchall()

# How does the average age of employee at hire vary by city?
curs.execute('''SELECT AVG(age), City
                FROM(
                SELECT
                (JULIANDAY(HireDate) - JULIANDAY(BirthDate))/365 as age, City
                FROM Employee
                )
                GROUP BY City;''').fetchall()

# What are the ten most expensive items (per unit price) in the database *and*
# their suppliers?
curs.execute('''SELECT CompanyName, ProductName, UnitPrice
                FROM Product, Supplier
                GROUP BY ProductName
                ORDER BY UnitPrice DESC
                LIMIT 10;''').fetchall()

# What is the largest category (by number of unique products in it)?
curs.execute('''SELECT x.CategoryName, COUNT(y.CategoryID)
                FROM Product AS y
                INNER JOIN Category AS x
                ON y.CategoryID=x.ID
                GROUP BY x.ID
                ORDER BY COUNT(y.CategoryID) DESC
                LIMIT 1;''').fetchall()

# Who's the employee with the most territories?
curs.execute('''SELECT FirstName, LastName, MAX(num)
                FROM (
                SELECT FirstName, LastName, COUNT(DISTINCT TerritoryId) AS num
                FROM Employee as x LEFT JOIN EmployeeTerritory as y
                ON x.Id = y.EmployeeId
                GROUP BY EmployeeId
                );''').fetchall()
