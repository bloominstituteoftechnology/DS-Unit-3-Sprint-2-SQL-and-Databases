import sqlite3

conn = sqlite3.connect('SC/northwind_small.sqlite3')

curs = conn.cursor()

# Top ten highest prices
top_ten = 'SELECT UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10'
print('Ten highest prices:', curs.execute(top_ten).fetchall())

# Average age of employees
age_avg = 'SELECT AVG(2019 - BirthDate) FROM Employee'
print('Average age of employees:', curs.execute(age_avg).fetchone())

# Average age by city
age_by_city = 'SELECT AVG(2019 - BirthDate) FROM Employee GROUP BY City'
print('Average age by city:', curs.execute(age_by_city).fetchall())

# Ten most expensive items and their suppliers
expensive_suppliers = '''
SELECT UnitPrice, CompanyName AS Supplier FROM (
Product
INNER JOIN Supplier ON Product.SupplierId=Supplier.Id
)
ORDER BY UnitPrice DESC LIMIT 10
'''
print('Ten most expensive items and their suppliers:',
      curs.execute(expensive_suppliers).fetchall())

# Largest category by number of unique products
diverse_categories = '''
SELECT CategoryName, MAX(Diversity) FROM (
SELECT COUNT(DISTINCT ProductName) AS Diversity, CategoryName FROM (
Product
INNER JOIN Category ON Product.CategoryId=Category.Id
)
GROUP BY CategoryName
ORDER BY COUNT(DISTINCT ProductName))
'''
print('Largest category by number of unique products:',
      curs.execute(diverse_categories).fetchall())

# Employee with most territories
most_territories = '''
SELECT FirstName, LastName, MAX(Territories)
FROM (
Employee
INNER JOIN (
SELECT COUNT(DISTINCT TerritoryId) AS Territories, EmployeeId
FROM (
EmployeeTerritory
INNER JOIN Territory ON EmployeeTerritory.TerritoryId=Territory.Id)
GROUP BY EmployeeId
ORDER BY Territories) AS EmpTer ON EmpTer.EmployeeId=Employee.Id)
'''
print('Employee with most territories and number of those territories:',
      curs.execute(most_territories).fetchall())

conn.close()
