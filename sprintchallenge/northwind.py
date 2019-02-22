import sqlite3

# Establish connection to sqlite db and create a cursor
conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

print('What are the ten most expensive items (per unit price) in the database?')
command = """
    SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
cur.execute(command)
print('(Product Name, Unit Price)')
for value in cur.fetchall():
    print(f'{value[0], value[1]}')

print('What is the average age of an employee at the time of their hiring?')
command = """
    SELECT AVG(HireDate - BirthDate)
    FROM Employee;
    """
cur.execute(command)
print(f'{int(cur.fetchall()[0][0])}')

print('(Stretch) How does the average age of employee at hire vary by city?')
command = """
    SELECT City, AVG(HireDate - BirthDate)
    FROM Employee
    GROUP BY City;
    """
cur.execute(command)
print('(City, Avg Age at Hire)')
for value in cur.fetchall():
    print(f'{value[0], value[1]}')

print('What are the ten most expensive items (per unit price) '
'in the database and their suppliers?')
command = """
    SELECT p.ProductName, p.UnitPrice, s.CompanyName
    FROM Product AS p
    INNER JOIN Supplier AS s
    ON p.SupplierId = s.Id
    ORDER BY p.UnitPrice DESC
    LIMIT 10;
    """
cur.execute(command)
print('(Product Name, Unit Price, CompanyName)')
for value in cur.fetchall():
    print(f'{value[0], value[1], value[2]}')

print('What is the largest category (by number of products in it)?')
command = """
    SELECT c.CategoryName, COUNT(c.CategoryName)
    FROM Product AS p
    INNER JOIN Category as c
    ON p.CategoryId = c.Id
    GROUP BY c.CategoryName
    ORDER BY COUNT(c.CategoryName) DESC
    LIMIT 1;
    """
cur.execute(command)
print(cur.fetchall())

print("(Stretch) Who's the employee with the most territories?")
command = """
    SELECT e.LastName, e.FirstName, COUNT(t.ID)
    FROM Employee as e,
    Territory as t,
    EmployeeTerritory AS et
    WHERE e.Id = et.EmployeeId
    AND t.Id = et.TerritoryId
    ORDER BY e.LastName, e.FirstName;
    """
cur.execute(command)
print(cur.fetchall())


