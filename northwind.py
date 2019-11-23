import sqlite3
#PART 2
connect = sqlite3.connect()
cursor = connect.cursor()

query = '''
SELECT UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
;
'''
cursor.execute(query).fetchall()

query = '''
SELECT AVG(HireDate - BirthDate)
FROM Employee
;
'''
cursor = connect.cursor()
cursor.execute(query).fetchall()

query = '''
SELECT AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City
;
'''
#PART 3
query = '''
SELECT Product.UnitPrice*OrderDetail.Quantity, Product.SupplierID 
FROM (Product JOIN OrderDetail WHERE Product.ProductID = OrderDetail.ProductID)
ORDER BY UnitPrice*Quantity
LIMIT 10
;
'''
cursor = connect.cursor()
cursor.execute(query).fetchall()

query = '''
SELECT Category.CategoryName
FROM (Category JOIN Product WHERE Category.CategoryID = Product.CategoryID)
LIMIT 1
ORDER BY COUNT(DISTINCT ProductID)
;
'''

