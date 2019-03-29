import sqlite3

# Connect to existing northwind_small.sqlite3 file

# Create cursor
curs = conn.cursor()

# Queries
ten_most_exp_items = """
SELECT ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

employee_avg_age = """
SELECT AVG(Cast ((
	julianday(Employee.HireDate)/365 - julianday(Employee.BirthDate)/365
	) AS INTEGER))
FROM Employee;
"""

avg_age_by_city = """
SELECT Employee.City, AVG(Cast ((
	julianday(Employee.HireDate)/365 - julianday(Employee.BirthDate)/365
	) AS INTEGER))
FROM Employee
GROUP BY Employee.City;
"""
ten_most_exp_items_supplier = """
SELECT s.CompanyName, p.ProductName, p.UnitPrice FROM Supplier AS s, Product AS p
WHERE s.Id = p.SupplierId
ORDER BY p.UnitPrice DESC
LIMIT 10;
"""

largest_category = """
SELECT c.CategoryName, COUNT(c.CategoryName) FROM Category AS c, Product AS p
WHERE c.Id = p.CategoryId
GROUP BY c.CategoryName
ORDER BY COUNT(c.CategoryName) DESC
LIMIT 1;
"""

# Print part 2 results
print('Ten most expensive items:', curs.execute(ten_most_exp_items).fetchall())
print('Average age of employee at time of hiring:', curs.execute(employee_avg_age).fetchall())
print('Average age of employee at time of hiring (by City):', curs.execute(avg_age_by_city).fetchall())

# Print part 3 results
print('10 most expensive items and their supplier:', curs.execute(ten_most_exp_items_supplier).fetchall())
print('Largest category:', curs.execute(largest_category).fetchall())

# Part 2 Outputs
# Ten most expensive items: [('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]
# Average age of employee at time of hiring: [(36.77777777777778,)]
# Average age of employee at time of hiring (by City): [('Kirkland', 28.0), ('London', 32.25), ('Redmond', 55.0), ('Seattle', 39.5), ('Tacoma', 40.0)]

# Part 3 Outputs
# 10 most expensive items and their supplier: [('Aux joyeux ecclésiastiques', 'Côte de Blaye', 263.5), ('Plutzer Lebensmittelgroßmärkte AG', 'Thüringer Rostbratwurst', 123.79), ('Tokyo Traders', 'Mishi Kobe Niku', 97), ('Specialty Biscuits, Ltd.', "Sir Rodney's Marmalade", 81), ('Pavlova, Ltd.', 'Carnarvon Tigers', 62.5), ('Gai pâturage', 'Raclette Courdavault', 55), ("G'day, Mate", 'Manjimup Dried Apples', 53), ("Forêts d'érables", 'Tarte au sucre', 49.3), ('Leka Trading', 'Ipoh Coffee', 46), ('Plutzer Lebensmittelgroßmärkte AG', 'Rössle Sauerkraut', 45.6)]
# Largest category: [('Confections', 13)]
