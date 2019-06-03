import sqlite3

# initialize connection
sql3_conn = sqlite3.connect('northwind_small.sqlite3')
sql3_curs = sql3_conn.cursor()

# ten most expensive items
sql3_stmt = """SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC;
    """
results  = sql3_curs.execute(sql3_stmt).fetchmany(10)
print ('The ten most expensive items (per unit price) in the database are:')
for result in results:
    print(result)

# average age of an employee at the time of their hiring
sql3_stmt = """SELECT AVG(HireDate - BirthDate)
    FROM Employee;
    """
print("\nThe average age of an employee at the time of their hiring is:",
      sql3_curs.execute(sql3_stmt).fetchone()[0])

# ten most expensive items (per unit price) in the database and their suppliers
sql3_stmt = """SELECT Product.ProductName, Supplier.CompanyName
    FROM Product, Supplier
    WHERE Product.SupplierID = Supplier.ID
    ORDER BY UnitPrice DESC;
    """
results  = sql3_curs.execute(sql3_stmt).fetchmany(10)
print ('\nThe ten most expensive items (per unit price) and their suppliers in the database are:')
for result in results:
    print(result)

# largest category (by number of products in it)
sql3_stmt = """SELECT CategoryName, COUNT(ProductName)
    FROM Category, Product
    WHERE Category.Id = Product.CategoryId
    GROUP BY Product.CategoryId
    ORDER BY COUNT(Product.ProductName) DESC;
    """
print("\nThe largest category (by number of products in it) is:",
      sql3_curs.execute(sql3_stmt).fetchone()[0])
