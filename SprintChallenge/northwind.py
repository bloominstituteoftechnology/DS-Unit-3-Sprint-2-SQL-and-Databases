import sqlite3

# Create connection and cursor
sl_conn = sqlite3.connect('SprintChallenge/northwind_small (2).sqlite3')
sl_cur = sl_conn.cursor()

# 10 most expensive products
print('Most expensive products:')
query = f'''
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;'''
high_cost = sl_cur.execute(query).fetchall()
print(high_cost)

# Average employee age at time of hiring
print('\nAverage employee age at time of hiring:')
query = f'SELECT AVG(HireDate - BirthDate) FROM Employee;'
avg_age = sl_cur.execute(query).fetchall()
print(avg_age[0][0])

# Average employee age at time of hiring by city
print('\nAverage employee age at time of hiring by city:')
query = f'''
SELECT AVG(HireDate - BirthDate)
FROM Employee
GROUP BY PostalCode'''
age_by_city = sl_cur.execute(query).fetchall()
print(age_by_city)

# 10 most expensive products with corresponding suppliers
print('\nMost expensive products and their suppliers:')
query = f'''
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier ON SupplierId
ORDER BY UnitPrice DESC
LIMIT 10;'''
prod_supp = sl_cur.execute(query).fetchall()
print(prod_supp)

# Largest category (by number of unique products in it)
print('\nLargest category (by number of unique products):')
query = f'''
SELECT CategoryName
FROM Category
JOIN Product ON CategoryId
ORDER BY CategoryId, ProductName
LIMIT 1;'''
large_cat = sl_cur.execute(query).fetchall()
print(large_cat[0][0])

# Employee with the most territories
print('\nEmployee with the most territories:')
query = f'''
SELECT FirstName, LastName
FROM Employee
JOIN EmployeeTerritory ON EmployeeId
ORDER BY EmployeeId, TerritoryId DESC
LIMIT 1;'''
most_terr = sl_cur.execute(query).fetchall()
print(most_terr[0])
