import sqlite3 as sql

connect = sql.connect('northwind_small.sqlite')
curs = connect.cursor()

high_price = '''SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;'''
curs.execute(high_price)
curs.fetchall()

avg_age_hired = '''SELECT AVG(HireDate - BirthDate)
    FROM employee'''

age_hire_city = '''SELECT AVG(HireDate - BirthDate)
    FROM employee
    GROUP BY City'''

# # # # # # ################ PART 3 #######################
expense_supplier = '''SELECT Supplier.CompanyName, Product.ProductName, Product.UnitPrice
    FROM Product 
    JOIN Supplier  ON Supplier.Id = Product.SupplierId
    ORDER BY UnitPrice DESC
    LIMIT 10;'''

largest_cat = '''SELECT Category.CategoryName, COUNT(Product.Id) prod_count
    FROM Product 
    JOIN Category ON Category.Id = Product.CategoryId
    GROUP BY Category.CategoryName
    ORDER BY COUNT(Product.Id) DESC
    LIMIT 1;'''

top_terr = '''SELECT Territory.TerritoryDescription, COUNT(Employee.Id) as employee_count
    FROM EmployeeTerritory 
    JOIN Territory ON Territory.Id = EmployeeTerritory.TerritoryId
    JOIN Employee on Employee.Id = EmployeeTerritory.EmployeeId
    GROUP BY TerritoryDescription
    ORDER BY COUNT(Employee.Id) DESC
    LIMIT 1;'''

most_terrs = '''SELECT Employee.Id, Employee.LastName, Employee.FirstName,
    COUNT(DISTINCT EmployeeTerritory.TerritoryId) count_territories
    FROM EmployeeTerritory
    JOIN Employee on Employee.Id = EmployeeTerritory.EmployeeId
    GROUP BY Employee.Id
    ORDER BY COUNT(distinct EmployeeTerritory.TerritoryId) DESC
    LIMIT 1;'''