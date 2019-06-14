import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

curs.execute('''SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10''')
print('1. ', curs.fetchall())

curs.execute('SELECT AVG(Employee.HireDate-Employee.BirthDate) FROM Employee')
print('2. ', curs.fetchall())

curs.execute('''SELECT ProductName, UnitPrice, CompanyName 
FROM Product, Supplier
ON Product.SupplierId=Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10''')
print('3. ', curs.fetchall())

curs.execute('''SELECT COUNT(*)
FROM Category, Product
WHERE Category.Id=Product.CategoryId
AND CategoryName='Beverages'
''')
print('Beverages: ', curs.fetchall())

curs.execute('''SELECT COUNT(*)
FROM Category, Product
WHERE Category.Id=Product.CategoryId
AND CategoryName='Condiments'
''')
print('Condiments: ', curs.fetchall())

curs.execute('''SELECT COUNT(*)
FROM Category, Product
WHERE Category.Id=Product.CategoryId
AND CategoryName='Confections'
''')
print('Confections: ', curs.fetchall())

curs.execute('''SELECT COUNT(*)
FROM Category, Product
WHERE Category.Id=Product.CategoryId
AND CategoryName='Dairy Products'
''')
print('Dairy Products: ', curs.fetchall())

curs.execute('''SELECT COUNT(*)
FROM Category, Product
WHERE Category.Id=Product.CategoryId
AND CategoryName='Grains/Cereals'
''')
print('Grains/Cereals: ', curs.fetchall())

curs.execute('''SELECT COUNT(*)
FROM Category, Product
WHERE Category.Id=Product.CategoryId
AND CategoryName='Meat/Poultry'
''')
print('Meat/Poultry: ', curs.fetchall())

curs.execute('''SELECT COUNT(*)
FROM Category, Product
WHERE Category.Id=Product.CategoryId
AND CategoryName='Produce'
''')
print('Produce: ', curs.fetchall())

curs.execute('''SELECT COUNT(*)
FROM Category, Product
WHERE Category.Id=Product.CategoryId
AND CategoryName='Seafood'
''')
print('Seafood: ', curs.fetchall())