import sqlite3

# Connect to given northwind database
conn = sqlite3.connect('northwind_small.sqlite3')

# Make a cursor
curs = conn.cursor()

# Answer for part 2, Execute each result
# Top 10 most expensive items in the database
top_10 = curs.execute('SELECT ProductName, UnitPrice FROM Product ORDER BY Unitprice DESC LIMIT 10;').fetchall()
print('Top 10 most expensive items:', top_10)


# Average age of an employee at the time of their hiring
avg_age = curs.execute('SELECT ROUND(AVG(HireDate - BirthDate), 2) FROM Employee').fetchall()
print('Avg age of an employee at the time of hiring:', avg_age[0][0])


#Average age of an employee at hire vary by city
avg_age_city = curs.execute('SELECT City, HireDate, AVG(HireDate - BirthDate) FROM Employee GROUP BY City;').fetchall()
print('Avg age of an employee at hire vary by city:', avg_age_city)


# Answer for part 3, Execute each result
# Top 10 most expensive items in the database and their suppliers
top_10_sup = curs.execute('SELECT p.ProductName, s.CompanyName, p.UnitPrice FROM Supplier AS s INNER JOIN Product AS p ON SupplierID ORDER BY UnitPrice DESC LIMIT 10;').fetchall()
print('Top 10 most expensive items and their supplier', top_10_sup)


# Largest category by number of unique products in it
L_category = curs.execute('SELECT CategoryID, COUNT(p.ProductName) FROM Category AS c INNER JOIN Product as p ON CategoryID GROUP BY CategoryID ORDER BY COUNT(p.ProductName) DESC LIMIT 1;').fetchall()
print('Largest category,', L_category[0][0], ', by number of unique products in it' , L_category[0][1])


# Most territories
most_territories = curs.execute('SELECT EmployeeID, COUNT(TerritoryDescription) FROM EmployeeTerritory INNER JOIN Territory ON TerritoryID GROUP BY EmployeeID ORDER BY COUNT(TerritoryDescription) DESC LIMIT 1;').fetchall()
print('EmployeeID number:,', most_territories[0][0], ', with the most territory:', most_territories[0][1])
