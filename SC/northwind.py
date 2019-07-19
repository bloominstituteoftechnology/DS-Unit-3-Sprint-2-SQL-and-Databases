# Import required library
import sqlite3

# Create the connection to db
conn = sqlite3.connect('northwind_small.sqlite3')

# Create the cursor to parse the db
c = conn.cursor()
print('Cursor open')

# Review tables
c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()

# Answer part 2 question 1
# Review the product table
c.execute('SELECT sql FROM sqlite_master WHERE name="Product";').fetchall()

# Calculate 10 most expensive items
ei = c.execute('SELECT ProductName, UnitPrice from Product ORDER BY UnitPrice DESC LIMIT 10').fetchall()
print('Top 10 most expensive products:', ei)

# Answer part 2 question 2
# Review employee table
c.execute('SELECT sql FROM sqlite_master WHERE name="Employee";').fetchall()

# Review date data
c.execute('SELECT HireDate, BirthDate, (HireDate - Birthdate) as Age from Employee LIMIT 10').fetchall()

# Calculate average age of employee at time of hiring
a = c.execute('SELECT avg((HireDate - BirthDate)) as AvgAge from Employee').fetchall()
print('The average Age of an employee at hire is:', a[0])

# Answer part 2 stretch question 3
ac = c.execute('SELECT City, avg(HireDate-Birthdate) AS AvgAge from Employee GROUP BY City').fetchall()
print('The average employee age by city', ac)

# Answer part 3 question 1
print('Top 10 Products with Supplier by Price')
ps = c.execute('SELECT P.ProductName, P.UnitPrice, S.CompanyName from Product as P LEFT JOIN Supplier as S on P.SupplierID = S.Id ORDER BY P.UnitPrice DESC LIMIT 10').fetchall()
print('Name:', ps)

# Answer part 3 question 2
cp = c.execute('SELECT C.CategoryName, count(P.ProductName) AS UniqueProds from Product as P LEFT JOIN Category as C on P.CategoryID = C.Id GROUP BY C.CategoryName ORDER BY UniqueProds DESC LIMIT 1').fetchall()
print('Category with most unique products:',cp)

# Answer part 3 stretch question 3
emt = c.execute('SELECT E.FirstName, E.Lastname, count(ET.TerritoryID) AS CountTerritories from EmployeeTerritory AS ET LEFT JOIN Employee AS E ON ET.EmployeeID = E.ID GROUP BY E.FirstName, E.Lastname ORDER BY CountTerritories DESC LIMIT 1').fetchall()
print('Employee with most territories:', emt)

