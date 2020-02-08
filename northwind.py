import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

query = '''SELECT Id, ProductName, UnitPrice 
            FROM Product 
            ORDER BY UnitPrice DESC 
            LIMIT 10'''
results = curs.execute(query).fetchall()
print('Ten most expensive items (by unit price):', results)

query = '''SELECT AVG(HireAge) FROM 
            (SELECT HireDate - BirthDate AS HireAge FROM Employee)'''
results = curs.execute(query).fetchone()
print('Average employee age at time of hire:', results)

query = '''SELECT AVG(HireAge), City FROM (
            SELECT
                LastName,
                FirstName,
                City,
                HireDate - BirthDate AS HireAge
            FROM
                Employee)
            GROUP BY City'''
results = curs.execute(query).fetchall()
print('Comparison of average employee age at time of hire by city:', results)

query = '''SELECT Product.Id, Product.ProductName, Product.UnitPrice, 
            Supplier.CompanyName
            FROM Product
            LEFT JOIN Supplier ON Product.SupplierId = Supplier.Id
            ORDER BY UnitPrice DESC 
            LIMIT 10'''
results = curs.execute(query).fetchall()
print('Ten most expensive items (by unit price), with supplier:', results)

query = '''SELECT Product.CategoryId, 
            Category.CategoryName, 
            COUNT(DISTINCT Product.ProductName) AS ProductCount
            FROM Product
            LEFT JOIN Category ON Product.CategoryId = Category.Id
            GROUP BY 2
            ORDER BY ProductCount DESC
            LIMIT 1'''
results = curs.execute(query).fetchall()
print('Largest Category:', results[0][1], ', with', results[0][2])

query = '''SELECT Employee.Id,
                Employee.LastName,
                Employee.FirstName,
                COUNT(EmployeeTerritory.TerritoryId) AS territory_count
            FROM Employee
            LEFT JOIN 
                EmployeeTerritory ON Employee.Id = EmployeeTerritory.EmployeeId
            GROUP BY Employee.Id
            ORDER BY territory_count DESC
            LIMIT 1'''
results = curs.execute(query).fetchall()
print('Employee with most territories:', 
        results[0][2], 
        results[0][1], 
        ', with', 
        results[0][3])