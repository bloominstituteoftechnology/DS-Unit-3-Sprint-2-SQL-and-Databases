
import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

# What are the ten most expensive items (per unit price) in the database?
curs = conn.cursor()
curs.execute("""
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;""")
result = curs.fetchall()

print(result)

# What is the average age of an employee at the time of their hiring? 
# (Hint: a lot of arithmetic works with dates.)

curs = conn.cursor()
curs.execute("""SELECT AVG(birthdate - hiredate)FROM Employee;""")

result = curs.fetchall()
result = float(result[0][0] * -1)

print("Average Age At Hiring: ", result)

# STRETCH: How does the average age of employee at hire vary by city?
# TODO After Finishing

# What are the ten most expensive items (per unit price) in the database
# and their suppliers?

curs = conn.cursor()
curs.execute("""
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product, Supplier
    WHERE Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;""")
result = curs.fetchall()

print('Top 10 Most Expensive Items: ', result)

# What is the largest category (by number of unique products in it)?

curs = conn.cursor()
curs.execute("""
    SELECT CategoryName, COUNT(Product.CategoryId) AS NumberOfProducts
    FROM Category, Product
    WHERE Category.Id = Product.CategoryId
    GROUP BY CategoryName
    ORDER BY NumberOfProducts DESC
    LIMIT 1;""")
result = curs.fetchall()
print('Largest Category by Number of Unique Products: ', result)

#(Stretch) Who's the employee with the most territories? 
# Use TerritoryId (not name, region, or other fields) as the 
# unique identifier for territories.
# ATTEMPTED: NOT SURE IF ACCURATE RESULT

curs = conn.cursor()
curs.execute("""
SELECT e.Id, e.LastName, e.FirstName,
COUNT(distinct et.TerritoryId) count_territories
FROM EmployeeTerritory et
JOIN Employee e on e.Id = et.EmployeeId
GROUP BY e.Id
ORDER BY COUNT(distinct et.TerritoryId) DESC
LIMIT 1;""") 
result = curs.fetchall()
result = result[0][0:4]
print("Employee with the most territories: ", result)
