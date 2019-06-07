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
[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10518/38', 10518, 38, 263.5, 15, 0.0),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10540/38', 10540, 38, 263.5, 30, 0.0),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10541/38', 10541, 38, 263.5, 4, 0.1),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10616/38', 10616, 38, 263.5, 15, 0.05),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10672/38', 10672, 38, 263.5, 15, 0.1),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10783/38', 10783, 38, 263.5, 5, 0.0),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10805/38', 10805, 38, 263.5, 10, 0.0),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10816/38', 10816, 38, 263.5, 30, 0.05),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10817/38', 10817, 38, 263.5, 30, 0.0),
(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles',
263.5, 17, 0, 15, 0, '10828/38', 10828, 38, 263.5, 2, 0.0)]

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
