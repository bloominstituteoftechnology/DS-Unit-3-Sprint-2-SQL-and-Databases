import sqlite3


# Instantiate connection to database and initialize cursor
conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()


# Query for top ten most expensive products
query = """
    SELECT UnitPrice
    FROM Product 
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""
curs.execute(query)
print(curs.fetchall())


# Query for average age of employees
query = """
    SELECT AVG(HireDate) - AVG(BirthDate)
    FROM  Employee
"""
curs.execute(query)
print(curs.fetchall())


# Query for top ten expensive products and their suppliers
query = """
    SELECT UnitPrice, Supplier.CompanyName
    FROM Product
    INNER JOIN Supplier
    ON Product.SupplierID = Supplier.ID
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""
curs.execute(query)
print(curs.fetchall())


# Query for the largest category
query = """
    SELECT MAX(DISTINCT(CategoryID)), Category.CategoryName
    FROM Product
    INNER JOIN Category
    ON Product.CategoryID = Category.ID
"""
curs.execute(query)
print(curs.fetchall())


curs.close()
conn.commit()
