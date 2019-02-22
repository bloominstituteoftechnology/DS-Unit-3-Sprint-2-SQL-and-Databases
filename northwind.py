"""
Answers some basic questions about northwind data
"""

import sqlite3

try:
    from tabulate import tabulate
except ImportError:
    raise ImportError('Please install tablulate module for nicely '
                      'formatted printing :)')

# initialize connection and cursor
connection = sqlite3.connect('northwind_small.sqlite3')
curs = connection.cursor()

# Part 2
print ('_____Part 2 Questions_____')
# What are the ten most expensive items (per unit price) in the database?
expensive_items_query = """SELECT ProductName, UnitPrice FROM Product
    ORDER BY UnitPrice DESC"""
expensive_items = curs.execute(expensive_items_query).fetchmany(10)
print ('\nTen Most Expensive Items')
print (tabulate(expensive_items,
                headers=['Item Name', 'Unit Cost']))

# What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)
employee_age_query = 'SELECT AVG(HireDate - BirthDate) FROM Employee'
average_hire_age = curs.execute(employee_age_query).fetchone()[0]
print ('\nAverage Hire Age: %.2f' % average_hire_age)

# (*Stretch*) How does the average age of employee at hire vary by city?
employee_age_by_city_query = """SELECT
    City, AVG(HireDate - BirthDate)
    FROM Employee
    GROUP BY City"""
employee_age_by_city = curs.execute(employee_age_by_city_query).fetchall()
print ('\nAverage Hire Age by City')
print (tabulate(employee_age_by_city,
                headers=['City', 'Average Hire Age']))

# Part 3
print ('\n_____Part 3 Questions_____')
# What are the ten most expensive items (per unit price) in the database *and*
# their suppliers?
expensive_suppliers_query = """SELECT Product.ProductName, Product.UnitPrice,
    Supplier.CompanyName
    FROM Product, Supplier
    WHERE Product.SupplierID = Supplier.ID
    ORDER BY UnitPrice DESC"""
expensive_suppliers = curs.execute(expensive_suppliers_query).fetchmany(10)
print ('\nExpensive Items and their Suppliers')
print (tabulate(expensive_suppliers,
                headers=['Item Name', 'Unit Cost', 'Supplier Name']))

# What is the largest category (by number of products in it)?
category_count_query = """SELECT Category.CategoryName,
    COUNT(Category.CategoryName) AS counts FROM Product, Category
    WHERE Product.CategoryID = Category.ID
    GROUP BY Category.CategoryName
    ORDER BY counts DESC"""

category_count = curs.execute(category_count_query).fetchone()
print ('\nMost Popular Category: %s has %d offerings' % category_count)

# Who's the employee with the most territories?
employee_territories_query = """SELECT Employee.FirstName,
    Employee.LastName, COUNT(EmployeeID) AS territory_count
    FROM Employee, EmployeeTerritory
    WHERE Employee.ID = EmployeeTerritory.EmployeeID
    GROUP BY EmployeeID
    ORDER BY territory_count DESC
"""
top_employee = curs.execute(employee_territories_query).fetchone()
print ('\nEmployee with Most Territories: %s %s (%d)' % top_employee)
