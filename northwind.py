import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()
query = '''SELECT ProductName FROM Product
ORDER BY UnitPrice DESC
LIMIT 10'''
curs.execute(query)
results = curs.fetchall()
print('Ten most expensive items (per unit price):')
for result in results:
    print(result[0])

query = '''SELECT avg(HireDate - BirthDate)
FROM Employee'''
curs.execute(query)
print('Average age of an employee at the time of their hiring:', curs.fetchall()[0][0])

query = '''SELECT City, avg(HireDate - BirthDate) as Age
FROM Employee
GROUP BY City'''
curs.execute(query)
print('Average age of an employee at the time of their hiring by city:')
results = curs.fetchall()
for result in results:
    print(result[0], result[1])

query = '''SELECT ProductName, CompanyName FROM Product
INNER JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10'''
curs.execute(query)
results = curs.fetchall()
print('Ten most expensive items (per unit price) and their suppliers:')
print('Product', 'Supplier', sep='\t\t\t')
for result in results:
    if len(result[0]) > 15:
        sep = '\t'
    else:
        sep = '\t\t'
    print(result[0], result[1], sep=sep)

query = '''SELECT CategoryName, count(Product.Id) as ProductCount FROM Category
INNER JOIN Product
ON Category.Id = Product.CategoryId
GROUP BY CategoryId
ORDER BY ProductCount DESC
LIMIT 1'''
curs.execute(query)
print('Largest category (by number of products in it):', curs.fetchall()[0][0])

query = '''SELECT LastName, FirstName, count(Territory.TerritoryDescription) as TerritoryCount
FROM Employee, Territory
JOIN EmployeeTerritory
ON Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY Employee.Id
ORDER BY TerritoryCount DESC
LIMIT 1'''
curs.execute(query)
results = curs.fetchall()
print('Employee with the most territories, and number of territories they have:',
        results[0][1], results[0][0] + ';', results[0][2])
