import sqlite3
connect = sqlite3.connect('C:/Users/Donaldo/Downloads/northwind_small.sqlite3')
cursor = connect.cursor()

expensive_items = """SELECT ProductName, UnitPrice 
FROM Product ORDER BY UnitPrice DESC"""
expensive_items = cursor.execute(expensive_items).fetchmany(10)

# Top 10 most expensive items
for item in expensive_items:
    print(item[0])

average_employee_age = 'SELECT AVG(HireDate - BirthDate) FROM Employee'
average_employee_age = cursor.execute(average_employee_age).fetchone()[0]

#Average age of an amployee when hired
print(average_employee_age)

expensive_things = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product, Supplier
WHERE Product.SupplierID = Supplier.ID
ORDER BY UnitPrice DESC"""

expensive_things = cursor.execute(expensive_things).fetchmany(10)
#Top ten most expensive items with their suppliers
for item in expensive_things:
    print('Item: ',item[0], '\nSupplier: ', item[2])

largest_category = """
SELECT Category.CategoryName, COUNT(Category.CategoryName)
FROM Category, Product
WHERE Product.CategoryID = Category.ID
GROUP BY Category.CategoryName
ORDER BY COUNT(Category.CategoryName) DESC"""

largest_category = cursor.execute(largest_category).fetchone()

#The largest category by number of products
print(largest_category[0])