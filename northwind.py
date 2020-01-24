import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
query = """
SELECT DISTINCT ProductName
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
response = curs.execute(query).fetchall()
item_list = [item[0] for item in response]
print("The ten most expensive items per unit price are:")
for item in item_list:
    print(item)

# What is the average age of an employee at the time of their hiring?
query = """
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""
response = curs.execute(query).fetchall()[0][0]
print(round(response), 'is the average age of an employee at the time of hiring, rounded to the nearest year.')