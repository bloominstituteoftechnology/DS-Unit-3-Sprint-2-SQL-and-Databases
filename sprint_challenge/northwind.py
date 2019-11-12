import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


print("What are the ten most expensive items (per unit price) in the database?")
query = 'SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
print(curs.execute(query).fetchall())


print("\nWhat is the average age at hire?")
query = 'SELECT ROUND(AVG(HireDate - BirthDate)) as "average hire age" from Employee;'
print(curs.execute(query).fetchall())


print("\nWhat is the average age by city?")
query = 'SELECT City, ROUND(AVG(HireDate - BirthDate)) as "average hire age by City" from Employee GROUP BY City;'
print(curs.execute(query).fetchall())


print("\n\nPart 4 Questions")


print("\n\nWhat are the 10 most expensive items AND their Supplier?")
query = 'SELECT ProductName, UnitPrice, CompanyName from Product JOIN Supplier ON Product.SupplierID = Supplier.Id ORDER BY UnitPrice DESC LIMIT 10;'
print(curs.execute(query).fetchall())


print("\nWhat is the largest category (by unique products)")
query = 'SELECT CategoryName, COUNT(ProductName) as "count" FROM Product JOIN Category ON Product.CategoryId = Category.Id GROUP BY CategoryName ORDER BY "count" DESC LIMIT 1;'
print(curs.execute(query).fetchall())


print("\nWho's the employee with the most territories?")
query = "SELECT FirstName || ' ' ||  LastName as fullname FROM Employee JOIN EmployeeTerritory ON Employee.Id = EmployeeTerritory.EmployeeId GROUP BY fullname ORDER BY COUNT( DISTINCT TerritoryId) DESC LIMIT 1;"
print(curs.execute(query).fetchall())
