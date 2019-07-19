import sqlite3


conn = sqlite3.connect('demo_data1.sqlite')
cursor = conn.cursor()
#anytime we are querying we commit
cursor.execute(''' CREATE TABLE demo
    (s TEXT NOT NULL,
    x INT NOT NULL,
    y INT NOT NULL);''')


cursor = conn.cursor()
cursor.execute("INSERT INTO demo (s, x, y) \
    VALUES ('g', 3, 9)");
cursor.execute("INSERT INTO demo (s, x, y) \
    VALUES ('g', 5, 7)");
cursor.execute("INSERT INTO demo (s, x, y) \
    VALUES ('g', 8, 7)");
conn.commit()


countrows = 'SELECT COUNT(*) FROM demo'
cursor.execute(countrows).fetchall()


atleastfive = 'SELECT COUNT(*) FROM demo WHERE x > 5 AND y > 5;'
cursor.execute(atleastfive).fetchall()


countvaluesy = 'SELECT COUNT(DISTINCT y) FROM demo;'
cursor.execute(countvaluesy).fetchall()

cursor.close()


conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()


conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()


# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
avgage = 'SELECT AVG(HireDate - BirthDate) FROM Employee;'
cursor.execute(avgage).fetchall()


# (Stretch) How does the average age of employee at hire vary by city?
avgagebycity = 'SELECT City, AVG(HireDate - BirthDate) FROM Employee GROUP BY City;'
cursor.execute(avgagebycity).fetchall()


avgagebycityvary = 'SELECT City, AVG(HireDate - BirthDate - 37.222) FROM Employee GROUP BY City;'
cursor.execute(avgagebycityvary).fetchall()


# What are the ten most expensive items (per unit price) in the database and their suppliers?
mostexpensivesupplier = 'SELECT ProductName, SupplierName FROM ProductDetails_V ORDER BY UnitPrice DESC LIMIT 10;'
cursor.execute(mostexpensivesupplier).fetchall()


# What is the largest category (by number of unique products in it)?
largestcategory = 'SELECT CategoryName, COUNT(DISTINCT ProductName) FROM ProductDetails_V GROUP BY CategoryName ORDER BY COUNT(DISTINCT ProductName) DESC LIMIT 1;'
cursor.execute(largestcategory).fetchall()


# (Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.
mostterritories = 'SELECT Employee.Id, Employee.FirstName, Employee.LastName, EmployeeTerritory.EmployeeId, EmployeeTerritory.TerritoryId, Territory.Id, Territory.TerritoryDescription \
                    FROM Employee \
                    INNER JOIN EmployeeTerritory ON Employee.Id = EmployeeTerritory.EmployeeId \
                    INNER JOIN Territory ON EmployeeTerritory.TerritoryId = Territory.Id;'
cursor.execute(mostterritories).fetchall()


mostterritories = 'SELECT Employee.FirstName, Employee.LastName, COUNT(DISTINCT EmployeeTerritory.TerritoryId) \
                    FROM Employee \
                    INNER JOIN EmployeeTerritory ON Employee.Id = EmployeeTerritory.EmployeeId \
                    INNER JOIN Territory ON EmployeeTerritory.TerritoryId = Territory.Id \
                    GROUP BY Employee.FirstName \
                    ORDER BY COUNT(DISTINCT EmployeeTerritory.TerritoryId) DESC \
                    LIMIT 1;'
cursor.execute(mostterritories).fetchall()


# In the Northwind database, what is the type of relationship between the Employee and Territory tables?
# There is a one-to-one relationship between each employee, their primary id's, matched with the EmployeeId vs TerritoryId keys of the
#EmployeeTerritory table, which then directly relates to the Territory table through the primary Id of the Territory table vs. the
#TerritoryId of the EmployeeTerritory table.


# What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
#MongoDB is great for securing data for web applications for use in BSON format for necessary retrieval.


# What is "NewSQL", and what is it trying to achieve?
#NewSQL is a class of databases that satisfies the scalability and elasticity of new SQL systems while maintaining
#ACID guarrantees, atomicity, consistency, isolation and durability, meaning that there is integrity of the entire
#database transaction pipeline, that the data that only follows specific rules will be written into the database, and that there
# are concurrent processes, and one process does not affect another, durability to make failures invisible to the end-user.