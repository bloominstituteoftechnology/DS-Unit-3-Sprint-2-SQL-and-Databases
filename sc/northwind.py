import sqlite3

conn = sqlite3.connect("northwind_small.sqlite3")
print('CONNECTION:', conn)
curs = conn.cursor()
print('CURSOR:', curs, '\n')


# What are the ten most expensive items (per unit price) in the database?
curs.execute("""
            SELECT ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;""")
most_exp = curs.fetchall()
print('10 most expensive items and their prices: ', most_exp, '\n')
''' ANSWER
[('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79),
('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81),
('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55),
('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3),
 ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]
 '''

# What is the average age of an employee at the time of their hiring?
# (Hint: a lot of arithmetic works with dates.)
curs.execute("""
            SELECT AVG(HireDate - BirthDate) FROM Employee;""")
avg_age = curs.fetchall()
print('Average age of employee at time of hiring: ', avg_age, '\n')
'''
ANSWER 37.2222222
 '''

# What are the ten most expensive items (per unit price)
# in the database and their suppliers?
curs.execute("""
            SELECT ProductName, CompanyName FROM Product
JOIN Supplier ON Product.Supplierid = Supplier.id
ORDER BY UnitPrice DESC
LIMIT 10;""")
most_exp_supp = curs.fetchall()
print('10 most expensive items and their suppliers: ', most_exp_supp, '\n')
''' ANSWER
[('Côte de Blaye', 'Aux joyeux ecclésiastiques'),
('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG'),
('Mishi Kobe Niku', 'Tokyo Traders'),
("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'),
('Carnarvon Tigers', 'Pavlova, Ltd.'),
('Raclette Courdavault', 'Gai pâturage'),
('Manjimup Dried Apples', "G'day, Mate"),
('Tarte au sucre', "Forêts d'érables"),
('Ipoh Coffee', 'Leka Trading'),
('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]
 '''

# What is the largest category (by number of unique products in it)?
curs.execute("""
            SELECT CategoryName, COUNT(CategoryId) FROM Product
JOIN Category ON Product.CategoryId = Category.id
GROUP BY CategoryId
ORDER BY COUNT(CategoryId) DESC
LIMIT 1;""")
larg_cat = curs.fetchall()
print('Largest category by number of unique products: ', larg_cat, '\n')
'''
ANSWER Confections, 13 products
 '''
