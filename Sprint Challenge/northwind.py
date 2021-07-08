import sqlite3

# Establish connection to database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
query = """SELECT ProductName
           FROM Product
           ORDER BY UnitPrice DESC
           LIMIT 10;"""
result = curs.execute(query)

print('The Ten Most Expensive Items (per unit price) are:')
for item in result.fetchall():
    print(item[0])
print('\n')

# What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)
query = """SELECT ROUND(AVG(HireDate - BirthDate), 2) as 'Average Worker Age at Hire'
           FROM Employee"""
result = curs.execute(query)

print('The average worker age at hire is:')
print(result.fetchall()[0][0])
print('\n')

# How does the average age of employee at hire vary by city?
query = """SELECT City, AVG(HireDate - BirthDate) as 'Average Worker Age at Hire'
           FROM Employee
           GROUP BY City"""
result = curs.execute(query)

print('Variation in Worker Age at Hire by City:')
for pair in result.fetchall():
    print(pair[0] + " " + str(pair[1]) + " years")

print('\n')

# What are the ten most expensive items (per unit price) in the database and
# their suppliers?
query = """SELECT ProductName as 'Product Name', Supplier.CompanyName as 'Supplier Name'
            FROM Product
            JOIN Supplier ON Product.SupplierId = Supplier.Id
            ORDER BY UnitPrice DESC
            LIMIT 10;"""
result = curs.execute(query)

print('The Ten Most Expensive Items (per unit price) and their suppliers are:')
print('Product, Supplier')
for item in result.fetchall():
    print(item[0] + ', ' + item[1])
print('\n')

# What is the largest category (by number of unique products in it)?
query = """SELECT category.CategoryName as 'Category w/ Most Unique Products'
            FROM Product
            JOIN category ON product.CategoryId = Category.Id
            GROUP BY CategoryId
            ORDER BY COUNT(CategoryId) DESC
            LIMIT 1;"""
result = curs.execute(query)

print('The largest category (by number of unique products in it) is:')
print(result.fetchall()[0][0])
print('\n')

# Who's the employee with the most territories? Use TerritoryId (not name,
# region, or other fields) as the unique identifier for territories.
query = """SELECT Employee.FirstName, Employee.LastName
            FROM EmployeeTerritory
            JOIN Employee ON EmployeeTerritory.EmployeeId = Employee.Id
            GROUP BY EmployeeId
            ORDER BY COUNT(TerritoryId) DESC
            LIMIT 1;"""
result = curs.execute(query)

print('The employee with the most territories is:')
result = result.fetchall()
print(result[0][0] + ' ' + result[0][1])

# Output
# The Ten Most Expensive Items (per unit price) are:
# Côte de Blaye
# Thüringer Rostbratwurst
# Mishi Kobe Niku
# Sir Rodney's Marmalade
# Carnarvon Tigers
# Raclette Courdavault
# Manjimup Dried Apples
# Tarte au sucre
# Ipoh Coffee
# Rössle Sauerkraut


# The average worker age at hire is:
# 37.22


# Variation in Worker Age at Hire by City:
# Kirkland 29.0 years
# London 32.5 years
# Redmond 56.0 years
# Seattle 40.0 years
# Tacoma 40.0 years


# The Ten Most Expensive Items (per unit price) and their suppliers are:
# Product, Supplier
# Côte de Blaye, Aux joyeux ecclésiastiques
# Thüringer Rostbratwurst, Plutzer Lebensmittelgroßmärkte AG
# Mishi Kobe Niku, Tokyo Traders
# Sir Rodney's Marmalade, Specialty Biscuits, Ltd.
# Carnarvon Tigers, Pavlova, Ltd.
# Raclette Courdavault, Gai pâturage
# Manjimup Dried Apples, G'day, Mate
# Tarte au sucre, Forêts d'érables
# Ipoh Coffee, Leka Trading
# Rössle Sauerkraut, Plutzer Lebensmittelgroßmärkte AG


# The largest category (by number of unique products in it) is:
# Confections


# The employee with the most territories is:
# Robert King
