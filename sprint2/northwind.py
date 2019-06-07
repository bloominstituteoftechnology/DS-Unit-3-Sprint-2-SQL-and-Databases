import sqlite3

# Connect to northwind_small database
conn = sqlite3.connect('northwind_small.sqlite3')

# Read through its database to query later on
curs = conn.cursor()

# Save db in result_product
result_10 = curs.execute('SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;').fetchall()
print('Top 10 expensive items:', result_10)

result_avg_age = curs.execute('SELECT HireDate, AVG(HireDate - BirthDate) FROM Employee GROUP BY HireDate').fetchall()
print('Avg age of employees at hiring date:', result_avg_age)

result_city = curs.execute('SELECT City, HireDate, AVG(HireDate - BirthDate) FROM Employee GROUP BY City').fetchall()
print('Avg age of employees at hiring date by city:', result_city)