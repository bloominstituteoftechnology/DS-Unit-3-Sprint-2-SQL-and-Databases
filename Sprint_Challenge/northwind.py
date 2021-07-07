import sqlite3

# form a connection to 'northwind_small' db
conn = sqlite3.connect('northwind_small.sqlite3')

# create a cursor
curs = conn.cursor()

# What are the ten most expensive products?
answer_1 = """
SELECT ProductName
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
print('The Ten most Expensive products are: \n', curs.execute(answer_1).fetchall(), '\n\n')

# What is the average age of an employee at the time 
# of their hiring? (Hint: a lot of arithmetic works with dates.)
answer_2 = """
SELECT ROUND(AVG(HireDate - BirthDate))
FROM Employee;
"""

print('Average age at time of hiring is: \n', curs.execute(answer_2).fetchone()[0], '\n\n')

# (Stretch) How does the average age of employee at hire vary by city?
stretch_1 = """
SELECT City, ROUND(AVG(HireDate - BirthDate))
FROM Employee
GROUP BY City;
"""
print('Average age at time of hire by city: \n', curs.execute(stretch_1).fetchall(), '\n\n')

# What are the ten most expensive items (per unit price) in the database 
# and their suppliers?
answer_3 = """
SELECT p.ProductName, s.CompanyName
FROM Product AS p, Supplier AS s
WHERE p.SupplierID = s.Id
ORDER BY p.UnitPrice DESC
LIMIT 10;
"""

print('The ten most expensive items and their suppliers are: \n', curs.execute(answer_3).fetchall(), '\n\n')

# What is the largest category (by number of unique products in it)?
answer_4 = """
SELECT DISTINCT COUNT(*), Product.CategoryID, Category.CategoryName
FROM Product JOIN Category ON Product.CategoryID = Category.Id
GROUP BY Product.CategoryID
ORDER BY COUNT(*) DESC
"""

print('Largest category by number of unique products is: \n', curs.execute(answer_4).fetchone(), '\n\n')


# (Stretch) Who's the employee with the most territories? Use 
# TerritoryId (not name, region, or other fields) as the unique 
# identifier for territories.

stretch_2 = """
SELECT Employee.FirstName, Employee.LastName, COUNT(Territory.Id)
FROM Employee, Territory, EmployeeTerritory
WHERE Employee.Id = EmployeeTerritory.EmployeeID AND Territory.Id = EmployeeTerritory.TerritoryID
GROUP BY Employee.Id
ORDER BY COUNT(Territory.Id) DESC;
"""
print('Employee with most territories: \n', curs.execute(stretch_2).fetchone(), '\n\n')

