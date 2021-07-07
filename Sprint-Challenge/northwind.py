import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
curs.execute(
"""
SELECT
    UnitPrice
FROM
    Product
ORDER BY
    UnitPrice DESC
LIMIT
    10;
"""
)

#What is the average age of an employee at the time of their hiring?
curs.execute(
"""
SELECT
    round(avg(HireDate - BirthDate), 1)
FROM
    Employee;
"""
)

# What are the ten most expensive items (per unit price) in the database and
# their suppliers?
curs.execute(
"""
SELECT
    UnitPrice,
	SupplierId,
	SupplierName
FROM
	Product
INNER JOIN Supplier ON Supplier.SupplierId = Product.SupplierId
ORDER BY
    UnitPrice DESC
LIMIT
    10;
"""
)

# What is the largest category (by number of products in it)?
curs.execute(
"""
SELECT
	Category.Id,
	Category.CategoryName,
	COUNT(Product.Id)
FROM
	Product
JOIN Category ON Category.Id = Product.CategoryId
GROUP BY
	Category.CategoryName
ORDER BY COUNT(Product.Id) DESC
LIMIT 1;
"""
)
