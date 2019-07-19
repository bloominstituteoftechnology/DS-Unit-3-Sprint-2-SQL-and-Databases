import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curr = conn.cursor()

# # Schema
# schema = curr.execute('''SELECT sql FROM sqlite_master WHERE name="EmployeeTerritory"''').fetchall()
# print(schema)

# Part 2.
# Ten most expensive items.
pricy = curr.execute('''
SELECT  productname, unitprice
FROM product
ORDER BY unitprice DESC
LIMIT 10;''').fetchall()
print(f'Ten most expensive items: {list(pricy)}\n')

"""Ten most expensive items: 
[('Côte de Blaye', 263.5), 
('Thüringer Rostbratwurst', 123.79), 
('Mishi Kobe Niku', 97),
("Sir Rodney's Marmalade", 81), 
('Carnarvon Tigers', 62.5), 
('Raclette Courdavault', 55), 
('Manjimup Dried Apples', 53), 
('Tarte au sucre', 49.3), 
('Ipoh Coffee', 46), 
('Rössle Sauerkraut', 45.6)]
"""

# Average age of employee at hire.
emp_age = curr.execute('''
SELECT ROUND(AVG(hiredate - birthdate))
FROM employee;''').fetchall()
print(f'Average age of employee: {list(emp_age)}\n')

"""Average age of employee: [(37.0,)]
"""

# Average age of employee by city.
emp_age_city = curr.execute('''
SELECT city, ROUND(AVG(hiredate - birthdate)) age
FROM employee
GROUP BY city
ORDER BY age;''').fetchall()
print(f'Average age of employee by city: {list(emp_age_city)}\n')

"""Average age of employee by city: 
[('Kirkland', 29.0), 
('London', 33.0), 
('Seattle', 40.0), 
('Tacoma', 40.0), 
('Redmond', 56.0)
]"""

# Part 3.
# Most expensive items and their suppliers.
pricy_supply = curr.execute('''
SELECT productname, sup.companyname, prod.unitprice
FROM product prod
JOIN supplier sup
ON prod.supplierid = sup.id
ORDER BY unitprice DESC
LIMIT 10;''').fetchall()
print(f'Ten most expensive products and supplier: {list(pricy_supply)}/n')

"""Ten most expensive products and supplier: 
[('Côte de Blaye', 'Aux joyeux ecclésiastiques', 263.5), 
('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG', 123.79), 
('Mishi Kobe Niku', 'Tokyo Traders', 97), 
("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.', 81), 
('Carnarvon Tigers', 'Pavlova, Ltd.', 62.5), 
('Raclette Courdavault', 'Gai pâturage', 55), 
('Manjimup Dried Apples', "G'day, Mate", 53), 
('Tarte au sucre', "Forêts d'érables", 49.3), 
('Ipoh Coffee', 'Leka Trading', 46), 
('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG', 45.6)]/n
"""

# Most common categories.
comm_cat = curr.execute('''
SELECT productname, COUNT(productname) count
FROM product
JOIN category
ON product.categoryid=category.id
ORDER BY count DESC
LIMIT 1''').fetchall()
print(f'Largest category: {list(comm_cat)}\n')

"""Largest category: [('Original Frankfurter grüne Soße', 77)]
"""

# Employee with most territories.
most_territory = curr.execute('''
SELECT firstname, lastname, COUNT(terr.territoryid) count 
FROM employee
JOIN employeeterritory terr
ON employee.id=terr.employeeid
GROUP BY employee.id
ORDER BY count DESC 
LIMIT 1''').fetchall()
print(f'Employee with most territories: {list(most_territory)}\n')

"""Employee with most territories: [('Robert', 'King', 10)]
"""

