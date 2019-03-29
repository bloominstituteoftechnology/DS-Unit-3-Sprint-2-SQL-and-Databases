import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Test the connection, get names for all tables
print('Connection is working, here are the tables names:',
      curs.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY
      name;""").fetchall())

# The ten most expensive items per unit price
q = """SELECT ProductName, UnitPrice FROM Product
       ORDER BY UnitPrice DESC LIMIT 10"""

print('Ten most expensive items:', curs.execute(q).fetchall())

# Average age of an employee at the time of their hiring
q = """SELECT AVG(substr(HireDate, 1, 4) - substr(BirthDate, 1, 4))
        FROM Employee"""

print('Average age of employee at time of hiring:', curs.execute(q).fetchall())

# Stretch: how does the average age of an employee at hire vary by city?

# What are the ten most expensive items in the db and their suppliers
q = """SELECT ProductName, UnitPrice, CompanyName FROM Product
    JOIN supplier
    ON Product.supplierId = Supplier.id
    ORDER BY UnitPrice DESC LIMIT 10;"""

print('Ten most expensive items and the comapies that supply them:',
      curs.execute(q).fetchall())

# What is the largest category by number of unique products?
q = """SELECT CategoryName, COUNT(*)
       FROM Product JOIN Category
       ON Product.CategoryId = Category.Id
       GROUP BY CategoryName
       ORDER BY COUNT(*) DESC"""

print('Number of unique products per category:', curs.execute(q).fetchall())

# Stretch: What is the name of the employee with the most territories?
# Use `TerritoryId`(not name, region, or other fields) as the unique identifier
# for territories.
