import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

curs = conn.cursor()

###Part 2

print('Start of Part 2')
print()

qury1 ='select ProductName, UnitPrice from Product order by UnitPrice DESC LIMIT 10'
print(curs.execute(qury1).fetchall())

query2 = 'select avg(HireDate-BirthDate) from Employee'
print(curs.execute(query2).fetchall())

query3 = 'select city, avg(HireDate-BirthDate) from Employee group by city'
print(curs.execute(query3).fetchall())
print()

###Part 3

print(' Start of Part 3')
print()



query1 = 'select Supplier.CompanyName, Product.ProductName, Product.UnitPrice from Product, Supplier ' \
         'where Product.SupplierId=Supplier.id order by Product.UnitPrice DESC LIMIT 10'
print(curs.execute((query1)).fetchall())

query2 = 'select Category.CategoryName, count(*) as Number_Products ' \
         'from Product,Category where Product.CategoryId=Category.Id ' \
         'group by Category.Id order by Number_Products DESC LIMIT 1'
print(curs.execute(query2).fetchall())

query3 = 'SELECT Employee.FirstName, Employee.LastName, count(DISTINCT EmployeeTerritory.TerritoryId) as Number_Territory ' \
         'from Employee, EmployeeTerritory ' \
         'where EmployeeTerritory.EmployeeId = Employee.Id group by EmployeeId ' \
         'order by Number_Territory DESC limit 1'
print(curs.execute(query3).fetchall())


