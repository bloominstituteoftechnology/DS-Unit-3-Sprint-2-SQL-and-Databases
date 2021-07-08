import sqlite3

# Part 2

# Create connection to northwind database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
curs.execute('''SELECT ProductName, UnitPrice 
                FROM Product
                ORDER BY UnitPrice DESC
                LIMIT 10;
                ''')
curs.fetchall()
# Output: [('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97),
# ("Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55),
# ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
curs.execute('''SELECT AVG(HireDate - BirthDate) AS avg_age
                FROM Employee;''')
curs.fetchall()
# Output: [(37.22222222222222,)]

# Part 3

# What are the ten most expensive items (per unit price) in the database and their suppliers?
curs.execute('''SELECT CompanyName, ProductName, UnitPrice
                FROM Product, Supplier
                GROUP BY ProductName
                ORDER BY UnitPrice DESC
                LIMIT 10;
                ''')
curs.fetchall()

# What is the largest category (by number of unique products in it)?
curs.execute('''SELECT c.CategoryName, COUNT(p.CategoryID)
                FROM Product AS p
                INNER JOIN Category AS c
                ON p.CategoryID = c.ID
                GROUP BY c.ID
                ORDER BY COUNT(p.CategoryID) DESC
                LIMIT 1;''')
curs.fetchall()
# Output: [('Confections', 13)]
