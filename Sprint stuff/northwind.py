import sqlite3

# connection and cursors
conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()

# Queries
Q_1 = curs.execute("""SELECT Product.UnitPrice
FROM Product
ORDER BY Product.UnitPrice DESC
LIMIT 10
;""")
Q_2 =  curs.execute("""select AVG(HireDate - BirthDate)
from Employee;
""")
Stretchg_1 = curs.execute("""select AVG(HireDate - BirthDate), City
from Employee
Group By City;
""")

# Other Part

Q_3 = curs.execute("""SELECT Product.Id, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier
ON Product.id
ORDER BY Product.UnitPrice DESC
LIMIT 10
;""")
Q_4 = curs.execute("""SELECT COUNT(DISTINCT Category.CategoryName), Category.CategoryName
FROM Category
JOIN Product
ON Category.id
ORDER BY COUNT(Category.CategoryName) DESC
LIMIT 1
;""")
Stretchg_2 = curs.execute("""SELECT COUNT(DISTINCT Employee.FirstName), Employee.LastName, Employee.FirstName
FROM Employee
JOIN EmployeeTerritory
ON Employee.Id = EmployeeTerritory.EmployeeId
JOIN Territory
ON EmployeeTerritory.TerritoryId = Territory.Id
ORDER BY COUNT(DISTINCT Employee.FirstName) desc
LIMIT 1;""")

conn.commit()
