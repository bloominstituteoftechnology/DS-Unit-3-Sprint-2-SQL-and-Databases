import sqlite3

connection = sqlite3.connect('northwind_small.sqlite3')
curs = connection.cursor()

# Part 2
print ('_____Part 2 Questions_____')
# What are the ten most expensive items (per unit price) in the database?
expensive_items_query = 'SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC;'
print ('Ten Most Expensive Items:',connection.cursor().execute(expensive_items_query).fetchmany(10), '\n')

# What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)
employee_age_query = 'SELECT AVG(HireDate - BirthDate) FROM Employee'
print ('Average Hire Age::',connection.cursor().execute(employee_age_query).fetchone()[0], '\n')

# (*Stretch*) How does the average age of employee at hire vary by city?
employee_age_by_city_query = """SELECT City, AVG(HireDate - BirthDate) FROM Employee GROUP BY City"""
print ('Average Hire Age by City:',connection.cursor().execute(employee_age_by_city_query).fetchall(), '\n')

# Part 3
print ('\n_____Part 3 Questions_____')
# What are the ten most expensive items (per unit price) in the database *and*
# their suppliers?
expensive_suppliers_query = """SELECT Product.ProductName, Product.UnitPrice,Supplier.CompanyName FROM Product, Supplier WHERE Product.SupplierID = Supplier.ID ORDER BY UnitPrice DESC"""
print ('Expensive Items and their Suppliers:',connection.cursor().execute(expensive_suppliers_query).fetchmany(10), '\n')


# What is the largest category (by number of products in it)?
category_count_query = """SELECT Category.CategoryName, COUNT(Category.CategoryName) AS counts FROM Product, Category WHERE Product.CategoryID = Category.ID GROUP BY Category.CategoryName ORDER BY counts DESC"""
print ('Most Popular Category:',connection.cursor().execute(category_count_query).fetchone(), '\n')


# Who's the employee with the most territories?
employee_territories_query = """SELECT Employee.FirstName, Employee.LastName, COUNT(EmployeeID) AS territory_count FROM Employee, EmployeeTerritory WHERE Employee.ID = EmployeeTerritory.EmployeeID GROUP BY EmployeeID ORDER BY territory_count DESC"""
print ('Employee with Most Territories:',connection.cursor().execute(employee_territories_query).fetchone(), '\n')

