import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


print(curs.execute("SELECT DISTINCT(Product.ProductName) FROM Product, OrderDetail WHERE "
                   "Product.ID = OrderDetail.ProductID ORDER BY "
                   "OrderDetail.UnitPrice DESC LIMIT 10;").fetchall())

"""
Most Expensive products

"""
"""
[('Côte de Blaye',), ('Thüringer Rostbratwurst',),
 ('Mishi Kobe Niku',), ("Sir Rodney's Marmalade",),
  ('Carnarvon Tigers',), ('Raclette Courdavault',),
   ('Manjimup Dried Apples',), ('Tarte au sucre',),
    ('Ipoh Coffee',), ('Rössle Sauerkraut',)]

"""

"""
Average age at hire
"""
print(curs.execute("SELECT AVG(Employee.HireDate - Employee.BirthDate)"
                   " FROM Employee").fetchall())
"""
[(37.22222222222222,)]

"""
print("Most expensive products and their suppliers")
print(curs.execute("SELECT * FROM Product, Supplier, OrderDetail "
                   "WHERE Product.ID = OrderDetail.ProductID AND "
                   "Product.SupplierID = Supplier.ID ORDER BY "
                   "OrderDetail.UnitPrice DESC LIMIT 10;").fetchall())

"""
[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0, 18,
 'Aux joyeux ecclésiastiques',
 'Guylène Nodier', 'Sales Manager', '203, Rue des Francs-Bourgeois', 'Paris', 'Western Europe', '75004',
  'France', '(1) 03.83.00.68', '(1) 03.83.00.62', None, '10518/38', 10518, 38, 263.5, 15, 0.0),
   ............
"""
"""
Most popular category
"""
print("Most popular category")
print(curs.execute("SELECT Category.CategoryName FROM Product, Category WHERE "
                   "Product.CategoryID = Category.ID GROUP BY "
                   "Category.CategoryName ORDER BY count(*) "
                   "DESC LIMIT 1").fetchall())
"""
[('Confections',)]

"""
