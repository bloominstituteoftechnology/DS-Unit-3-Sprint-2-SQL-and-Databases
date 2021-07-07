import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()
top_products = cur.execute('SELECT ProductName, UnitPrice FROM Product \
ORDER BY UnitPrice DESC LIMIT 10').fetchall()
print(top_products)
"""[('Côte de Blaye',), ('Thüringer Rostbratwurst',), ('Mishi Kobe Niku
 ("Sir Rodney's Marmalade",), ('Carnarvon Tigers',),
 ('Raclette Courdavault',), ('Manjimup Dried Apples',),
 ('Tarte au sucre',), ('Ipoh Coffee',), ('Rössle Sauerkraut',)]
 """
avg_age = cur.execute("SELECT avg(HireDate -BirthDate) \
FROM Employee").fetchall()
print(avg_age[0][0])
"""37.22222222222222"""
supply = cur.execute("SELECT ProductName, UnitPrice, CompanyName \
FROM Product \
INNER JOIN Supplier on Supplier.Id = Product.SupplierID \
ORDER BY UnitPrice DESC LIMIT 10").fetchall()
print(supply)
cat = cur.execute("SELECT CategoryName, COUNT(DISTINCT Product.Id) \
FROM Product \
INNER JOIN Category on Category.Id = Product.CategoryID \
GROUP BY CategoryName \
ORDER BY COUNT(DISTINCT Product.Id) DESC \
LIMIT 1 \
").fetchall()
print(cat[0][0])
"""Confections"""
conn.close()
# No changes so no need to commit
