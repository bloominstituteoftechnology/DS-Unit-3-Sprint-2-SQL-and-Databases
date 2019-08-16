import sqlite3

conn = sqlite3.connect("northwind_small.sqlite3")

curs = conn.cursor()

query = """
    SELECT ProductName
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;"""
ten_most_expensive_items = curs.execute(query).fetchall()

query = """
    SELECT AVG(HireDate - BirthDate)
    FROM Employee;"""
average_age_at_hire = curs.execute(query).fetchall()[0][0]

query = """
    SELECT City, AVG(HireDate - BirthDate)
    FROM Employee
    GROUP BY City;"""
average_age_at_hire_by_city = curs.execute(query).fetchall()

query = """
    SELECT ProductName, CompanyName
    FROM Product
    INNER JOIN Supplier
    ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;"""
ten_most_expensive_items_and_their_suppliers = curs.execute(query).fetchall()

query = """
    SELECT CategoryName
    FROM Product
    INNER JOIN Category
    ON Product.CategoryId = Category.Id
    GROUP BY CategoryId
    ORDER BY COUNT(DISTINCT Product.Id) DESC
    LIMIT 1;"""
largest_category = curs.execute(query).fetchall()[0][0]

query = """
    SELECT TitleOfCourtesy, FirstName, LastName
    FROM EmployeeTerritory
    INNER JOIN Employee
    ON EmployeeTerritory.EmployeeId = Employee.Id
    GROUP BY EmployeeId
    ORDER BY COUNT(DISTINCT TerritoryId) DESC
    LIMIT 1;"""
employee_most_territories = (curs.execute(query).fetchall()[0][0] + " " +
                             curs.execute(query).fetchall()[0][1] + " " +
                             curs.execute(query).fetchall()[0][2])

curs.close()

print("Ten most expensive items:", ten_most_expensive_items,
      "\nAverage age at hire:", average_age_at_hire,
      "\nAverage at at hire by city:", average_age_at_hire_by_city,
      "\nTen most expensive items and their suppliers:",
      ten_most_expensive_items_and_their_suppliers,
      "\nLargest category:", largest_category,
      "\nEmployee with most territories:", employee_most_territories)

# Output:
#
# Ten most expensive items: [('Côte de Blaye',),
#                            ('Thüringer Rostbratwurst',),
#                            ('Mishi Kobe Niku',),
#                            ("Sir Rodney's Marmalade",),
#                            ('Carnarvon Tigers',),
#                            ('Raclette Courdavault',),
#                            ('Manjimup Dried Apples',),
#                            ('Tarte au sucre',),
#                            ('Ipoh Coffee',),
#                            ('Rössle Sauerkraut',)]
#
# Average age at hire: 37.22222222222222
#
# Average at at hire by city: [('Kirkland', 29.0),
#                              ('London', 32.5),
#                              ('Redmond', 56.0),
#                              ('Seattle', 40.0),
#                              ('Tacoma', 40.0)]
#
#
# Ten most expensive items and their suppliers:
#       [('Côte de Blaye', 'Aux joyeux ecclésiastiques'),
#        ('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG'),
#        ('Mishi Kobe Niku', 'Tokyo Traders'),
#        ("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'),
#        ('Carnarvon Tigers', 'Pavlova, Ltd.'),
#        ('Raclette Courdavault', 'Gai pâturage'),
#        ('Manjimup Dried Apples', "G'day, Mate"),
#        ('Tarte au sucre', "Forêts d'érables"),
#        ('Ipoh Coffee', 'Leka Trading'),
#        ('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]
# 
# Largest category: Confections
#
# Employee with most territories: Mr. Robert King
