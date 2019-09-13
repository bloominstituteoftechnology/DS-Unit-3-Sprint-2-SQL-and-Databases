import sqlite3


con = sqlite3.connect('northwind_small.sqlite3')
curs = con.cursor()

q1 = '''
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''

mostExp = curs.execute(q1).fetchall()

q2 = '''
SELECT Product.ProductName, Supplier.CompanyName, Product.UnitPrice
FROM Product
INNER JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
'''

mostExpSup = curs.execute(q2).fetchall()

q3 = '''
SELECT Category.CategoryName, COUNT(Category.CategoryName)
FROM Product
INNER JOIN Category
ON Category.Id = Product.CategoryId
GROUP BY Category.CategoryName
ORDER BY COUNT(Category.CategoryName) DESC
LIMIT 1;
'''

commonCat = curs.execute(q3).fetchall()
