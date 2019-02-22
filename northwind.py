import sqlite3

# New database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()





# Part 2


# What are the ten most expensive items (per unit price) in the database?

curs.execute("""
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
""")
print()
print('Item                      Price')
print('-------------------------------')
for x in curs.fetchall():
    print(f'{x[0]:24} $ {x[1]}')

# What is the average age of an employee at the time of their hiring?

curs.execute("""
SELECT AVG(HireDate - BirthDate)
FROM Employee
""")
age = curs.fetchall()[0][0]
print()
print('Most Expensive items (per unit price):')
print(f'Average age when they were hired: {age:.2f}')

# How does the average age of employee at hire vary by city?
curs.execute("""
SELECT City, AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City
""")
print()
print('City           Age at hire (avg)')

for x in curs.fetchall():
    print(f'{x[0]:20} {x[1]}')


### Part 3


# What are the ten most expensive items (per unit price)
# in the database and their suppliers?
curs.execute("""
SELECT
    Product.ProductName AS "Product Name",
    Product.UnitPrice AS Price,
    Supplier.CompanyName AS "Supplier Name"
FROM Product, Supplier
WHERE Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
""")
print()
print('Item                      Price     Supplier')
print('--------------------------------------------')
for x in curs.fetchall():
    print(f'{x[0]:24} $ {x[1]:<6}   {x[2]}')


# What is the largest category (by number of products in it)?

curs.execute("""
SELECT CategoryName
FROM Category
WHERE Id =
        (
        SELECT
                Product.CategoryId
        FROM Product
        GROUP BY Product.CategoryId
        ORDER BY COUNT (Product.ProductName) DESC
        LIMIT 1
        )
""")
print()
print(f'Largest category: {curs.fetchall()[0][0]}')


# Who's the employee with the most territories?
curs.execute("""
SELECT
        FirstName, LastName,
        COUNT (TerritoryId) AS "Number of territories"
FROM Employee, EmployeeTerritory
WHERE Employee.Id =
        (
        SELECT
                EmployeeId
        FROM EmployeeTerritory
        GROUP BY EmployeeId
        ORDER BY COUNT (TerritoryId) DESC
        LIMIT 1
        )
""")
x = curs.fetchall()
