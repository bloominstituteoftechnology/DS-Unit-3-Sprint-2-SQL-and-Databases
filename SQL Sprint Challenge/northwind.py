import sqlite3 as sql

connection  = sql.connect('northwind_small.sqlite3')
c = connection.cursor()

# part 2

print("""
What are the ten most expensive items (per unit price) in the database?""")
c.execute("""
    SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
""")
print(c.fetchall())

print("""
What is the average age of an employee at the time of their hiring?""")
c.execute("""
    SELECT AVG(HireDate - BirthDate)
    FROM employee;
""")
print(c.fetchone())


print("""
How does the average age of employee at hire vary by city?""")
c.execute("""
    SELECT AVG(HireDate - BirthDate)
    FROM employee
    GROUP BY City;
""")
print(c.fetchall())

# part 3
print("""
What are the ten most expensive items (per unit price) in the database *and*
  their suppliers?""")
c.execute("""
    SELECT Supplier.CompanyName, Product.ProductName, Product.UnitPrice
    FROM Product 
    JOIN Supplier  ON Supplier.Id = Product.SupplierId
    ORDER BY UnitPrice DESC
    LIMIT 10;
""")
print(c.fetchall())

print("""
What is the largest category?""")
c.execute("""
    SELECT Category.CategoryName, COUNT(Product.Id) prod_count
    FROM Product 
    JOIN Category ON Category.Id = Product.CategoryId
    GROUP BY Category.CategoryName
    ORDER BY COUNT(Product.Id) DESC
    LIMIT 1;
""")
print(c.fetchone())

print("""
Who's the employee with the most territories?""")
c.execute("""
    SELECT Employee.Id, Employee.LastName, Employee.FirstName,
    COUNT(DISTINCT EmployeeTerritory.TerritoryId) count_territories
    FROM EmployeeTerritory
    JOIN Employee on Employee.Id = EmployeeTerritory.EmployeeId
    GROUP BY Employee.Id
    ORDER BY COUNT(distinct EmployeeTerritory.TerritoryId) DESC
    LIMIT 1;
""")
print(c.fetchone())

connection.close()