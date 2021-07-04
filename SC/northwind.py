import sqlite3

# create connection
sl_conn = sqlite3.connect('/Users/Elizabeth/sql/northwind_small.sqlite3')
curs = sl_conn.cursor()

# table names
# [('Category',), ('Customer',), ('CustomerCustomerDemo',),
# ('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
# ('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
# ('Territory',)]

# PART 2
# What are the ten most expensive items (per unit price) in the database?
query = """
        SELECT ProductName
        FROM Product
        ORDER BY UnitPrice
        LIMIT 10;
        """
answer = curs.execute(query).fetchall()
print('\nPART 2')
print('The ten most expensive items per unit price are:')
for i in answer:
    print('      {}'.format(i[0]))

# What is the average age of an employee at the time of their hiring?
query = """
        SELECT AVG(HireDate - BirthDate)
        FROM Employee;
        """
answer = curs.execute(query).fetchall()[0][0]
print('The avg age of an employee at the time of hiring is:', round(answer,2))


# (Stretch) How does the average age of employee at hire vary by city?
query = """
        SELECT City, AVG(HireDate - BirthDate)
        FROM Employee
        GROUP BY City;
        """
answer = curs.execute(query).fetchall()
print('The avg age of an employee in each city is:')
for i in answer:
    print('      {} : {}'.format(i[0],i[1]))

# PART 3
# What are the ten most expensive items (per unit price) in the database and their suppliers?
query = """
        SELECT Product.ProductName, Supplier.CompanyName 
        FROM Product
        JOIN Supplier ON Product.SupplierID = Supplier.ID
        ORDER BY Product.UnitPrice
        LIMIT 10;
        """
answer = curs.execute(query).fetchall()
print('\nPART 3')
print('The ten most expensive items per unit price and their suppliers are:')
for i in answer:
    print('      {} : {}'.format(i[0],i[1]))

# What is the largest category (by number of unique products in it)?
query = """
        SELECT Category.CategoryName
        FROM Product
        JOIN Category ON Product.CategoryID = Category.ID
        GROUP BY Product.CategoryID
        ORDER BY COUNT(DISTINCT Product.ID) DESC
        LIMIT 1;
        """
answer = curs.execute(query).fetchall()[0][0]
print('The largest category is:', answer)

